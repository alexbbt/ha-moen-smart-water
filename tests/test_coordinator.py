"""Tests for Moen Smart Water coordinator."""

from __future__ import annotations

from unittest.mock import MagicMock

from homeassistant.config_entries import ConfigEntry

from custom_components.moen_smart_water.coordinator import (
    SCAN_INTERVAL,
    MoenDataUpdateCoordinator,
)


class TestMoenDataUpdateCoordinator:
    """Test MoenDataUpdateCoordinator class."""

    def test_coordinator_initialization(
        self,
        hass: MagicMock,
        mock_api: MagicMock,
        config_entry: ConfigEntry,
    ) -> None:
        """Test coordinator initialization."""
        coordinator = MoenDataUpdateCoordinator(hass, mock_api, config_entry)

        assert coordinator.api == mock_api
        assert coordinator.entry == config_entry
        assert coordinator._devices == {}
        assert coordinator._device_shadows == {}
        assert coordinator._device_details == {}
        assert coordinator.name == "moen_smart_water"
        assert coordinator.update_interval == SCAN_INTERVAL

    def test_get_device_returns_none_for_unknown(
        self,
        hass: MagicMock,
        mock_api: MagicMock,
        config_entry: ConfigEntry,
    ) -> None:
        """Test getting non-existent device returns None."""
        coordinator = MoenDataUpdateCoordinator(hass, mock_api, config_entry)

        device = coordinator.get_device("nonexistent")

        assert device is None

    def test_get_device_shadow_returns_none_for_unknown(
        self,
        hass: MagicMock,
        mock_api: MagicMock,
        config_entry: ConfigEntry,
    ) -> None:
        """Test getting non-existent device shadow returns None."""
        coordinator = MoenDataUpdateCoordinator(hass, mock_api, config_entry)

        shadow = coordinator.get_device_shadow("nonexistent")

        assert shadow is None

    def test_get_all_devices(
        self,
        hass: MagicMock,
        mock_api: MagicMock,
        config_entry: ConfigEntry,
    ) -> None:
        """Test getting all devices."""
        coordinator = MoenDataUpdateCoordinator(hass, mock_api, config_entry)
        coordinator._devices = {
            "device1": {"name": "Faucet 1"},
            "device2": {"name": "Faucet 2"},
        }

        devices = coordinator.get_all_devices()

        assert len(devices) == 2
        assert "device1" in devices
        assert "device2" in devices

    def test_get_all_device_shadows(
        self,
        hass: MagicMock,
        mock_api: MagicMock,
        config_entry: ConfigEntry,
    ) -> None:
        """Test getting all device shadows."""
        coordinator = MoenDataUpdateCoordinator(hass, mock_api, config_entry)
        coordinator._device_shadows = {
            "device1": {"state": {}},
            "device2": {"state": {}},
        }

        shadows = coordinator.get_all_device_shadows()

        assert len(shadows) == 2
        assert "device1" in shadows
        assert "device2" in shadows
