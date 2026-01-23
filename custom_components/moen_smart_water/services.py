"""Actions for Moen Smart Water integration."""

from __future__ import annotations

import logging

import voluptuous as vol
from homeassistant.core import HomeAssistant, ServiceCall, ServiceResponse
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import device_registry as dr

from .coordinator import MoenDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

DOMAIN = "moen_smart_water"


def get_moen_device_id(hass: HomeAssistant, ha_device_id: str) -> str | None:
    """Convert Home Assistant device ID to Moen device ID."""
    device_registry = dr.async_get(hass)
    device = device_registry.async_get(ha_device_id)

    if not device:
        return None

    # Look for the Moen device identifier
    for identifier in device.identifiers:
        if identifier[0] == DOMAIN:
            return identifier[1]

    return None


# Service schemas
START_WATER_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("device_id"): cv.string,
        vol.Optional("temperature", default="coldest"): vol.Any(
            cv.string, vol.All(float, vol.Range(min=0, max=100))
        ),
        vol.Optional("flow_rate", default=100): vol.All(int, vol.Range(min=0, max=100)),
    }
)

DISPENSE_VOLUME_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("device_id"): cv.string,
        vol.Required("volume_ml"): vol.All(int, vol.Range(min=50, max=2000)),
        vol.Optional("temperature"): vol.Any(
            cv.string, vol.All(float, vol.Range(min=0, max=100))
        ),
        vol.Optional("timeout"): vol.All(int, vol.Range(min=10, max=300)),
    }
)

STOP_WATER_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("device_id"): cv.string,
    }
)

GET_STATUS_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("device_id"): cv.string,
    }
)

GET_USER_PROFILE_SERVICE_SCHEMA = vol.Schema({})

SET_TEMPERATURE_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("device_id"): cv.string,
        vol.Required("temperature"): vol.All(float, vol.Range(min=0, max=100)),
        vol.Optional("flow_rate", default=100): vol.All(int, vol.Range(min=0, max=100)),
    }
)

SET_DEFAULT_FLOW_RATE_SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("device_id"): cv.string,
        vol.Required("default_flow_rate"): vol.All(int, vol.Range(min=0, max=100)),
    }
)


async def async_setup_services(hass: HomeAssistant) -> None:
    """Set up the actions for Moen Smart Water integration."""
    _LOGGER.info("Setting up Moen Smart Water actions")

    async def start_water(call: ServiceCall) -> ServiceResponse:
        """Action to start water flow with specified temperature and flow rate."""
        ha_device_id = call.data["device_id"]
        temperature = call.data["temperature"]
        flow_rate = call.data["flow_rate"]

        # Convert HA device ID to Moen device ID
        device_id = get_moen_device_id(hass, ha_device_id)
        if not device_id:
            # If conversion failed, try using it as-is (for backward compatibility)
            device_id = ha_device_id

        # Find the coordinator for this device
        coordinator = None
        for _entry_id, entry_coordinator in hass.data.get(
            "moen_smart_water", {}
        ).items():
            if isinstance(entry_coordinator, MoenDataUpdateCoordinator):
                devices = entry_coordinator.get_all_devices()
                if device_id in devices:
                    coordinator = entry_coordinator
                    break

        if not coordinator:
            error_msg = f"Device {device_id} not found in any configured Moen Smart Water integration"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
            }

        try:
            await hass.async_add_executor_job(
                coordinator.api.start_water_flow, device_id, temperature, flow_rate
            )
            _LOGGER.info(
                "Started water flow on device %s (temp: %s, flow: %d%%)",
                device_id,
                temperature,
                flow_rate,
            )

            # Get current device shadow to return state
            shadow = coordinator.get_device_shadow(device_id)

            return {
                "success": True,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
                "temperature": temperature,
                "flow_rate": flow_rate,
                "message": f"Started water flow on device {device_id}",
                "current_state": shadow.get("reported", {}).get("valveState", "unknown")
                if shadow
                else "unknown",
            }
        except Exception as err:
            error_msg = f"Failed to start water flow on device {device_id}: {err}"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
            }

    async def dispense_volume(call: ServiceCall) -> ServiceResponse:
        """Action to dispense a specific volume of water from the faucet."""
        ha_device_id = call.data["device_id"]
        volume_ml = call.data.get("volume_ml")  # Now optional
        temperature = call.data.get("temperature")  # Optional
        # Flow rate is always 100% for volume dispensing - faucet controls it automatically
        flow_rate = 100
        timeout = call.data.get("timeout", 120)  # Default to 120s if not provided

        # Convert HA device ID to Moen device ID
        device_id = get_moen_device_id(hass, ha_device_id)
        if not device_id:
            # If conversion failed, try using it as-is (for backward compatibility)
            device_id = ha_device_id

        # Find the coordinator for this device
        coordinator = None
        for _entry_id, entry_coordinator in hass.data.get(
            "moen_smart_water", {}
        ).items():
            if isinstance(entry_coordinator, MoenDataUpdateCoordinator):
                devices = entry_coordinator.get_all_devices()
                if device_id in devices:
                    coordinator = entry_coordinator
                    break

        if not coordinator:
            error_msg = f"Device {device_id} not found in any configured Moen Smart Water integration"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
            }

        try:
            await hass.async_add_executor_job(
                coordinator.api.dispense_water,
                device_id,
                volume_ml,
                temperature,
                flow_rate,
                timeout,
            )

            # Build log message with optional parameters
            log_parts = []
            if volume_ml is not None:
                log_parts.append(f"{volume_ml}ml")
            if temperature is not None:
                log_parts.append(f"temp: {temperature}")
            log_parts.append(f"flow: {flow_rate}%")  # Always 100% for volume dispensing
            log_msg = ", ".join(log_parts) if log_parts else "no limits"

            _LOGGER.info(
                "Set up dispense on device %s (%s)",
                device_id,
                log_msg,
            )

            # Get current device shadow to return state
            shadow = coordinator.get_device_shadow(device_id)

            # Build response message
            msg_parts = []
            if volume_ml is not None:
                msg_parts.append(f"{volume_ml}ml")
            if temperature is not None:
                msg_parts.append(f"temp {temperature}")
            msg_parts.append(f"flow {flow_rate}%")  # Always 100% for volume dispensing
            message = f"Dispense configured ({', '.join(msg_parts) if msg_parts else 'no limits'}) - wave hand to start"

            response = {
                "success": True,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
                "message": message,
                "current_state": shadow.get("reported", {}).get("valveState", "unknown")
                if shadow
                else "unknown",
            }

            # Add optional parameters to response if they were provided
            if volume_ml is not None:
                response["volume_ml"] = volume_ml
            if temperature is not None:
                response["temperature"] = temperature
            response["flow_rate"] = flow_rate  # Always 100% for volume dispensing
            response["timeout"] = timeout

            return response
        except Exception as err:
            error_msg = f"Failed to dispense water from device {device_id}: {err}"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
            }

    async def stop_water(call: ServiceCall) -> ServiceResponse:
        """Action to stop water flow from the faucet."""
        ha_device_id = call.data["device_id"]

        # Convert HA device ID to Moen device ID
        device_id = get_moen_device_id(hass, ha_device_id)
        if not device_id:
            # If conversion failed, try using it as-is (for backward compatibility)
            device_id = ha_device_id

        # Find the coordinator for this device
        coordinator = None
        for _entry_id, entry_coordinator in hass.data.get(
            "moen_smart_water", {}
        ).items():
            if isinstance(entry_coordinator, MoenDataUpdateCoordinator):
                devices = entry_coordinator.get_all_devices()
                if device_id in devices:
                    coordinator = entry_coordinator
                    break

        if not coordinator:
            error_msg = f"Device {device_id} not found in any configured Moen Smart Water integration"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
            }

        try:
            await hass.async_add_executor_job(
                coordinator.api.stop_water_flow, device_id
            )
            _LOGGER.info("Stopped water flow on device %s", device_id)

            # Get current device shadow to return state
            shadow = coordinator.get_device_shadow(device_id)

            return {
                "success": True,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
                "message": f"Stopped water flow on device {device_id}",
                "current_state": shadow.get("reported", {}).get("valveState", "unknown")
                if shadow
                else "unknown",
            }
        except Exception as err:
            error_msg = f"Failed to stop water flow on device {device_id}: {err}"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
            }

    async def get_device_status(call: ServiceCall) -> ServiceResponse:
        """Action to get device status."""
        ha_device_id = call.data["device_id"]

        # Convert HA device ID to Moen device ID
        device_id = get_moen_device_id(hass, ha_device_id)
        if not device_id:
            # If conversion failed, try using it as-is (for backward compatibility)
            device_id = ha_device_id

        # Find the coordinator for this device
        coordinator = None
        for _entry_id, entry_coordinator in hass.data.get(
            "moen_smart_water", {}
        ).items():
            if isinstance(entry_coordinator, MoenDataUpdateCoordinator):
                devices = entry_coordinator.get_all_devices()
                if device_id in devices:
                    coordinator = entry_coordinator
                    break

        if not coordinator:
            error_msg = f"Device {device_id} not found in any configured Moen Smart Water integration"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
            }

        try:
            shadow = coordinator.get_device_shadow(device_id)
            _LOGGER.info("Device %s shadow: %s", device_id, shadow)

            return {
                "success": True,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
                "shadow": shadow,
                "message": f"Retrieved status for device {device_id}",
            }
        except Exception as err:
            error_msg = f"Failed to get status for device {device_id}: {err}"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
            }

    async def get_user_profile(call: ServiceCall) -> ServiceResponse:
        """Action to get user profile."""
        # Find any coordinator (they all have the same user profile)
        coordinator = None
        for _entry_id, entry_coordinator in hass.data.get(
            "moen_smart_water", {}
        ).items():
            if isinstance(entry_coordinator, MoenDataUpdateCoordinator):
                coordinator = entry_coordinator
                break

        if not coordinator:
            error_msg = "No Moen Smart Water integration found"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
            }

        try:
            profile = await hass.async_add_executor_job(
                coordinator.api.get_user_profile
            )
            _LOGGER.info("User profile: %s", profile)

            return {
                "success": True,
                "profile": profile,
                "message": "Retrieved user profile",
            }
        except Exception as err:
            error_msg = f"Failed to get user profile: {err}"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
            }

    async def set_temperature(call: ServiceCall) -> ServiceResponse:
        """Action to set water temperature."""
        ha_device_id = call.data["device_id"]
        temperature = call.data["temperature"]
        flow_rate = call.data["flow_rate"]

        # Convert HA device ID to Moen device ID
        device_id = get_moen_device_id(hass, ha_device_id)
        if not device_id:
            # If conversion failed, try using it as-is (for backward compatibility)
            device_id = ha_device_id

        # Find the coordinator for this device
        coordinator = None
        for _entry_id, entry_coordinator in hass.data.get(
            "moen_smart_water", {}
        ).items():
            if isinstance(entry_coordinator, MoenDataUpdateCoordinator):
                devices = entry_coordinator.get_all_devices()
                if device_id in devices:
                    coordinator = entry_coordinator
                    break

        if not coordinator:
            error_msg = f"Device {device_id} not found in any configured Moen Smart Water integration"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
            }

        try:
            await hass.async_add_executor_job(
                coordinator.api.set_specific_temperature,
                device_id,
                temperature,
                flow_rate,
            )
            _LOGGER.info(
                "Set temperature to %.1f°C for device %s", temperature, device_id
            )

            # Get current device shadow to return state
            shadow = coordinator.get_device_shadow(device_id)

            return {
                "success": True,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
                "temperature": temperature,
                "flow_rate": flow_rate,
                "message": f"Set temperature to {temperature}°C for device {device_id}",
                "current_state": shadow.get("reported", {}).get("valveState", "unknown")
                if shadow
                else "unknown",
            }
        except Exception as err:
            error_msg = f"Failed to set temperature for device {device_id}: {err}"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
            }

    async def set_default_flow_rate(call: ServiceCall) -> ServiceResponse:
        """Action to set default flow rate for gesture activation."""
        ha_device_id = call.data["device_id"]
        default_flow_rate = call.data["default_flow_rate"]

        # Convert HA device ID to Moen device ID
        device_id = get_moen_device_id(hass, ha_device_id)
        if not device_id:
            # If conversion failed, try using it as-is (for backward compatibility)
            device_id = ha_device_id

        # Find the coordinator for this device
        coordinator = None
        for _entry_id, entry_coordinator in hass.data.get(
            "moen_smart_water", {}
        ).items():
            if isinstance(entry_coordinator, MoenDataUpdateCoordinator):
                devices = entry_coordinator.get_all_devices()
                if device_id in devices:
                    coordinator = entry_coordinator
                    break

        if not coordinator:
            error_msg = f"Device {device_id} not found in any configured Moen Smart Water integration"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
            }

        try:
            await hass.async_add_executor_job(
                coordinator.api.set_default_flow_rate, device_id, default_flow_rate
            )
            _LOGGER.info(
                "Set default flow rate (for gesture activation) to %d%% for device %s",
                default_flow_rate,
                device_id,
            )

            return {
                "success": True,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
                "default_flow_rate": default_flow_rate,
                "message": f"Set default flow rate to {default_flow_rate}% for device {device_id}",
            }
        except Exception as err:
            error_msg = f"Failed to set default flow rate for device {device_id}: {err}"
            _LOGGER.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "device_id": ha_device_id,
                "moen_device_id": device_id,
            }

    # Register actions
    try:
        hass.services.async_register(
            "moen_smart_water",
            "start_water",
            start_water,
            schema=START_WATER_SERVICE_SCHEMA,
            supports_response=True,
        )

        hass.services.async_register(
            "moen_smart_water",
            "dispense_volume",
            dispense_volume,
            schema=DISPENSE_VOLUME_SERVICE_SCHEMA,
            supports_response=True,
        )

        hass.services.async_register(
            "moen_smart_water",
            "stop_water",
            stop_water,
            schema=STOP_WATER_SERVICE_SCHEMA,
            supports_response=True,
        )

        hass.services.async_register(
            "moen_smart_water",
            "get_device_status",
            get_device_status,
            schema=GET_STATUS_SERVICE_SCHEMA,
            supports_response=True,
        )

        hass.services.async_register(
            "moen_smart_water",
            "get_user_profile",
            get_user_profile,
            schema=GET_USER_PROFILE_SERVICE_SCHEMA,
            supports_response=True,
        )

        hass.services.async_register(
            "moen_smart_water",
            "set_temperature",
            set_temperature,
            schema=SET_TEMPERATURE_SERVICE_SCHEMA,
            supports_response=True,
        )

        hass.services.async_register(
            "moen_smart_water",
            "set_default_flow_rate",
            set_default_flow_rate,
            schema=SET_DEFAULT_FLOW_RATE_SERVICE_SCHEMA,
            supports_response=True,
        )

        _LOGGER.info("Successfully registered all Moen Smart Water actions")
    except Exception as err:
        _LOGGER.error("Failed to register Moen Smart Water actions: %s", err)
        raise
