"""Tests for the realtime device shadow client and coordinator merge."""

from __future__ import annotations

import json
from unittest.mock import MagicMock

from custom_components.moen_smart_water.coordinator import (
    MoenDataUpdateCoordinator,
    _merge_reported,
)
from custom_components.moen_smart_water.iot import parse_shadow_message

TOPIC = "$aws/things/101046568/shadow"


def _payload(doc: object) -> bytes:
    return json.dumps(doc).encode()


class TestParseShadowMessage:
    """Tests for parse_shadow_message."""

    def test_update_accepted(self) -> None:
        payload = _payload({"state": {"reported": {"state": "running"}}})
        assert parse_shadow_message(f"{TOPIC}/update/accepted", payload) == (
            "101046568",
            {"state": "running"},
        )

    def test_update_documents_uses_current(self) -> None:
        payload = _payload(
            {
                "previous": {"state": {"reported": {"state": "idle"}}},
                "current": {"state": {"reported": {"state": "running"}}},
            }
        )
        assert parse_shadow_message(f"{TOPIC}/update/documents", payload) == (
            "101046568",
            {"state": "running"},
        )

    def test_get_accepted(self) -> None:
        payload = _payload({"state": {"reported": {"temperature": 30.1}}})
        assert parse_shadow_message(f"{TOPIC}/get/accepted", payload) == (
            "101046568",
            {"temperature": 30.1},
        )

    def test_desired_only_is_ignored(self) -> None:
        payload = _payload({"state": {"desired": {"command": "run"}}})
        assert parse_shadow_message(f"{TOPIC}/update/accepted", payload) is None

    def test_invalid_payloads_are_ignored(self) -> None:
        topic = f"{TOPIC}/update/accepted"
        assert parse_shadow_message(topic, b"not json") is None
        assert parse_shadow_message(topic, b"[1, 2]") is None
        assert parse_shadow_message(topic, _payload({"state": None})) is None

    def test_unexpected_topic_is_ignored(self) -> None:
        payload = _payload({"state": {"reported": {"state": "running"}}})
        assert parse_shadow_message("other/topic", payload) is None


class TestMergeReported:
    """Tests for merging partial shadow updates."""

    def test_merges_nested_and_deletes_null(self) -> None:
        target = {"state": "idle", "alerts": {"a": 1, "b": 2}, "volume": 10}
        _merge_reported(
            target, {"state": "running", "alerts": {"b": 3}, "volume": None}
        )
        assert target == {"state": "running", "alerts": {"a": 1, "b": 3}}


class TestCoordinatorIngest:
    """Tests for MoenDataUpdateCoordinator.async_ingest_shadow_update."""

    def test_ingest_merges_into_cached_shadow(self) -> None:
        coordinator = MagicMock(spec=MoenDataUpdateCoordinator)
        coordinator._devices = {}
        coordinator._device_details = {}
        coordinator._device_usage = {}
        coordinator._device_shadows = {
            "101046568": {"state": {"reported": {"state": "idle", "wifiRssi": -70}}}
        }
        coordinator._snapshot = lambda: MoenDataUpdateCoordinator._snapshot(coordinator)

        MoenDataUpdateCoordinator.async_ingest_shadow_update(
            coordinator, "101046568", {"state": "running"}
        )

        assert coordinator._device_shadows["101046568"]["state"]["reported"] == {
            "state": "running",
            "wifiRssi": -70,
        }
        coordinator.async_set_updated_data.assert_called_once()
