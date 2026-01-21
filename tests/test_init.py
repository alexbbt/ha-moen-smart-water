"""Tests for Moen Smart Water integration setup."""

from __future__ import annotations

from homeassistant.const import Platform

from custom_components.moen_smart_water import (
    PLATFORMS,
    __version__,
)


class TestIntegrationSetup:
    """Test integration setup."""

    def test_version(self) -> None:
        """Test that version is defined."""
        assert __version__ is not None
        assert isinstance(__version__, str)
        assert len(__version__) > 0

    def test_platforms(self) -> None:
        """Test that platforms are defined."""
        assert PLATFORMS is not None
        assert isinstance(PLATFORMS, list)
        assert len(PLATFORMS) > 0
        assert Platform.BUTTON in PLATFORMS
        assert Platform.NUMBER in PLATFORMS
        assert Platform.SENSOR in PLATFORMS
        assert Platform.SELECT in PLATFORMS
        assert Platform.VALVE in PLATFORMS

    def test_platforms_count(self) -> None:
        """Test that all expected platforms are present."""
        assert len(PLATFORMS) == 5
