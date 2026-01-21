"""Data update coordinator for Moen Smart Water integration."""

from __future__ import annotations

import asyncio
import logging
from datetime import timedelta
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import MoenAPI

_LOGGER = logging.getLogger(__name__)

# Polling interval - update every 30 seconds
SCAN_INTERVAL = timedelta(seconds=30)


class MoenDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Class to manage fetching data from the Moen API."""

    def __init__(self, hass: HomeAssistant, api: MoenAPI, entry: ConfigEntry) -> None:
        """Initialize the coordinator."""
        self.api = api
        self.entry = entry
        self._devices: dict[str, dict[str, Any]] = {}
        self._device_shadows: dict[str, dict[str, Any]] = {}
        self._device_details: dict[str, dict[str, Any]] = {}
        self._device_usage: dict[str, dict[str, Any]] = {}

        super().__init__(
            hass,
            _LOGGER,
            name="moen_smart_water",
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self) -> dict[str, Any]:
        """Update data via library."""
        try:
            _LOGGER.debug("Starting coordinator data update")

            # Get fresh device list
            devices = await self.hass.async_add_executor_job(
                self.api.get_cached_devices
            )
            _LOGGER.debug("Coordinator received %d devices", len(devices))

            # Update device cache
            self._devices = {
                device.get("clientId", device.get("id", "")): device
                for device in devices
            }

            # Get device shadows for all devices (operational data) in parallel
            async def fetch_shadow(device_id: str) -> tuple[str, dict[str, Any]]:
                """Fetch a single device shadow."""
                try:
                    _LOGGER.debug("Fetching shadow for device %s", device_id)
                    shadow = await self.hass.async_add_executor_job(
                        self.api.get_device_shadow, device_id
                    )
                    _LOGGER.debug(
                        "Successfully fetched shadow for device %s", device_id
                    )
                    return device_id, shadow
                except Exception as err:
                    _LOGGER.warning(
                        "Failed to get shadow for device %s: %s", device_id, err
                    )
                    # Return empty shadow if we can't get it
                    return device_id, {}

            # Fetch all shadows in parallel
            _LOGGER.debug("Fetching shadows for %d devices", len(self._devices))
            shadow_results = await asyncio.gather(
                *[fetch_shadow(device_id) for device_id in self._devices.keys()],
                return_exceptions=False,
            )
            device_shadows = dict(shadow_results)
            _LOGGER.debug("Fetched %d device shadows", len(device_shadows))

            # All diagnostic data is now available in device shadows
            self._device_shadows = device_shadows

            # Get daily usage data for all devices (for cumulative water usage)
            async def fetch_usage(device_id: str) -> tuple[str, dict[str, Any]]:
                """Fetch daily usage data for a device."""
                try:
                    _LOGGER.debug("Fetching daily usage for device %s", device_id)
                    usage = await self.hass.async_add_executor_job(
                        self.api.get_daily_usage, device_id
                    )
                    _LOGGER.debug(
                        "Successfully fetched daily usage for device %s", device_id
                    )
                    return device_id, usage
                except Exception as err:
                    _LOGGER.warning(
                        "Failed to get daily usage for device %s: %s", device_id, err
                    )
                    # Return empty usage if we can't get it
                    return device_id, {}

            # Fetch all usage data in parallel
            _LOGGER.debug("Fetching usage for %d devices", len(self._devices))
            usage_results = await asyncio.gather(
                *[fetch_usage(device_id) for device_id in self._devices.keys()],
                return_exceptions=False,
            )
            device_usage = dict(usage_results)
            _LOGGER.debug("Fetched %d device usage records", len(device_usage))

            self._device_usage = device_usage

            # Store updated tokens if they were refreshed
            from . import _store_tokens

            await _store_tokens(self.hass, self.entry, self.api.get_tokens())

            return {
                "devices": self._devices,
                "device_shadows": self._device_shadows,
                "device_details": self._device_details,
                "device_usage": self._device_usage,
            }

        except Exception as err:
            _LOGGER.error("Error communicating with Moen API: %s", err)
            raise UpdateFailed(f"Error communicating with Moen API: {err}") from err

    def get_device(self, device_id: str) -> dict[str, Any] | None:
        """Get device data by ID."""
        return self._devices.get(device_id)

    def get_device_shadow(self, device_id: str) -> dict[str, Any] | None:
        """Get device shadow data by ID."""
        return self._device_shadows.get(device_id)

    def get_all_devices(self) -> dict[str, dict[str, Any]]:
        """Get all devices."""
        return self._devices

    def get_all_device_shadows(self) -> dict[str, dict[str, Any]]:
        """Get all device shadows."""
        return self._device_shadows

    def get_device_usage(self, device_id: str) -> dict[str, Any] | None:
        """Get device usage data by ID."""
        return self._device_usage.get(device_id)
