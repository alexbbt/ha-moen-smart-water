"""Valve platform for Moen Smart Water integration."""

from __future__ import annotations

import asyncio
import logging
from typing import Any

from homeassistant.components.valve import (
    ValveEntity,
    ValveEntityDescription,
    ValveEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import MoenDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


VALVE_DESCRIPTIONS: list[ValveEntityDescription] = [
    ValveEntityDescription(
        key="water_control",
        name="Water Control",
        device_class="water",
        icon="mdi:valve",
    ),
]


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Moen Smart Water valve entities."""
    coordinator: MoenDataUpdateCoordinator = hass.data["moen_smart_water"][
        config_entry.entry_id
    ]

    # Get devices and create entities for each
    devices = coordinator.get_all_devices()
    _LOGGER.info(
        "Setting up valve entities. Found %d devices: %s",
        len(devices),
        list(devices.keys()),
    )

    entities = []
    for device_id, device in devices.items():
        device_name = device.get("name", f"Moen Smart Water {device_id}")
        _LOGGER.info("Creating valve entity for device %s: %s", device_id, device_name)

        for description in VALVE_DESCRIPTIONS:
            entities.append(
                MoenFaucetValve(coordinator, device_id, device_name, description)
            )

    _LOGGER.info("Adding %d valve entities", len(entities))
    async_add_entities(entities)


class MoenFaucetValve(CoordinatorEntity, ValveEntity):
    """Valve entity for Moen Smart Water water control."""

    def __init__(
        self,
        coordinator: MoenDataUpdateCoordinator,
        device_id: str,
        device_name: str,
        description: ValveEntityDescription,
    ) -> None:
        """Initialize the valve entity."""
        super().__init__(coordinator)
        self._device_id = device_id
        self._device_name = device_name
        self.entity_description = description
        self._attr_unique_id = f"{device_id}_{description.key}"
        self._attr_has_entity_name = True

        # Valve features
        self._attr_supported_features = (
            ValveEntityFeature.OPEN
            | ValveEntityFeature.CLOSE
            | ValveEntityFeature.SET_POSITION
        )

        # Valve state
        self._attr_is_closed = True
        self._attr_is_opening = False
        self._attr_is_closing = False
        self._attr_valve_position = 0  # 0-100 for flow rate
        self._attr_reports_position = True  # Required for valve entities
        self._attr_state = "closed"  # Primary state: open, opening, closed, closing, stopped, unavailable, unknown

        # Device flow rate constraints (will be updated from device shadow)
        self._min_flow_rate = 10  # Default to trickleFlowRate
        self._max_flow_rate = 100  # Default to maxFlowRate

        # Additional attributes for temperature and status
        self._attr_temperature = 20.0
        self._attr_preset_mode = "coldest"
        self._attr_extra_state_attributes = {}

        # Track manual state changes to prevent coordinator from overriding
        self._manual_close_requested = False
        self._manual_open_requested = False

        # Device information
        self._attr_device_info = DeviceInfo(
            identifiers={("moen_smart_water", device_id)},
            name=device_name,
            manufacturer="Moen",
            model="Smart Faucet",
        )

    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        shadow = self.coordinator.get_device_shadow(self._device_id)
        if shadow:
            state = shadow.get("state", {}).get("reported", {})
            self._update_valve_state_from_data(state, "coordinator")

        self.async_write_ha_state()

    @property
    def state(self) -> str:
        """Return the current state of the valve."""
        return self._attr_state

    def _update_valve_state_from_data(
        self, state: dict, source: str = "coordinator"
    ) -> None:
        """Update valve state and attributes from API data. Shared by coordinator and manual updates."""
        _LOGGER.debug(
            "%s UPDATE: Raw state data for device %s: %s",
            source.upper(),
            self._device_id,
            state,
        )

        device_state = state.get("state", "idle")
        # flowRate is only present when water is actively running
        # When idle, use defaultFlowRate to show what rate will be used when opened
        flow_rate = state.get("flowRate") or state.get("defaultFlowRate")
        temperature_celsius = state.get("temperature", 20.0)

        # Convert Celsius to Fahrenheit: F = (C * 9/5) + 32
        temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32

        # Update flow rate constraints from device shadow
        trickle_flow_rate = state.get("trickleFlowRate")
        max_flow_rate = state.get("maxFlowRate")
        if trickle_flow_rate is not None:
            self._min_flow_rate = int(trickle_flow_rate)
        if max_flow_rate is not None:
            self._max_flow_rate = int(max_flow_rate)

        _LOGGER.debug(
            "%s UPDATE: Parsed values - device_state=%s, flow_rate=%s, temperature=%s°C (%.1f°F), min_flow=%d%%, max_flow=%d%%",
            source.upper(),
            device_state,
            flow_rate,
            temperature_celsius,
            temperature_fahrenheit,
            self._min_flow_rate,
            self._max_flow_rate,
        )

        # Determine if valve is open based on device state and flow rate
        # If we manually changed the valve state, respect that until API confirms
        if source == "coordinator" and self._manual_close_requested:
            is_valve_open = False
            self._manual_close_requested = False  # Reset flag after one update
            _LOGGER.debug("VALVE STATE: Using manual close flag, setting closed")
        elif source == "coordinator" and self._manual_open_requested:
            is_valve_open = True
            self._manual_open_requested = False  # Reset flag after one update
            _LOGGER.debug("VALVE STATE: Using manual open flag, setting open")
        else:
            # Valve is open if:
            # 1. Device state is "running", OR
            # 2. We have a valid flow rate > 0
            is_valve_open = device_state == "running" or (
                flow_rate is not None and flow_rate != "unknown" and flow_rate > 0
            )
            _LOGGER.debug(
                "VALVE STATE: Using API data, is_valve_open=%s", is_valve_open
            )

        # Update valve state attributes
        if is_valve_open:
            self._attr_is_closed = False
            self._attr_is_opening = False
            self._attr_is_closing = False
            self._attr_state = "open"
            _LOGGER.debug("VALVE STATE: Setting to OPEN")
        else:
            self._attr_is_closed = True
            self._attr_is_opening = False
            self._attr_is_closing = False
            self._attr_state = "closed"
            _LOGGER.debug("VALVE STATE: Setting to CLOSED")

        # Update valve position (flow rate)
        if flow_rate is not None and flow_rate != "unknown":
            # Use flow rate from API (either active flowRate or defaultFlowRate)
            self._attr_valve_position = int(flow_rate)

        # If valve is closed and we have no flow rate data, set position to 0
        if not is_valve_open and (flow_rate is None or flow_rate == "unknown"):
            self._attr_valve_position = 0

        # Update temperature (store in Fahrenheit)
        self._attr_temperature = temperature_fahrenheit

        # Update extra state attributes
        # Note: The Moen API reports flowRate when actively running, otherwise
        # it reports defaultFlowRate (the rate used for gesture activation).
        # valve_position represents the current or default flow rate (0-100%)
        attributes = {
            "valve_state": self._attr_state,
            "faucet_state": device_state,
            "preset_mode": self._attr_preset_mode,
            "is_valve_open": is_valve_open,
            "temperature": f"{temperature_fahrenheit:.1f} °F",
            "temperature_celsius": f"{temperature_celsius:.1f} °C",
            "valve_position": f"{self._attr_valve_position}%",
            "min_flow_rate": f"{self._min_flow_rate}%",
            "max_flow_rate": f"{self._max_flow_rate}%",
        }

        # Only include api_flow_rate if we actually got one from the API
        # (API typically doesn't include this field in device shadow)
        if flow_rate is not None and flow_rate != "unknown":
            attributes["api_flow_rate"] = f"{flow_rate}%"

        self._attr_extra_state_attributes.update(attributes)

        _LOGGER.debug(
            "%s UPDATE: Updated state to %s, position=%s",
            source.upper(),
            self._attr_state,
            self._attr_valve_position,
        )

    def _clamp_flow_rate(self, flow_rate: int) -> int:
        """Clamp flow rate to device constraints.

        Args:
            flow_rate: The requested flow rate (0-100)

        Returns:
            Clamped flow rate (0 for closed, or min_flow_rate to max_flow_rate)
        """
        if flow_rate == 0:
            # 0 means close valve, don't clamp
            return 0

        # For any non-zero value, enforce minimum (trickleFlowRate)
        if flow_rate < self._min_flow_rate:
            _LOGGER.info(
                "Flow rate %d%% is below minimum %d%%, clamping to minimum",
                flow_rate,
                self._min_flow_rate,
            )
            return self._min_flow_rate

        # Enforce maximum (maxFlowRate)
        if flow_rate > self._max_flow_rate:
            _LOGGER.info(
                "Flow rate %d%% is above maximum %d%%, clamping to maximum",
                flow_rate,
                self._max_flow_rate,
            )
            return self._max_flow_rate

        return flow_rate

    async def _manual_update_from_api(self) -> None:
        """Manually update valve state with fresh API data, bypassing coordinator cache."""
        try:
            _LOGGER.debug("MANUAL UPDATE: Getting fresh API data")
            # Get fresh device shadow data directly from API
            shadow = await self.hass.async_add_executor_job(
                self.coordinator.api.get_device_shadow, self._device_id
            )

            if shadow:
                state = shadow.get("state", {}).get("reported", {})
                self._update_valve_state_from_data(state, "manual")
                # Update Home Assistant immediately
                self.async_write_ha_state()
            else:
                _LOGGER.warning("MANUAL UPDATE: No device shadow data available")

        except Exception as err:
            _LOGGER.error("MANUAL UPDATE: Failed to get fresh API data: %s", err)

    async def _delayed_api_check(self) -> None:
        """Wait a few seconds then check API to confirm valve state."""
        _LOGGER.debug("DELAYED CHECK: Waiting 5 seconds for API to update...")
        await asyncio.sleep(5)  # Wait 5 seconds for API to catch up
        _LOGGER.debug("DELAYED CHECK: Checking API after delay")
        await self._manual_update_from_api()

    async def async_open_valve(self, **kwargs: Any) -> None:
        """Open the valve (start water flow)."""
        try:
            _LOGGER.info("Opening valve for device %s", self._device_id)

            # Call the API to start water flow - use valve position as flow rate percentage
            # If valve is closed (0%), default to defaultFlowRate from device, or min_flow_rate as fallback
            if self._attr_valve_position > 0:
                flow_rate = int(self._attr_valve_position)
            else:
                # Get defaultFlowRate from device state
                shadow = self.coordinator.get_device_shadow(self._device_id)
                state = shadow.get("state", {}).get("reported", {}) if shadow else {}
                default_flow_rate = state.get("defaultFlowRate")
                flow_rate = (
                    int(default_flow_rate) if default_flow_rate else self._min_flow_rate
                )

            # Clamp flow rate to device constraints
            flow_rate = self._clamp_flow_rate(flow_rate)

            # Get current temperature setting from device state to preserve it
            shadow = self.coordinator.get_device_shadow(self._device_id)
            if not shadow:
                temperature_to_use = "coldest"
            else:
                reported = shadow.get("state", {}).get("reported", {})
                desired = shadow.get("state", {}).get("desired", {})
                temperature_goal = reported.get("temperatureGoal", "coldest")

                # Determine temperature to use:
                # 1. Check desired state for last commanded temperature
                # 2. If temperatureGoal is "specific", use the specific temperature value
                # 3. Otherwise, use the preset (coldest, warm, hottest)
                desired_temp = desired.get("temperature")
                if desired_temp is not None:
                    # Use the last commanded temperature from desired state
                    temperature_to_use = desired_temp
                    _LOGGER.debug(
                        "Valve open: preserving temperature %s from desired state",
                        desired_temp,
                    )
                elif temperature_goal == "specific":
                    # Use the specific temperature from reported state
                    temperature_value = reported.get("temperature")
                    if temperature_value is not None:
                        temperature_to_use = temperature_value
                        _LOGGER.debug(
                            "Valve open: preserving specific temperature of %.1f°C",
                            temperature_value,
                        )
                    else:
                        # Fallback to preset mode if temperature value not available
                        temperature_to_use = self._attr_preset_mode
                        _LOGGER.debug(
                            "Valve open: specific temp not available, using preset %s",
                            self._attr_preset_mode,
                        )
                else:
                    # Use the temperature goal from device state (coldest, warm, hottest)
                    temperature_to_use = temperature_goal
                    _LOGGER.debug(
                        "Valve open: preserving temperature preset %s",
                        temperature_goal,
                    )

            _LOGGER.info(
                "Opening valve with temperature %s and %d%% flow rate",
                temperature_to_use,
                flow_rate,
            )

            # Start water flow with current temperature and flow rate
            await self.hass.async_add_executor_job(
                self.coordinator.api.start_water_flow,
                self._device_id,
                temperature_to_use,
                flow_rate,
            )

            # Update valve position to reflect actual flow rate
            self._attr_valve_position = flow_rate

            # Set valve to "open" state immediately (optimistic update)
            # This keeps the toggle visible in the UI
            self._attr_is_closed = False
            self._attr_is_opening = False
            self._attr_is_closing = False
            self._attr_state = "open"
            self.async_write_ha_state()

            # Set manual flag and check API after delay
            self._manual_open_requested = True
            await self._delayed_api_check()
            _LOGGER.info("Successfully opened valve for device %s", self._device_id)

        except Exception as err:
            _LOGGER.error(
                "Failed to open valve for device %s: %s", self._device_id, err
            )
            raise

    async def async_close_valve(self, **kwargs: Any) -> None:
        """Close the valve (stop water flow)."""
        try:
            _LOGGER.info("Closing valve for device %s", self._device_id)

            # Call the API to stop water flow
            await self.hass.async_add_executor_job(
                self.coordinator.api.stop_water_flow, self._device_id
            )

            # Set valve to "closed" state immediately (optimistic update)
            # This keeps the toggle visible in the UI
            self._attr_is_closed = True
            self._attr_is_opening = False
            self._attr_is_closing = False
            self._attr_state = "closed"
            self._attr_valve_position = 0
            self.async_write_ha_state()

            # Set manual flag and check API after delay
            self._manual_close_requested = True
            await self._delayed_api_check()
            _LOGGER.info("Successfully closed valve for device %s", self._device_id)

        except Exception as err:
            _LOGGER.error(
                "Failed to close valve for device %s: %s", self._device_id, err
            )
            raise

    async def async_stop_valve(self, **kwargs: Any) -> None:
        """Stop the valve (same as close for faucet)."""
        await self.async_close_valve(**kwargs)

    async def async_toggle(self) -> None:
        """Toggle the valve open/closed."""
        if self._attr_is_closed:
            await self.async_open_valve()
        else:
            await self.async_close_valve()

    async def async_set_valve_position(self, position: float) -> None:
        """Set the valve position (flow rate 0-100) and start water flow."""
        try:
            requested_position = int(position)
            _LOGGER.info(
                "Setting valve position to %d%% for device %s",
                requested_position,
                self._device_id,
            )

            # Clamp position to device constraints (0, or min_flow_rate to max_flow_rate)
            clamped_position = self._clamp_flow_rate(requested_position)

            if clamped_position != requested_position:
                _LOGGER.info(
                    "Requested position %d%% adjusted to %d%% to respect device constraints (min=%d%%, max=%d%%)",
                    requested_position,
                    clamped_position,
                    self._min_flow_rate,
                    self._max_flow_rate,
                )

            # Update the valve position
            self._attr_valve_position = clamped_position

            # If position is 0, close the valve
            if clamped_position == 0:
                if not self._attr_is_closed:
                    _LOGGER.info("Position set to 0%, closing valve")
                    # Call stop_water_flow directly like the stop button does
                    await self.hass.async_add_executor_job(
                        self.coordinator.api.stop_water_flow, self._device_id
                    )
                    # Set valve to "closed" state immediately (optimistic update)
                    # This keeps the toggle visible in the UI
                    self._attr_is_closed = True
                    self._attr_is_opening = False
                    self._attr_is_closing = False
                    self._attr_state = "closed"
                    self.async_write_ha_state()

                    # Check API after delay
                    await self._delayed_api_check()
                    _LOGGER.info(
                        "Successfully stopped water flow for device %s", self._device_id
                    )
                else:
                    _LOGGER.info("Valve already closed")
            else:
                # Position > 0, start water flow with current temperature setting and new flow rate
                # Get current temperature setting from device state to preserve it
                shadow = self.coordinator.get_device_shadow(self._device_id)
                if not shadow:
                    temperature_to_use = "coldest"
                else:
                    reported = shadow.get("state", {}).get("reported", {})
                    desired = shadow.get("state", {}).get("desired", {})
                    temperature_goal = reported.get("temperatureGoal", "coldest")

                    # Determine temperature to use:
                    # 1. Check desired state for last commanded temperature
                    # 2. If temperatureGoal is "specific", use the specific temperature value
                    # 3. Otherwise, use the preset (coldest, warm, hottest)
                    desired_temp = desired.get("temperature")
                    if desired_temp is not None:
                        # Use the last commanded temperature from desired state
                        temperature_to_use = desired_temp
                        _LOGGER.debug(
                            "Flow rate change: preserving temperature %s from desired state",
                            desired_temp,
                        )
                    elif temperature_goal == "specific":
                        # Use the specific temperature from reported state
                        temperature_value = reported.get("temperature")
                        if temperature_value is not None:
                            temperature_to_use = temperature_value
                            _LOGGER.debug(
                                "Flow rate change: preserving specific temperature of %.1f°C",
                                temperature_value,
                            )
                        else:
                            # Fallback to preset mode if temperature value not available
                            temperature_to_use = self._attr_preset_mode
                            _LOGGER.debug(
                                "Flow rate change: specific temp not available, using preset %s",
                                self._attr_preset_mode,
                            )
                    else:
                        # Use the temperature goal from device state (coldest, warm, hottest)
                        temperature_to_use = temperature_goal
                        _LOGGER.debug(
                            "Flow rate change: preserving temperature preset %s",
                            temperature_goal,
                        )

                _LOGGER.info(
                    "Starting water flow with temperature %s and %d%% flow rate",
                    temperature_to_use,
                    clamped_position,
                )

                # Start water flow with current temperature and new flow rate
                await self.hass.async_add_executor_job(
                    self.coordinator.api.start_water_flow,
                    self._device_id,
                    temperature_to_use,
                    clamped_position,
                )

                # Set valve to "open" state immediately (optimistic update)
                # This keeps the toggle visible in the UI
                self._attr_is_closed = False
                self._attr_is_opening = False
                self._attr_is_closing = False
                self._attr_state = "open"
                self.async_write_ha_state()

                # Check API after delay
                await self._delayed_api_check()
                _LOGGER.info(
                    "Successfully started water flow with %d%% flow rate for device %s",
                    int(position),
                    self._device_id,
                )

        except Exception as err:
            _LOGGER.error(
                "Failed to set valve position for device %s: %s", self._device_id, err
            )
            raise

    async def async_set_temperature(self, temperature: float) -> None:
        """Set the water temperature."""
        try:
            await self.hass.async_add_executor_job(
                self.coordinator.api.set_specific_temperature,
                self._device_id,
                temperature,
                int(self._attr_valve_position),
            )
            self._attr_temperature = temperature
            _LOGGER.info(
                "Set temperature to %.1f°C for device %s", temperature, self._device_id
            )
        except Exception as err:
            _LOGGER.error(
                "Failed to set temperature for device %s: %s", self._device_id, err
            )

    async def async_set_preset_mode(self, preset_mode: str) -> None:
        """Set the temperature preset mode."""
        try:
            # Map preset modes to API calls
            if preset_mode == "coldest":
                await self.hass.async_add_executor_job(
                    self.coordinator.api.set_coldest,
                    self._device_id,
                    int(self._attr_valve_position),
                )
            elif preset_mode == "hottest":
                await self.hass.async_add_executor_job(
                    self.coordinator.api.set_hottest,
                    self._device_id,
                    int(self._attr_valve_position),
                )
            elif preset_mode == "warm":
                await self.hass.async_add_executor_job(
                    self.coordinator.api.set_warm,
                    self._device_id,
                    int(self._attr_valve_position),
                )

            self._attr_preset_mode = preset_mode
            _LOGGER.info(
                "Set preset mode to %s for device %s", preset_mode, self._device_id
            )
        except Exception as err:
            _LOGGER.error(
                "Failed to set preset mode for device %s: %s", self._device_id, err
            )

    @property
    def preset_modes(self) -> list[str]:
        """Return the available preset modes."""
        return ["coldest", "cold", "warm", "hot", "hottest"]

    @property
    def current_option(self) -> str:
        """Return the current preset mode."""
        return self._attr_preset_mode
