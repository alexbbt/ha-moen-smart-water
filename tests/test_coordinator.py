"""Tests for Moen Smart Water coordinator."""

from __future__ import annotations

from custom_components.moen_smart_water.coordinator import (
    SCAN_INTERVAL,
    MoenDataUpdateCoordinator,
)


class TestMoenDataUpdateCoordinator:
    """Test MoenDataUpdateCoordinator class."""

    def test_scan_interval(self) -> None:
        """Test that scan interval is defined."""
        assert SCAN_INTERVAL is not None
        assert SCAN_INTERVAL.total_seconds() == 30

    def test_coordinator_class_exists(self) -> None:
        """Test that coordinator class exists."""
        assert MoenDataUpdateCoordinator is not None

    def test_coordinator_has_required_methods(self) -> None:
        """Test that coordinator has required methods."""
        assert hasattr(MoenDataUpdateCoordinator, "get_device")
        assert hasattr(MoenDataUpdateCoordinator, "get_device_shadow")
        assert hasattr(MoenDataUpdateCoordinator, "get_all_devices")
        assert hasattr(MoenDataUpdateCoordinator, "get_all_device_shadows")
        assert hasattr(MoenDataUpdateCoordinator, "_async_update_data")
