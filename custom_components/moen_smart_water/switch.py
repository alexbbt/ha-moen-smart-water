"""Switch platform for Moen Smart Water integration."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

from homeassistant.components.switch import SwitchEntity, SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import MoenDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

PARALLEL_UPDATES = 1


@dataclass(frozen=True, kw_only=True)
class MoenSwitchEntityDescription(SwitchEntityDescription):
    """Switch description bound to a shadow field."""

    shadow_field: str


SWITCHES: tuple[MoenSwitchEntityDescription, ...] = (
    MoenSwitchEntityDescription(
        key="freeze_enable",
        name="Freeze Protection",
        shadow_field="freezeEnable",
        icon="mdi:snowflake",
    ),
    MoenSwitchEntityDescription(
        key="handle_reverse",
        name="Handle Reverse",
        shadow_field="handleReverse",
        entity_category=EntityCategory.CONFIG,
        icon="mdi:rotate-left",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Moen Smart Water switch entities."""
    coordinator: MoenDataUpdateCoordinator = hass.data["moen_smart_water"][
        config_entry.entry_id
    ]

    entities: list[MoenSwitch] = []
    for device_id, device in coordinator.get_all_devices().items():
        device_name = device.get("name", f"Moen Smart Water {device_id}")
        entities.extend(
            MoenSwitch(coordinator, device_id, device_name, desc) for desc in SWITCHES
        )

    _LOGGER.info("Adding %d switch entities", len(entities))
    async_add_entities(entities)


class MoenSwitch(CoordinatorEntity, SwitchEntity):
    """A device setting read from the shadow and written via the settings API."""

    entity_description: MoenSwitchEntityDescription

    def __init__(
        self,
        coordinator: MoenDataUpdateCoordinator,
        device_id: str,
        device_name: str,
        description: MoenSwitchEntityDescription,
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator)
        self._device_id = device_id
        self.entity_description = description
        self._attr_has_entity_name = True
        self._attr_unique_id = f"{device_id}_{description.key}"
        self._attr_device_info = DeviceInfo(
            identifiers={("moen_smart_water", device_id)},
            name=device_name,
            manufacturer="Moen",
            model="Smart Faucet",
        )

    @property
    def is_on(self) -> bool | None:
        """Return the current setting value from the shadow."""
        shadow = self.coordinator.get_device_shadow(self._device_id)
        if not shadow:
            return None
        reported = shadow.get("state", {}).get("reported", {})
        value = reported.get(self.entity_description.shadow_field)
        return bool(value) if value is not None else None

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Enable the setting."""
        await self._async_write(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Disable the setting."""
        await self._async_write(False)

    async def _async_write(self, value: bool) -> None:
        settings = {self.entity_description.shadow_field: value}
        try:
            await self.hass.async_add_executor_job(
                self.coordinator.api.update_device_settings, self._device_id, settings
            )
        except Exception as err:
            raise HomeAssistantError(
                f"Failed to set {self.entity_description.name}: {err}"
            ) from err
        # Reflect the change now; realtime or the next poll confirms it.
        self.coordinator.async_ingest_shadow_update(self._device_id, settings)
