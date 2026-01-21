"""Select platform for Moen Smart Water integration."""

from __future__ import annotations

import logging

from homeassistant.components.select import SelectEntity, SelectEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import MoenDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

# Select descriptions
DEFAULT_TEMPERATURE_SELECT = SelectEntityDescription(
    key="default_temperature",
    name="Default Temperature",
    options=["Handle Position", "Coldest", "Equal Mix"],
    entity_category=EntityCategory.CONFIG,
    icon="mdi:gesture-tap",
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Moen Smart Water select entities."""
    coordinator: MoenDataUpdateCoordinator = hass.data["moen_smart_water"][
        config_entry.entry_id
    ]

    # Get devices and create entities for each
    devices = coordinator.get_all_devices()

    entities = []
    for device_id, device in devices.items():
        device_name = device.get("name", f"Moen Smart Water {device_id}")
        entities.append(
            MoenSelect(coordinator, device_id, device_name, DEFAULT_TEMPERATURE_SELECT)
        )

    async_add_entities(entities)


class MoenSelect(CoordinatorEntity, SelectEntity):
    """Generic Moen select entity using SelectEntityDescription."""

    def __init__(
        self,
        coordinator: MoenDataUpdateCoordinator,
        device_id: str,
        device_name: str,
        description: SelectEntityDescription,
    ) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._device_id = device_id
        self._device_name = device_name
        self.entity_description = description
        self._attr_has_entity_name = True
        self._attr_unique_id = f"{device_id}_{description.key}"

        # Device information
        self._attr_device_info = DeviceInfo(
            identifiers={("moen_smart_water", device_id)},
            name=device_name,
            manufacturer="Moen",
            model="Smart Faucet",
        )

        # Set initial option
        self._attr_current_option = (
            description.options[0] if description.options else ""
        )

    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        shadow = self.coordinator.get_device_shadow(self._device_id)
        if not shadow:
            self.async_write_ha_state()
            return

        state = shadow.get("state", {}).get("reported", {})
        key = self.entity_description.key

        if key == "default_temperature":
            # Get default temperature mode for gesture activation
            default_temp = state.get("defaultTemp", "handle")
            # Map API values to display-friendly option names
            if default_temp == "handle":
                self._attr_current_option = "Handle Position"
            elif default_temp == "coldest":
                self._attr_current_option = "Coldest"
            elif default_temp in ["equal", "mix"]:
                self._attr_current_option = "Equal Mix"
            else:
                # Default to Handle Position if unknown value
                self._attr_current_option = "Handle Position"

        self.async_write_ha_state()

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        key = self.entity_description.key

        try:
            if key == "default_temperature":
                # Set default temperature mode for gesture activation
                # Map display-friendly option names to API values
                if option == "Handle Position":
                    api_value = "handle"
                elif option == "Coldest":
                    api_value = "coldest"
                elif option == "Equal Mix":
                    api_value = "equal"
                else:
                    # Fallback to handle if unknown option
                    api_value = "handle"
                    _LOGGER.warning(
                        "Unknown default temperature option '%s', using 'handle'",
                        option,
                    )

                await self.hass.async_add_executor_job(
                    self.coordinator.api.set_default_temperature,
                    self._device_id,
                    api_value,
                )
                _LOGGER.info(
                    "Set default temperature (for gesture activation) to %s for device %s",
                    option,
                    self._device_id,
                )

            self._attr_current_option = option
            _LOGGER.info("Set %s to %s for device %s", key, option, self._device_id)
        except Exception as err:
            _LOGGER.error(
                "Failed to set %s for device %s: %s",
                key,
                self._device_id,
                err,
            )
