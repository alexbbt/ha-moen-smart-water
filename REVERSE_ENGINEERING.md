# Moen SmartWater – Simple mitmproxy Setup Guide

This guide shows the **simplest, correct way** to capture and inspect Moen SmartWater mobile app traffic using **mitmproxy with a web UI**.

This is optimized for reverse‑engineering and Home Assistant integration development.

---

## What You Need

- A laptop (macOS/Linux)
- Your phone on the **same Wi‑Fi network**
- **mitmproxy** installed

Install mitmproxy:

```bash
brew install mitmproxy
# or
pip install mitmproxy
```

---

## Important Terminology (Avoid Common Mistakes)

- `mitmproxy` → **terminal UI only**
- `mitmweb` → **web UI (browser-based)** ✅

👉 If you want a web UI, you **must use `mitmweb`**

---

## One Correct Command (Use This)

```bash
mitmweb   --listen-port 8090   --web-port 8091   -w moen_app_capture.mitm
```

### What this does

- **Proxy server**: `http://<laptop-ip>:8090`
- **Web UI**: `http://localhost:8091`
- **Capture file**: `moen_app_capture.mitm`

---

## Phone Wi‑Fi Proxy Settings (iOS)

1. Settings → Wi‑Fi
2. Tap your connected network
3. Scroll to **HTTP Proxy**
4. Set to **Manual**
5. Configure:
   - **Server**: your laptop IP (example: `10.0.10.173`)
   - **Port**: `8090`
6. Save

⚠️ Do **not** use the web port (`8091`) on your phone.

---

## Install mitmproxy Certificate (Required)

1. On your phone, open Safari
2. Visit:

```
http://mitm.it
```

3. Download the **iOS certificate**
4. Install it:
   - Settings → General → VPN & Device Management
5. Trust it:
   - Settings → General → About → Certificate Trust Settings
   - Enable trust for **mitmproxy**

---

## Capture Moen Traffic

1. Start `mitmweb`
2. Open the **Moen SmartWater app**
3. Perform actions:
   - Login
   - View devices
   - Start / stop faucet
   - Change temperature
4. Wait ~30 seconds
5. Stop `mitmweb` (`Ctrl+C`)

---

## View the Traffic

- Open your browser to:
  ```
  http://localhost:8091
  ```
- Filter for:
  - `execute-api.us-east-2.amazonaws.com`
  - `/invoker`
  - `"fn": "smartwater-app-..."`

---

## Replay a Capture Later

```bash
mitmweb -r moen_app_capture.mitm
```

---

## Common Problems

### ❌ `--web-port` not recognized
You are using `mitmproxy` instead of `mitmweb`.

### ❌ No traffic captured
- Proxy not enabled on phone
- Wrong port used
- Certificate not trusted

---

## Summary

- Use **`mitmweb`**, not `mitmproxy`
- Phone uses **proxy port**
- Browser uses **web UI port**
- Focus on `/invoker` + `"fn"` calls

This setup is sufficient to fully reverse engineer SmartWater APIs.
