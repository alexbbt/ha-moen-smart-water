"""Number platform for Moen Smart Water integration."""

from __future__ import annotations

import logging

from homeassistant.components.number import (
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
    native_min_value=0.0,
    native_max_value=100.0,
    native_step=1.0,
    native_unit_of_measurement="°C",
    icon="mdi:thermometer",
)

FLOW_RATE_NUMBER = NumberEntityDescription(
    key="flow_rate",
    name="Default Flow Rate",
    native_min_value=0,
    native_max_value=100,
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
            # Update current temperature value
            self._attr_native_value = state.get("temperature", 20.0)
            # Update min/max from device setpoints
            setpoint_cold = state.get("setpointColdTemp", 0.0)
            setpoint_hot = state.get("setpointHotTemp", 100.0)
            # Ensure we have valid values
            if setpoint_cold is not None and setpoint_hot is not None:
                self._attr_native_min_value = float(setpoint_cold)
                self._attr_native_max_value = float(setpoint_hot)
        elif key == "flow_rate":
            # Handle "unknown" values by keeping current value or defaulting to 0
            flow_rate = state.get("flowRate", 0)
            if flow_rate == "unknown" or flow_rate is None:
                # Keep current value if available, otherwise default to 0
                if self._attr_native_value is None:
                    self._attr_native_value = 0
            else:
                self._attr_native_value = flow_rate

        self.async_write_ha_state()

    async def async_set_native_value(self, value: float) -> None:
        """Set the number value."""
        key = self.entity_description.key

        try:
            if key == "temperature":
                # Get current min/max values
                min_temp = self._attr_native_min_value
                max_temp = self._attr_native_max_value

                # Check if value is at min (coldest) or max (hottest)
                # Use a small tolerance (0.1°C) to account for floating point precision
                if abs(value - min_temp) < 0.1:
                    # Set to coldest
                    await self.hass.async_add_executor_job(
                        self.coordinator.api.set_coldest,
                        self._device_id,
                        100,  # Full flow rate
                    )
                    self._attr_native_value = min_temp
                    _LOGGER.info(
                        "Set temperature to coldest (%.1f°C) for device %s",
                        min_temp,
                        self._device_id,
                    )
                elif abs(value - max_temp) < 0.1:
                    # Set to hottest
                    await self.hass.async_add_executor_job(
                        self.coordinator.api.set_hottest,
                        self._device_id,
                        100,  # Full flow rate
                    )
                    self._attr_native_value = max_temp
                    _LOGGER.info(
                        "Set temperature to hottest (%.1f°C) for device %s",
                        max_temp,
                        self._device_id,
                    )
                else:
                    # Set specific temperature
                    await self.hass.async_add_executor_job(
                        self.coordinator.api.set_specific_temperature,
                        self._device_id,
                        value,
                    )
                    self._attr_native_value = value
                    _LOGGER.info(
                        "Set temperature to %.1f°C for device %s",
                        value,
                        self._device_id,
                    )

            elif key == "flow_rate":
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

        except Exception as err:
            _LOGGER.error(
                "Failed to set %s for device %s: %s",
                key,
                self._device_id,
                err,
            )
