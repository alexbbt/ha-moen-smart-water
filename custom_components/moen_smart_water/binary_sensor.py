"""Binary sensor platform for Moen Smart Water integration."""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import MoenDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

PARALLEL_UPDATES = 0


@dataclass(frozen=True, kw_only=True)
class MoenBinarySensorEntityDescription(BinarySensorEntityDescription):
    """Binary sensor description that reads the reported shadow state."""

    value_fn: Callable[[dict[str, Any]], bool]


BINARY_SENSORS: tuple[MoenBinarySensorEntityDescription, ...] = (
    MoenBinarySensorEntityDescription(
        key="running",
        name="Running",
        value_fn=lambda s: s.get("state") == "running",
        device_class=BinarySensorDeviceClass.RUNNING,
        icon="mdi:faucet",
    ),
    MoenBinarySensorEntityDescription(
        key="is_freezing",
        name="Freeze Risk",
        value_fn=lambda s: bool(s.get("isFreezing")),
        device_class=BinarySensorDeviceClass.COLD,
        icon="mdi:snowflake-alert",
    ),
    MoenBinarySensorEntityDescription(
        key="active_alert",
        name="Active Alert",
        value_fn=lambda s: bool(s.get("alerts")),
        device_class=BinarySensorDeviceClass.PROBLEM,
        icon="mdi:alert",
    ),
    MoenBinarySensorEntityDescription(
        key="sensor_comm_error",
        name="Sensor Comm Error",
        value_fn=lambda s: bool(s.get("sensorCommError")),
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    MoenBinarySensorEntityDescription(
        key="handle_comm_error",
        name="Handle Comm Error",
        value_fn=lambda s: bool(s.get("handleCommError")),
        device_class=BinarySensorDeviceClass.PROBLEM,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    # Safety features are read-only on purpose so automations can't weaken them.
    MoenBinarySensorEntityDescription(
        key="safety_mode",
        name="Scald Protection",
        value_fn=lambda s: bool(s.get("safetyModeEnabled")),
        icon="mdi:shield-check",
    ),
    MoenBinarySensorEntityDescription(
        key="child_mode",
        name="Child Lock",
        value_fn=lambda s: bool(s.get("childModeEnabled")),
        icon="mdi:account-lock",
    ),
)

CONNECTIVITY_SENSOR = BinarySensorEntityDescription(
    key="connectivity",
    name="Connectivity",
    device_class=BinarySensorDeviceClass.CONNECTIVITY,
    entity_category=EntityCategory.DIAGNOSTIC,
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Moen Smart Water binary sensor entities."""
    coordinator: MoenDataUpdateCoordinator = hass.data["moen_smart_water"][
        config_entry.entry_id
    ]

    entities: list[BinarySensorEntity] = []
    for device_id, device in coordinator.get_all_devices().items():
        device_name = device.get("name", f"Moen Smart Water {device_id}")
        entities.extend(
            MoenBinarySensor(coordinator, device_id, device_name, desc)
            for desc in BINARY_SENSORS
        )
        entities.append(
            MoenConnectivitySensor(
                coordinator, device_id, device_name, CONNECTIVITY_SENSOR
            )
        )

    _LOGGER.info("Adding %d binary sensor entities", len(entities))
    async_add_entities(entities)


class MoenBinarySensorBase(CoordinatorEntity, BinarySensorEntity):
    """Common setup for Moen binary sensors."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: MoenDataUpdateCoordinator,
        device_id: str,
        device_name: str,
        description: BinarySensorEntityDescription,
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._device_id = device_id
        self.entity_description = description
        self._attr_unique_id = f"{device_id}_{description.key}"
        self._attr_device_info = DeviceInfo(
            identifiers={("moen_smart_water", device_id)},
            name=device_name,
            manufacturer="Moen",
            model="Smart Faucet",
        )


class MoenBinarySensor(MoenBinarySensorBase):
    """Binary sensor backed by a field of the device shadow."""

    entity_description: MoenBinarySensorEntityDescription

    @property
    def is_on(self) -> bool | None:
        """Return the state from the reported shadow."""
        shadow = self.coordinator.get_device_shadow(self._device_id)
        if not shadow:
            return None
        return self.entity_description.value_fn(
            shadow.get("state", {}).get("reported", {})
        )


class MoenConnectivitySensor(MoenBinarySensorBase):
    """On while Home Assistant can reach the Moen cloud (realtime or polling)."""

    @property
    def available(self) -> bool:
        """Stay available so a failed poll reads as disconnected."""
        return True

    @property
    def is_on(self) -> bool:
        """Return whether the realtime link is up or the last poll succeeded."""
        return (
            self.coordinator.realtime_connected or self.coordinator.last_update_success
        )
