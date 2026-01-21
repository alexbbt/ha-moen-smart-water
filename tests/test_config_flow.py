"""Tests for Moen Smart Water config flow."""

from __future__ import annotations

from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

from custom_components.moen_smart_water.config_flow import (
    STEP_USER_DATA_SCHEMA,
    CannotConnect,
    ConfigFlow,
    InvalidAuth,
)


class TestConfigFlow:
    """Test ConfigFlow class."""

    def test_config_flow_exists(self) -> None:
        """Test that ConfigFlow class exists."""
        flow = ConfigFlow()
        assert flow is not None
        assert flow.VERSION == 1

    def test_step_user_data_schema(self) -> None:
        """Test that user data schema is defined."""
        assert STEP_USER_DATA_SCHEMA is not None
        assert CONF_USERNAME in STEP_USER_DATA_SCHEMA.schema
        assert CONF_PASSWORD in STEP_USER_DATA_SCHEMA.schema

    def test_cannot_connect_exception(self) -> None:
        """Test CannotConnect exception."""
        exc = CannotConnect("Connection failed")
        assert str(exc) == "Connection failed"
        assert isinstance(exc, Exception)

    def test_invalid_auth_exception(self) -> None:
        """Test InvalidAuth exception."""
        exc = InvalidAuth("Invalid credentials")
        assert str(exc) == "Invalid credentials"
        assert isinstance(exc, Exception)
