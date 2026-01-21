> [!IMPORTANT]
> Before setting up the integration, ensure your Moen Smart Water Network faucet is connected to your network and accessible via the Moen mobile app. This integration requires your Moen account credentials and uses the reverse-engineered official Moen cloud API.

# Moen Smart Water Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
[![ha_version](https://img.shields.io/badge/Home%20Assistant-2024.1%2B-blue.svg?style=for-the-badge)](https://www.home-assistant.io/)
[![version](https://img.shields.io/github/v/release/alexbbt/ha-moen-smart-water?style=for-the-badge&color=purple)](https://github.com/alexbbt/ha-moen-smart-water/releases)
[![license](https://img.shields.io/github/license/alexbbt/ha-moen-smart-water?style=for-the-badge&color=red)](https://github.com/alexbbt/ha-moen-smart-water/blob/main/LICENSE)
[![iot_class](https://img.shields.io/badge/iot_class-cloud_polling-green.svg?style=for-the-badge)](https://developers.home-assistant.io/docs/creating_integration_manifest#iot-class)

### Smart Faucet Control Made Simple
#### Control your Moen Smart Water Network faucet directly from Home Assistant

* Complete water flow control with valve entity (open/close/position)
* Real-time temperature control and monitoring (0-100°C)
* Adjustable flow rate control (10-100%)
* Volume-based dispensing (50-2000ml)
* Comprehensive diagnostic sensors (WiFi, Battery, Firmware)
* Cloud connection status monitoring
* Easy UI-based configuration
* Professional Moen integration with full API access

> [!WARNING]
> - This integration is **unofficial** and not affiliated with Moen
> - It requires your Moen account credentials to work
> - All communication goes through Moen's cloud services
> - Use at your own risk - may violate Moen's Terms of Service
> - The integration is based on reverse-engineering the official mobile app

### Supported Devices
#### This integration has been tested with the following Moen Smart Water Network faucet series

### MotionSense Wave Kitchen Faucets
* **Tested**: Cia model
* **Likely Compatible**: Other MotionSense Wave Kitchen Faucets
* **Unknown**: Other Moen Smart Water Network families

### Requirements
* Faucet connected to your home network
* Registered with a Moen account
* Valid Moen account credentials

> [!NOTE]
> Only tested with MotionSense Wave Kitchen Faucets (Cia model). May work with other models in the same family. [Report other models](https://github.com/alexbbt/ha-moen-smart-water/issues/new).

## Features

- **Valve Entity**: Control water flow with open/close/position control
  - Open/close valve to start/stop water flow
  - Adjustable flow rate position (0-100%)
  - Real-time temperature display
- **Button Controls**:
  - Start Water (starts flow with current settings)
  - Stop Water (stops water flow immediately)
- **Number Entities**:
  - Temperature control (0-100°C, range adjusts based on learned device limits)
  - Default Flow Rate (10-100%, used for gesture activation)
- **Select Entity**:
  - Default Temperature mode for gesture activation (Handle Position, Coldest, Equal Mix)
- **Sensors**:
  - Faucet state
  - Water usage today (daily cumulative total)
  - Last dispense volume
  - Current temperature
  - API Status
  - Last Update (timestamp)
  - WiFi Network name
  - WiFi Signal strength (dBm)
  - WiFi Connected status
  - Battery percentage
  - Firmware Version
  - Last Connect (timestamp)
- **Services**: Programmatic control via Home Assistant services

## Advanced Configuration

### Temperature Control

The integration provides comprehensive temperature control for your Moen Smart Faucet:

- **Temperature Number Entity**: Set specific temperature (0-100°C)
  - Range automatically adjusts based on your faucet's learned temperature limits
  - Works both when water is idle (sets for next use) and running (changes immediately)
- **Temperature Sensor**: Monitor current water temperature in real-time
- **Default Temperature Select**: Choose default temperature mode for gesture activation
  - Handle Position: Use physical handle position
  - Coldest: Always use coldest available temperature
  - Equal Mix: Use 50/50 hot/cold mix

### Flow Rate Control

The integration provides a **Default Flow Rate** number entity that allows you to set the flow rate percentage (10-100%) used when activating the faucet via gesture controls (hand wave or handle). This setting is applied when you start the water flow without explicitly specifying a flow rate.

**Valve Position Control**: Use the valve entity to control flow rate in real-time
- Set position 0-100% to control water flow intensity
- Position is preserved across temperature changes
- Position 0% closes the valve

**Enhanced Control vs. Official App:**
- The Home Assistant integration allows setting the default flow rate as low as **10%** (the device's trickle flow rate)
- The official Moen mobile app restricts this to a minimum of **30%**
- This provides finer control over water flow, useful for scenarios requiring minimal flow rates

> [!TIP]
> **Use Cases for Lower Flow Rates (10-30%):**
> - Hand washing and personal hygiene
> - Washing delicate items
> - Filling containers slowly to prevent splashing
> - Conserving water for routine tasks

## Time & Date Sensors

For general time and date needs, we recommend using Home Assistant's built-in [Time & Date integration](https://www.home-assistant.io/integrations/time_date/). This integration provides:

- Current date and time in various formats
- Automatic timezone handling
- Standard Home Assistant time/date sensors
- No custom code required

### Device-Specific Timestamps

This integration provides device-specific timestamp sensors:
- **Last Update**: When the integration last successfully updated data from the Moen API
- **Last Connect**: When the faucet last connected to the Moen cloud

These are different from general system time and provide specific information about your faucet's connectivity and data freshness.

## Installation

### Via [HACS](https://hacs.xyz/)
<a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=alexbbt&repository=ha-moen-smart-water&category=integration" target="_blank"><img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Open your Home Assistant instance and open a repository inside the Home Assistant Community Store." /></a>

### Manually

Get the folder `custom_components/moen_smart_water` in your HA `config/custom_components`

## Configuration
<a href="https://my.home-assistant.io/redirect/config_flow_start/?domain=moen_smart_water" target="_blank"><img src="https://my.home-assistant.io/badges/config_flow_start.svg" alt="Open your Home Assistant instance and start setting up a new integration." /></a>

- Enter your Moen account credentials and optionally adjust the client ID.

> [!TIP]
> **Finding Your Client ID:**
> * The integration provides a default value (`moen_mobile_app`) that may work
> * For best results, extract your specific client ID using a network monitoring tool
> * Use mitmproxy to capture traffic from the official Moen app
> * Look for API calls to `*.execute-api.us-east-2.amazonaws.com`
> * Find the `client_id` field in the login request

## Entity Naming

Entities are automatically created for each connected Moen Smart Water Network faucet. They are named in the format `{device_name}_{entity_type}` for easy identification.

The integration automatically detects and creates entities for:

- **Valve**: Water control with flow position (0-100%)
- **Buttons**: Start Water, Stop Water
- **Numbers**: Temperature control (0-100°C), Default Flow Rate (10-100%)
- **Select**: Default Temperature mode (Handle Position, Coldest, Equal Mix)
- **Sensors**: Faucet state, Water usage today, Temperature, Last dispense volume, API status, WiFi info, Battery, Firmware, Timestamps

> [!NOTE]
> Only entities available on your specific faucet model will be created. The integration queries your Moen account and only adds entities for faucets that are detected.

Example entity names:
- `valve.kitchen_faucet_water_control`
- `button.kitchen_faucet_start_water`
- `button.kitchen_faucet_stop_water`
- `number.kitchen_faucet_temperature`
- `number.kitchen_faucet_default_flow_rate`
- `select.kitchen_faucet_default_temperature`
- `sensor.kitchen_faucet_faucet_state`
- `sensor.kitchen_faucet_water_usage_today`
- `sensor.kitchen_faucet_temperature`
- `sensor.kitchen_faucet_last_dispense_volume`
- `sensor.kitchen_faucet_api_status`
- `sensor.kitchen_faucet_battery`
- `sensor.kitchen_faucet_wifi_signal`

### Services

You can also control the faucet programmatically using services:

```yaml
# Dispense water with specific volume
service: moen_smart_water.dispense_water
data:
  device_id: "your_device_id"
  volume_ml: 500  # Optional, 50-2000ml
  timeout: 120    # Optional, 10-300s

# Stop dispensing
service: moen_smart_water.stop_dispensing
data:
  device_id: "your_device_id"

# Set temperature
service: moen_smart_water.set_temperature
data:
  device_id: "your_device_id"
  temperature: 25  # Temperature in Celsius
  flow_rate: 100   # Optional, 0-100%

# Set default flow rate (for gesture activation)
service: moen_smart_water.set_default_flow_rate
data:
  device_id: "your_device_id"
  default_flow_rate: 50  # 0-100%

# Get device status
service: moen_smart_water.get_device_status
data:
  device_id: "your_device_id"

# Get user profile
service: moen_smart_water.get_user_profile
```

> [!TIP]
> **Finding Your Device ID:**
> * Check the Home Assistant logs after integration setup
> * Look for device discovery messages
> * Use the `moen_smart_water.get_device_status` service to list available devices
> * Device ID is visible in the device information page in Home Assistant

### Automations

Example automations for common use cases:

```yaml
# Example 1: Open valve when motion is detected
- alias: "Start water on motion"
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_motion
      to: "on"
  action:
    - service: valve.open_valve
      target:
        entity_id: valve.kitchen_faucet_water_control

# Example 2: Dispense specific volume
- alias: "Dispense water for coffee"
  trigger:
    - platform: state
      entity_id: input_boolean.make_coffee
      to: "on"
  action:
    - service: moen_smart_water.dispense_water
      data:
        device_id: "your_device_id"
        volume_ml: 500
        timeout: 120

# Example 3: Set temperature based on time of day
- alias: "Morning warm water"
  trigger:
    - platform: time
      at: "07:00:00"
  action:
    - service: number.set_value
      target:
        entity_id: number.kitchen_faucet_temperature
      data:
        value: 35  # Warm temperature in Celsius

# Example 4: Adjust flow rate for gentle washing
- alias: "Gentle flow for delicates"
  trigger:
    - platform: state
      entity_id: input_boolean.gentle_mode
      to: "on"
  action:
    - service: valve.set_valve_position
      target:
        entity_id: valve.kitchen_faucet_water_control
      data:
        position: 20  # 20% flow rate
```

> [!NOTE]
> Replace `"your_device_id"` and entity IDs with your actual device/entity names. You can find device IDs in the Home Assistant logs or device information pages.

## Troubleshooting

To troubleshoot your Home Assistant instance, you can add the following configuration to your configuration.yaml file:

```yaml
logger:
  default: warning  # Default log level for all components
  logs:
    custom_components.moen_smart_water: debug    # Enable debug logging for this integration
```

> [!WARNING]
> **Common Issues:**
> * Ensure the faucet is powered on and connected to your network
> * Verify your Moen account credentials are correct
> * Check that the faucet is online in the official Moen mobile app
> * Try using the default client ID (`moen_mobile_app`) first
> * Check Home Assistant logs for any error messages
> * Some faucet features may not be available on all models

## API Endpoints

The integration uses the following Moen API endpoints:
- Login: `POST /prod/auth/login`
- List devices: `GET /prod/devices`
- Device status: `GET /prod/devices/{device_id}/status`
- Send command: `POST /prod/devices/{device_id}/commands`

> [!NOTE]
> These endpoints are part of Moen's official cloud API and may change without notice. The integration will be updated accordingly.

## Security

- Credentials are stored securely in Home Assistant's configuration
- All communication uses HTTPS/TLS
- No local network access required

## Contributing

This integration is based on reverse-engineering the official Moen mobile app. If you have additional information about the API or encounter issues, please:

1. Check the existing issues
2. Create a new issue with detailed information
3. Include relevant logs and network captures (sanitized)

### Development Setup

This project uses pre-commit hooks to ensure code quality and consistency. To set up the development environment:

#### Create and activate virtual environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

#### Install pre-commit
```bash
pip install pre-commit
```

#### Install git hooks
```bash
pre-commit install
```

#### Run pre-commit on all files
```bash
pre-commit run --all-files
```

The pre-commit hooks will automatically:
- Run **ruff** for code linting and formatting
- Run **mypy** for type checking
- Ensure code follows the project's style guidelines

> [!TIP]
> Pre-commit hooks will run automatically on every commit. If you want to commit code that doesn't pass the checks, use `git commit --no-verify` (not recommended for regular development).

#### Manual Testing
You can also run the linting tools manually:

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows

# Install test dependencies
pip install -r requirements-test.txt

# Run ruff (code linting)
ruff check custom_components

# Run mypy (type checking)
mypy custom_components
```

## Disclaimer

This integration is not officially supported by Moen. Use at your own risk. The authors are not responsible for any damage or issues that may arise from using this integration.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
