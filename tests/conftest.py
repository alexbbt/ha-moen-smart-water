"""Pytest configuration and fixtures for Moen Smart Water integration tests."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from custom_components.moen_smart_water.api import MoenAPI
from custom_components.moen_smart_water.coordinator import MoenDataUpdateCoordinator


@pytest.fixture
def hass() -> MagicMock:
    """Return a mock Home Assistant instance for testing."""
    hass_instance = MagicMock(spec=HomeAssistant)
    hass_instance.data = {}
    hass_instance.async_add_executor_job = AsyncMock(
        side_effect=lambda func, *args: func(*args)
    )
    hass_instance.config_entries = MagicMock()
    hass_instance.config_entries.async_forward_entry_setups = AsyncMock()
    hass_instance.config_entries.async_unload_platforms = AsyncMock(return_value=True)
    hass_instance.config_entries.async_update_entry = MagicMock()
    hass_instance.services = MagicMock()
    hass_instance.services.has_service = MagicMock(return_value=False)
    hass_instance.services.async_register = MagicMock()
    hass_instance.services.async_call = AsyncMock()
    return hass_instance


@pytest.fixture
def config_entry() -> ConfigEntry:
    """Return a mock config entry for testing."""
    entry = MagicMock(spec=ConfigEntry)
    entry.entry_id = "test_entry_id"
    entry.data = {
        "username": "test@example.com",
        "password": "test_password",
        "tokens": {
            "access_token": "test_access",
            "refresh_token": "test_refresh",
            "id_token": "test_id",
            "expires_in": 3600,
        },
    }
    return entry


@pytest.fixture
def mock_api() -> MagicMock:
    """Return a mock MoenAPI instance for testing."""
    api = MagicMock(spec=MoenAPI)
    api.access_token = "test_access"
    api.refresh_token = "test_refresh"
    api.id_token = "test_id"
    api.token_expiry = 9999999999
    api.login = MagicMock()
    api.get_user_profile = MagicMock(
        return_value={"email": "test@example.com", "userId": "12345"}
    )
    api.get_cached_devices = MagicMock(
        return_value=[
            {"clientId": "device1", "name": "Kitchen Faucet"},
            {"clientId": "device2", "name": "Bathroom Faucet"},
        ]
    )
    api.get_device_shadow = MagicMock(
        return_value={
            "state": {
                "desired": {"temperature": 25.0, "flow_rate": 100},
                "reported": {
                    "temperature": 25.0,
                    "flow_rate": 100,
                    "water_flowing": False,
                },
            }
        }
    )
    api.start_water_flow = MagicMock(return_value={"success": True})
    api.stop_water_flow = MagicMock(return_value={"success": True})
    api.set_specific_temperature = MagicMock(return_value={"success": True})
    api.set_default_flow_rate = MagicMock(return_value={"success": True})
    api.get_tokens = MagicMock(
        return_value={
            "access_token": "test_access",
            "refresh_token": "test_refresh",
            "id_token": "test_id",
            "expires_in": 3600,
        }
    )
    return api


@pytest.fixture
def coordinator(
    hass: MagicMock, config_entry: ConfigEntry, mock_api: MagicMock
) -> MagicMock:
    """Return a mock MoenDataUpdateCoordinator instance for testing."""
    coordinator_instance = MagicMock(spec=MoenDataUpdateCoordinator)
    coordinator_instance.api = mock_api
    coordinator_instance.entry = config_entry
    coordinator_instance.hass = hass
    coordinator_instance._devices = {
        "device1": {"clientId": "device1", "name": "Kitchen Faucet"},
        "device2": {"clientId": "device2", "name": "Bathroom Faucet"},
    }
    coordinator_instance._device_shadows = {
        "device1": {
            "state": {
                "reported": {"temperature": 25.0, "flow_rate": 100},
            }
        },
        "device2": {
            "state": {
                "reported": {"temperature": 30.0, "flow_rate": 80},
            }
        },
    }
    coordinator_instance.get_device = MagicMock(
        side_effect=lambda device_id: coordinator_instance._devices.get(device_id)
    )
    coordinator_instance.get_device_shadow = MagicMock(
        side_effect=lambda device_id: coordinator_instance._device_shadows.get(
            device_id
        )
    )
    coordinator_instance.get_all_devices = MagicMock(
        return_value=coordinator_instance._devices
    )
    coordinator_instance.get_all_device_shadows = MagicMock(
        return_value=coordinator_instance._device_shadows
    )
    coordinator_instance.async_config_entry_first_refresh = AsyncMock()
    coordinator_instance._async_update_data = AsyncMock(
        return_value={
            "devices": coordinator_instance._devices,
            "device_shadows": coordinator_instance._device_shadows,
            "device_details": {},
        }
    )
    return coordinator_instance


@pytest.fixture
def sample_device_data() -> dict[str, Any]:
    """Return sample device data for testing."""
    return {
        "clientId": "test_device_123",
        "name": "Test Faucet",
        "model": "Moen Smart Faucet",
        "status": "online",
    }


@pytest.fixture
def sample_device_shadow() -> dict[str, Any]:
    """Return sample device shadow for testing."""
    return {
        "state": {
            "desired": {
                "temperature": 25.0,
                "flow_rate": 50,
                "water_flowing": False,
            },
            "reported": {
                "temperature": 25.0,
                "flow_rate": 50,
                "water_flowing": False,
                "battery_percentage": 85,
                "rssi": -45,
            },
        }
    }


@pytest.fixture
def sample_user_profile() -> dict[str, Any]:
    """Return sample user profile for testing."""
    return {
        "email": "test@example.com",
        "userId": "user123",
        "firstName": "Test",
        "lastName": "User",
    }
