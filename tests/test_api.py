"""Comprehensive tests for Moen API."""

from __future__ import annotations

from custom_components.moen_smart_water.api import MoenAPI


class TestMoenAPIInitialization:
    """Test MoenAPI initialization."""

    def test_api_init_without_tokens(self) -> None:
        """Test API initialization without stored tokens."""
        api = MoenAPI("test@example.com", "password")

        assert api.username == "test@example.com"
        assert api.password == "password"
        assert api.client_id == "6qn9pep31dglq6ed4fvlq6rp5t"
        assert api.access_token is None
        assert api.refresh_token is None
        assert api.id_token is None
        assert api.token_expiry == 0

    def test_api_init_with_tokens(self) -> None:
        """Test API initialization with stored tokens."""
        tokens = {
            "access_token": "test_access",
            "refresh_token": "test_refresh",
            "id_token": "test_id",
            "token_expiry": 9999999999.0,
        }
        api = MoenAPI("test@example.com", "password", tokens=tokens)

        assert api.access_token == "test_access"
        assert api.refresh_token == "test_refresh"
        assert api.id_token == "test_id"
        assert api.token_expiry == 9999999999.0

    def test_api_session_headers(self) -> None:
        """Test that API session has correct headers."""
        api = MoenAPI("test@example.com", "password")

        assert "User-Agent" in api.session.headers
        assert api.session.headers["User-Agent"] == "Smartwater-iOS-prod-3.39.0"

    def test_api_cached_data_initialization(self) -> None:
        """Test that API cached data is initialized correctly."""
        api = MoenAPI("test@example.com", "password")

        assert api._user_profile is None
        assert api._locations is None
        assert api._devices is None
        assert api._temperature_definitions is None

    def test_get_tokens_structure(self) -> None:
        """Test getting tokens returns correct structure."""
        api = MoenAPI("test@example.com", "password")
        api.access_token = "test_access"
        api.refresh_token = "test_refresh"
        api.id_token = "test_id"
        api.token_expiry = 3600

        tokens = api.get_tokens()

        assert "access_token" in tokens
        assert "refresh_token" in tokens
        assert "id_token" in tokens
        assert "token_expiry" in tokens

    def test_api_has_required_methods(self) -> None:
        """Test that API has all required methods."""
        api = MoenAPI("test@example.com", "password")

        assert hasattr(api, "login")
        assert hasattr(api, "get_user_profile")
        assert hasattr(api, "list_devices")
        assert hasattr(api, "get_cached_devices")
        assert hasattr(api, "get_device_shadow")
        assert hasattr(api, "start_water_flow")
        assert hasattr(api, "stop_water_flow")
        assert hasattr(api, "set_specific_temperature")
        assert hasattr(api, "set_default_flow_rate")
        assert hasattr(api, "set_coldest")
        assert hasattr(api, "set_hottest")
        assert hasattr(api, "set_warm")
