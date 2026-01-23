"""Tests for Moen Smart Water actions."""

from __future__ import annotations

import voluptuous as vol

from custom_components.moen_smart_water.services import (
    DISPENSE_VOLUME_SERVICE_SCHEMA,
    GET_STATUS_SERVICE_SCHEMA,
    GET_USER_PROFILE_SERVICE_SCHEMA,
    SET_DEFAULT_FLOW_RATE_SERVICE_SCHEMA,
    SET_TEMPERATURE_SERVICE_SCHEMA,
    START_WATER_SERVICE_SCHEMA,
    STOP_WATER_SERVICE_SCHEMA,
)


class TestServiceSchemas:
    """Test action schemas."""

    def test_start_water_service_schema(self) -> None:
        """Test start water action schema."""
        assert START_WATER_SERVICE_SCHEMA is not None

        # Test valid data
        valid_data = {
            "device_id": "test_device",
            "temperature": "coldest",
            "flow_rate": 80,
        }
        result = START_WATER_SERVICE_SCHEMA(valid_data)
        assert result["device_id"] == "test_device"
        assert result["temperature"] == "coldest"
        assert result["flow_rate"] == 80

        # Test default values
        minimal_data = {"device_id": "test_device"}
        result = START_WATER_SERVICE_SCHEMA(minimal_data)
        assert result["temperature"] == "coldest"  # Default
        assert result["flow_rate"] == 100  # Default

        # Test numeric temperature
        numeric_temp_data = {"device_id": "test_device", "temperature": 25.5}
        result = START_WATER_SERVICE_SCHEMA(numeric_temp_data)
        assert result["temperature"] == 25.5 or result["temperature"] == "25.5"

    def test_dispense_volume_service_schema(self) -> None:
        """Test dispense volume action schema."""
        assert DISPENSE_VOLUME_SERVICE_SCHEMA is not None

        # Test valid data with all fields
        valid_data = {
            "device_id": "test_device",
            "volume_ml": 250,
            "timeout": 120,
        }
        result = DISPENSE_VOLUME_SERVICE_SCHEMA(valid_data)
        assert result["device_id"] == "test_device"
        assert result["volume_ml"] == 250
        assert result["timeout"] == 120

        # Test with optional temperature
        data_with_temp = {
            "device_id": "test_device",
            "volume_ml": 500,
            "temperature": "coldest",
        }
        result = DISPENSE_VOLUME_SERVICE_SCHEMA(data_with_temp)
        assert result["device_id"] == "test_device"
        assert result["volume_ml"] == 500
        assert result["temperature"] == "coldest"

        # Test minimal required data (device_id and volume_ml are required)
        minimal_data = {"device_id": "test_device", "volume_ml": 250}
        result = DISPENSE_VOLUME_SERVICE_SCHEMA(minimal_data)
        assert result["device_id"] == "test_device"
        assert result["volume_ml"] == 250
        assert "timeout" not in result  # timeout is optional
        assert "temperature" not in result  # temperature is optional

    def test_stop_water_service_schema(self) -> None:
        """Test stop water action schema."""
        assert STOP_WATER_SERVICE_SCHEMA is not None

        valid_data = {"device_id": "test_device"}
        result = STOP_WATER_SERVICE_SCHEMA(valid_data)
        assert result["device_id"] == "test_device"

    def test_get_status_service_schema(self) -> None:
        """Test get device status action schema."""
        assert GET_STATUS_SERVICE_SCHEMA is not None

        valid_data = {"device_id": "test_device"}
        result = GET_STATUS_SERVICE_SCHEMA(valid_data)
        assert result["device_id"] == "test_device"

    def test_get_user_profile_service_schema(self) -> None:
        """Test get user profile action schema."""
        assert GET_USER_PROFILE_SERVICE_SCHEMA is not None

        # Schema accepts empty dict
        result = GET_USER_PROFILE_SERVICE_SCHEMA({})
        assert result == {}

    def test_set_temperature_service_schema(self) -> None:
        """Test set temperature action schema."""
        assert SET_TEMPERATURE_SERVICE_SCHEMA is not None

        valid_data = {
            "device_id": "test_device",
            "temperature": 30.0,
            "flow_rate": 80,
        }
        result = SET_TEMPERATURE_SERVICE_SCHEMA(valid_data)
        assert result["device_id"] == "test_device"
        assert result["temperature"] == 30.0
        assert result["flow_rate"] == 80

        # Test default flow_rate
        minimal_data = {"device_id": "test_device", "temperature": 30.0}
        result = SET_TEMPERATURE_SERVICE_SCHEMA(minimal_data)
        assert result["flow_rate"] == 100  # Default

    def test_set_default_flow_rate_service_schema(self) -> None:
        """Test set default flow rate action schema."""
        assert SET_DEFAULT_FLOW_RATE_SERVICE_SCHEMA is not None

        valid_data = {
            "device_id": "test_device",
            "default_flow_rate": 75,
        }
        result = SET_DEFAULT_FLOW_RATE_SERVICE_SCHEMA(valid_data)
        assert result["device_id"] == "test_device"
        assert result["default_flow_rate"] == 75

    def test_dispense_volume_schema_validation(self) -> None:
        """Test that dispense volume schema validates ranges."""
        # Test volume_ml is required
        try:
            DISPENSE_VOLUME_SERVICE_SCHEMA({"device_id": "test"})
            raise AssertionError("Should have raised error for missing volume_ml")
        except vol.Invalid:
            pass

        # Test volume_ml min
        try:
            DISPENSE_VOLUME_SERVICE_SCHEMA({"device_id": "test", "volume_ml": 10})
            raise AssertionError("Should have raised error for volume_ml < 50")
        except vol.Invalid:
            pass

        # Test volume_ml max
        try:
            DISPENSE_VOLUME_SERVICE_SCHEMA({"device_id": "test", "volume_ml": 3000})
            raise AssertionError("Should have raised error for volume_ml > 2000")
        except vol.Invalid:
            pass

        # Test valid minimal data
        result = DISPENSE_VOLUME_SERVICE_SCHEMA({"device_id": "test", "volume_ml": 250})
        assert result["device_id"] == "test"
        assert result["volume_ml"] == 250

    def test_temperature_schema_validation(self) -> None:
        """Test that temperature schema validates ranges."""
        # Test temperature min
        try:
            SET_TEMPERATURE_SERVICE_SCHEMA({"device_id": "test", "temperature": -10.0})
            raise AssertionError("Should have raised error for temperature < 0")
        except vol.Invalid:
            pass

        # Test temperature max
        try:
            SET_TEMPERATURE_SERVICE_SCHEMA({"device_id": "test", "temperature": 150.0})
            raise AssertionError("Should have raised error for temperature > 100")
        except vol.Invalid:
            pass

    def test_flow_rate_schema_validation(self) -> None:
        """Test that flow rate schema validates ranges."""
        # Test flow_rate min
        try:
            SET_DEFAULT_FLOW_RATE_SERVICE_SCHEMA(
                {"device_id": "test", "default_flow_rate": -10}
            )
            raise AssertionError("Should have raised error for flow_rate < 0")
        except vol.Invalid:
            pass

        # Test flow_rate max
        try:
            SET_DEFAULT_FLOW_RATE_SERVICE_SCHEMA(
                {"device_id": "test", "default_flow_rate": 150}
            )
            raise AssertionError("Should have raised error for flow_rate > 100")
        except vol.Invalid:
            pass
