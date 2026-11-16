"""Realtime AWS IoT Device Shadow client for Moen Smart Water.

The Moen cloud mirrors each faucet's state in an AWS IoT Device Shadow and
publishes changes to it over MQTT. This client exchanges the account's Cognito
id_token for temporary AWS credentials, connects to the IoT endpoint over a
SigV4-signed WebSocket, and subscribes to each device's shadow topics. Reported
state is merged into the coordinator as it arrives; the REST poll keeps running
as a fallback and full-state reconciler.
"""

from __future__ import annotations

import json
import logging
import time
import uuid
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

import requests
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.event import async_call_later

if TYPE_CHECKING:
    from .coordinator import MoenDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

# Fixed public identifiers of the Moen Smart Water cloud.
REGION = "us-east-2"
IDENTITY_POOL_ID = "us-east-2:7880fbef-a3a8-4ffc-a0d1-74e686e79c80"
USER_POOL_ID = "us-east-2_9puIPVyv1"
IOT_ENDPOINT = "a1r2q5ic87novc-ats.iot.us-east-2.amazonaws.com"
LOGIN_PROVIDER = f"cognito-idp.{REGION}.amazonaws.com/{USER_POOL_ID}"
COGNITO_IDENTITY_URL = f"https://cognito-identity.{REGION}.amazonaws.com/"

# `update/accepted` carries partial deltas, `update/documents` the full
# document after each update, and `get/accepted` answers our state request.
SHADOW_TOPICS = ("update/accepted", "update/documents", "get/accepted")

REFRESH_MARGIN = 600  # Reconnect this many seconds before credentials expire.
DEFAULT_CRED_LIFETIME = 3600
RECONNECT_BACKOFF = 60
HTTP_TIMEOUT = 20


def fetch_aws_credentials(id_token: str) -> dict[str, Any]:
    """Exchange a Cognito id_token for temporary AWS credentials (blocking).

    GetId and GetCredentialsForIdentity are unsigned calls; the login token is
    the authorization. Returns the Credentials block with `Expiration` as epoch
    seconds.
    """
    logins = {LOGIN_PROVIDER: id_token}

    def _post(target: str, body: dict[str, Any]) -> dict[str, Any]:
        resp = requests.post(
            COGNITO_IDENTITY_URL,
            json=body,
            headers={
                "Content-Type": "application/x-amz-json-1.1",
                "X-Amz-Target": f"AWSCognitoIdentityService.{target}",
            },
            timeout=HTTP_TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()

    identity_id = _post(
        "GetId", {"IdentityPoolId": IDENTITY_POOL_ID, "Logins": logins}
    )["IdentityId"]
    creds = _post(
        "GetCredentialsForIdentity", {"IdentityId": identity_id, "Logins": logins}
    )["Credentials"]
    if not isinstance(creds.get("Expiration"), (int, float)):
        creds["Expiration"] = time.time() + DEFAULT_CRED_LIFETIME
    return creds


def parse_shadow_message(
    topic: str, payload: bytes
) -> tuple[str, dict[str, Any]] | None:
    """Return (thing name, reported state) from a shadow message, if any."""
    parts = topic.split("/")
    if len(parts) < 4 or parts[:2] != ["$aws", "things"]:
        return None
    try:
        doc = json.loads(payload)
    except ValueError:
        return None
    if not isinstance(doc, dict):
        return None
    if topic.endswith("update/documents"):
        doc = doc.get("current") or {}
    reported = (doc.get("state") or {}).get("reported")
    if not isinstance(reported, dict) or not reported:
        return None
    return parts[2], reported


class MoenIotClient:
    """Keeps an MQTT shadow subscription open and feeds the coordinator."""

    def __init__(
        self, hass: HomeAssistant, coordinator: MoenDataUpdateCoordinator
    ) -> None:
        """Initialize the client."""
        self.hass = hass
        self.coordinator = coordinator
        self._thing_ids = [tid for tid in coordinator.get_all_devices() if tid]
        self._connection: Any = None
        self._cancel_reconnect: Callable[[], None] | None = None
        self._stopping = False
        self._failure_logged = False

    async def async_start(self) -> None:
        """Connect and subscribe. Failures are logged and retried, never raised."""
        if self._thing_ids:
            await self._async_connect()

    async def async_stop(self) -> None:
        """Cancel any pending reconnect and close the connection."""
        self._stopping = True
        if self._cancel_reconnect is not None:
            self._cancel_reconnect()
            self._cancel_reconnect = None
        connection, self._connection = self._connection, None
        self.coordinator.async_set_realtime_connected(False)
        if connection is not None:
            await self.hass.async_add_executor_job(_disconnect, connection)

    async def _async_connect(self) -> None:
        """Open a fresh connection, replacing the previous one if any."""
        try:
            creds = await self.hass.async_add_executor_job(self._get_credentials)
            connection = await self.hass.async_add_executor_job(self._connect, creds)
        except Exception as err:  # noqa: BLE001 - polling keeps working regardless
            if not self._failure_logged:
                _LOGGER.warning(
                    "Realtime updates unavailable, retrying every %ss: %s",
                    RECONNECT_BACKOFF,
                    err,
                )
                self._failure_logged = True
            self.coordinator.async_set_realtime_connected(False)
            self._schedule_reconnect(RECONNECT_BACKOFF)
            return

        if self._stopping:
            await self.hass.async_add_executor_job(_disconnect, connection)
            return

        old, self._connection = self._connection, connection
        if old is not None:
            await self.hass.async_add_executor_job(_disconnect, old)

        if self._failure_logged:
            _LOGGER.info("Realtime updates reconnected")
            self._failure_logged = False
        _LOGGER.debug("Subscribed to %d device shadow(s)", len(self._thing_ids))
        self.coordinator.async_set_realtime_connected(True)
        self._schedule_reconnect(
            max(creds["Expiration"] - time.time() - REFRESH_MARGIN, RECONNECT_BACKOFF)
        )

    def _get_credentials(self) -> dict[str, Any]:
        """Refresh the Moen login if needed and fetch AWS credentials (blocking)."""
        self.coordinator.api.ensure_authenticated()
        if not self.coordinator.api.id_token:
            raise RuntimeError("No Cognito id_token available")
        return fetch_aws_credentials(self.coordinator.api.id_token)

    def _connect(self, creds: dict[str, Any]) -> Any:
        """Build the MQTT connection, connect and subscribe (blocking)."""
        # Imported lazily so awscrt is only loaded when realtime is enabled.
        from awscrt import auth
        from awsiot import mqtt_connection_builder

        connection = mqtt_connection_builder.websockets_with_default_aws_signing(
            endpoint=IOT_ENDPOINT,
            region=REGION,
            credentials_provider=auth.AwsCredentialsProvider.new_static(
                access_key_id=creds["AccessKeyId"],
                secret_access_key=creds["SecretKey"],
                session_token=creds["SessionToken"],
            ),
            client_id=f"ha-moen-{uuid.uuid4().hex}",
            clean_session=True,
            keep_alive_secs=30,
            on_connection_interrupted=self._on_interrupted,
            on_connection_resumed=self._on_resumed,
        )
        connection.connect().result()
        try:
            self._subscribe(connection)
        except Exception:
            _disconnect(connection)
            raise
        return connection

    def _subscribe(self, connection: Any) -> None:
        """Subscribe to every device's shadow and request its current state."""
        from awscrt import mqtt

        for thing_id in self._thing_ids:
            prefix = f"$aws/things/{thing_id}/shadow"
            for suffix in SHADOW_TOPICS:
                connection.subscribe(
                    topic=f"{prefix}/{suffix}",
                    qos=mqtt.QoS.AT_LEAST_ONCE,
                    callback=self._on_message,
                )[0].result()
            connection.publish(
                topic=f"{prefix}/get", payload=b"", qos=mqtt.QoS.AT_LEAST_ONCE
            )

    def _resubscribe(self, connection: Any) -> None:
        """Restore subscriptions after the broker dropped our session (blocking)."""
        if self._stopping:
            return
        try:
            self._subscribe(connection)
        except Exception as err:  # noqa: BLE001
            _LOGGER.debug("Realtime resubscribe failed: %s", err)

    # awscrt invokes the callbacks below on its own IO thread.

    def _on_message(self, topic: str, payload: bytes, **_kwargs: Any) -> None:
        if (parsed := parse_shadow_message(topic, payload)) is not None:
            self.hass.loop.call_soon_threadsafe(
                self.coordinator.async_ingest_shadow_update, *parsed
            )

    def _on_interrupted(self, connection: Any, error: Any, **_kwargs: Any) -> None:
        _LOGGER.debug("Realtime connection interrupted: %s", error)
        self.hass.loop.call_soon_threadsafe(self._async_set_connected, False)

    def _on_resumed(
        self, connection: Any, return_code: Any, session_present: bool, **_kwargs: Any
    ) -> None:
        _LOGGER.debug("Realtime connection resumed")
        self.hass.loop.call_soon_threadsafe(self._async_set_connected, True)
        if not session_present:
            self.hass.add_job(self._resubscribe, connection)

    @callback
    def _async_set_connected(self, connected: bool) -> None:
        if not self._stopping:
            self.coordinator.async_set_realtime_connected(connected)

    @callback
    def _schedule_reconnect(self, delay: float) -> None:
        if self._cancel_reconnect is not None:
            self._cancel_reconnect()
        if self._stopping:
            self._cancel_reconnect = None
            return

        async def _reconnect(_now: Any) -> None:
            self._cancel_reconnect = None
            await self._async_connect()

        self._cancel_reconnect = async_call_later(self.hass, delay, _reconnect)


def _disconnect(connection: Any) -> None:
    """Close an MQTT connection, ignoring errors (blocking)."""
    try:
        connection.disconnect().result()
    except Exception as err:  # noqa: BLE001 - teardown must not raise
        _LOGGER.debug("Error closing realtime connection: %s", err)
