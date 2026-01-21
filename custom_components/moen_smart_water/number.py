"""Number platform for Moen Smart Water integration."""

from __future__ import annotations

import asyncio
import logging

from homeassistant.components.number import (
    NumberDeviceClass,
    NumberEntity,
    NumberEntityDescription,
    NumberMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import MoenDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

# Number descriptions
TEMPERATURE_NUMBER = NumberEntityDescription(
    key="temperature",
    name="Temperature",
    device_class=NumberDeviceClass.TEMPERATURE,
    native_min_value=0.0,
    native_max_value=100.0,
    native_step=1.0,
    native_unit_of_measurement="°C",
    icon="mdi:thermometer",
)

FLOW_RATE_NUMBER = NumberEntityDescription(
    key="default_flow_rate",
    name="Default Flow Rate",
    native_min_value=10,  # Will be updated from device trickleFlowRate
    native_max_value=100,  # Will be updated from device maxFlowRate
    native_step=1,
    native_unit_of_measurement="%",
    entity_category=EntityCategory.CONFIG,
    icon="mdi:water-percent",
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Moen Smart Water number entities."""
    coordinator: MoenDataUpdateCoordinator = hass.data["moen_smart_water"][
        config_entry.entry_id
    ]

    # Get devices and create entities for each
    devices = coordinator.get_all_devices()
    _LOGGER.info(
        "Setting up number entities. Found %d devices: %s",
        len(devices),
        list(devices.keys()),
    )

    entities = []
    for device_id, device in devices.items():
        device_name = device.get("name", f"Moen Smart Water {device_id}")
        _LOGGER.info(
            "Creating number entities for device %s: %s", device_id, device_name
        )

        entities.extend(
            [
                MoenNumber(coordinator, device_id, device_name, TEMPERATURE_NUMBER),
                MoenNumber(coordinator, device_id, device_name, FLOW_RATE_NUMBER),
            ]
        )

    _LOGGER.info("Adding %d number entities", len(entities))
    async_add_entities(entities)


class MoenNumber(CoordinatorEntity, NumberEntity):
    """Generic Moen number entity using NumberEntityDescription."""

    def __init__(
        self,
        coordinator: MoenDataUpdateCoordinator,
        device_id: str,
        device_name: str,
        description: NumberEntityDescription,
    ) -> None:
        """Initialize the number entity."""
        super().__init__(coordinator)
        self._device_id = device_id
        self._device_name = device_name
        self.entity_description = description
        self._attr_has_entity_name = True
        self._attr_unique_id = f"{device_id}_{description.key}"
        self._attr_mode = NumberMode.AUTO

        # Set initial value based on description
        if description.key == "temperature":
            self._attr_native_value = 20.0
            # Min/max will be set from device shadow data
            self._attr_native_min_value = 0.0
            self._attr_native_max_value = 100.0
        elif description.key == "default_flow_rate":
            # Default to trickle flow rate (will be updated from device shadow)
            self._attr_native_value = 10
        else:
            self._attr_native_value = 0

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
        if not shadow:
            self.async_write_ha_state()
            return

        state = shadow.get("state", {}).get("reported", {})
        key = self.entity_description.key

        if key == "temperature":
            # Update min/max from device learned temperature range
            learned_min = state.get("learnedMinTemp", 0.0)
            learned_max = state.get("learnedMaxTemp", 100.0)
            # Ensure we have valid values
            if learned_min is not None and learned_max is not None:
                # Round to whole numbers for cleaner display
                self._attr_native_min_value = round(float(learned_min))
                self._attr_native_max_value = round(float(learned_max))

            # Update temperature value from API
            # When temperatureGoal is "specific", the temperature field represents
            # the goal/setpoint the device is trying to reach
            temperature_goal = state.get("temperatureGoal")
            device_state = state.get("state", "idle")

            # If temperatureGoal is "specific" and device is idle,
            # temperature field represents the setpoint/goal
            # Otherwise, it's the actual measured temperature
            if temperature_goal == "specific" and device_state == "idle":
                api_temp = state.get("temperature")
                if api_temp is not None:
                    # Round to 1 decimal place for cleaner display
                    self._attr_native_value = round(float(api_temp), 1)
            # If device is running or goal is not specific,
            # temperature is measured temp, don't update slider
            # (keep current setpoint value)
        elif key == "default_flow_rate":
            # Get defaultFlowRate from shadow (the configured rate for gesture activation)
            # Note: flowRate only exists when water is actively running
            default_flow_rate = state.get("defaultFlowRate", 10)
            if default_flow_rate == "unknown" or default_flow_rate is None:
                # Keep current value if available, otherwise default to 10 (trickle flow rate)
                if self._attr_native_value is None:
                    self._attr_native_value = 10
            else:
                self._attr_native_value = default_flow_rate

        self.async_write_ha_state()

    async def async_set_native_value(self, value: float) -> None:
        """Set the number value."""
        key = self.entity_description.key

        try:
            if key == "temperature":
                # Get device state to determine if water is running
                shadow = self.coordinator.get_device_shadow(self._device_id)
                if not shadow:
                    device_state = "idle"
                    current_flow_rate = 100
                else:
                    reported = shadow.get("state", {}).get("reported", {})
                    desired = shadow.get("state", {}).get("desired", {})
                    device_state = reported.get("state", "idle")

                    # Determine current flow rate (only needed if device is running)
                    # 1. Check desired state for active flowRate (what was last commanded)
                    # 2. Otherwise, use defaultFlowRate from reported state (configured default)
                    # 3. Fall back to 100 if neither is available
                    active_flow_rate = desired.get("flowRate")
                    if active_flow_rate is not None and active_flow_rate != "unknown":
                        # Use the active flow rate from desired state (last command sent)
                        current_flow_rate = int(active_flow_rate)
                    else:
                        # Fall back to default flow rate from reported state
                        default_flow_rate = reported.get("defaultFlowRate")
                        if default_flow_rate is not None:
                            current_flow_rate = int(default_flow_rate)
                        else:
                            current_flow_rate = 100

                # Get current min/max values
                min_temp = self._attr_native_min_value
                max_temp = self._attr_native_max_value

                # Determine temperature setting to use
                # Check if value is at min (coldest) or max (hottest)
                # Use a small tolerance (0.1°C) to account for floating point precision
                if abs(value - min_temp) < 0.1:
                    temp_setting = "coldest"
                    temp_value = min_temp
                elif abs(value - max_temp) < 0.1:
                    temp_setting = "hottest"
                    temp_value = max_temp
                else:
                    temp_setting = value  # Specific temperature
                    temp_value = value

                # If device is running, update temperature and maintain water flow
                # If device is idle, just update the temperature setting for next time
                if device_state == "running":
                    _LOGGER.debug(
                        "Temperature change while running: applying immediately with flow rate %d%%",
                        current_flow_rate,
                    )
                    # Device is running - update temperature and keep water flowing
                    if temp_setting == "coldest":
                        await self.hass.async_add_executor_job(
                            self.coordinator.api.set_coldest,
                            self._device_id,
                            current_flow_rate,
                        )
                    elif temp_setting == "hottest":
                        await self.hass.async_add_executor_job(
                            self.coordinator.api.set_hottest,
                            self._device_id,
                            current_flow_rate,
                        )
                    else:
                        await self.hass.async_add_executor_job(
                            self.coordinator.api.set_specific_temperature,
                            self._device_id,
                            temp_setting,
                            current_flow_rate,
                        )
                    _LOGGER.info(
                        "Updated temperature to %s (%.1f°C) while running at %d%% for device %s",
                        temp_setting,
                        temp_value,
                        current_flow_rate,
                        self._device_id,
                    )
                else:
                    _LOGGER.debug(
                        "Temperature change while idle: setting for next water flow"
                    )
                    # Device is idle - just update the temperature setting without starting water
                    # Use update_device_settings to set temperature without "command": "run"
                    await self.hass.async_add_executor_job(
                        self.coordinator.api.update_device_settings,
                        self._device_id,
                        {"temperature": temp_setting},
                    )
                    _LOGGER.info(
                        "Set temperature to %s (%.1f°C) for next water flow for device %s",
                        temp_setting,
                        temp_value,
                        self._device_id,
                    )

                self._attr_native_value = temp_value

                # Write state immediately for responsive UI
                self.async_write_ha_state()

                # Request coordinator refresh to update other entities (like valve)
                # But we'll preserve our set value in the coordinator update handler
                # Wait a moment for API to process the change, then refresh
                await asyncio.sleep(1)  # Give API a moment to update
                await self.coordinator.async_request_refresh()

            elif key == "default_flow_rate":
                await self.hass.async_add_executor_job(
                    self.coordinator.api.set_default_flow_rate,
                    self._device_id,
                    int(value),
                )
                self._attr_native_value = int(value)
                _LOGGER.info(
                    "Set default flow rate (for gesture activation) to %d%% for device %s",
                    int(value),
                    self._device_id,
                )

                # Write state immediately for responsive UI
                self.async_write_ha_state()

                # Request coordinator refresh to update from API
                # Wait a moment for API to process the change, then refresh
                await asyncio.sleep(1)  # Give API a moment to update
                await self.coordinator.async_request_refresh()

        except Exception as err:
            _LOGGER.error(
                "Failed to set %s for device %s: %s",
                key,
                self._device_id,
                err,
            )
