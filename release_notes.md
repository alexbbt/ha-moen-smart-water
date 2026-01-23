## Changes in this release

🎉 **Official 1.0.0 Release** - This marks the first stable release of the Moen Smart Water integration for Home Assistant!

### Complete Feature Overview

This release provides comprehensive integration with Moen Smart Water Network faucets, enabling full control and monitoring through Home Assistant.

#### Core Control Features

**Valve Entity** - Primary water control interface
- Open/close valve to start/stop water flow
- Adjustable flow rate position (0-100%) for precise control
- Real-time temperature display in both Celsius and Fahrenheit
- Automatic flow rate clamping based on device capabilities (trickleFlowRate to maxFlowRate)
- Optimistic UI updates with automatic API state synchronization
- Temperature preservation when adjusting flow rate

**Button Controls**
- **Start Water**: Instantly start water flow with default settings
- **Stop Water**: Immediately stop water flow

**Temperature Control**
- **Temperature Number Entity**: Set specific temperature (0-100°C)
  - Range automatically adjusts based on device-learned temperature limits
  - Works when water is idle (sets for next use) or running (changes immediately)
  - Supports both preset modes (coldest/hottest) and specific temperatures
- **Default Temperature Select**: Choose default temperature mode for gesture activation
  - Handle Position: Use physical handle position
  - Coldest: Always use coldest available temperature
  - Equal Mix: Use 50/50 hot/cold mix

**Flow Rate Control**
- **Default Flow Rate Number Entity**: Set flow rate percentage (10-100%) for gesture activation
  - Enhanced control: Allows setting as low as 10% (device's trickle flow rate)
  - Official Moen app restricts minimum to 30% - this integration provides finer control
- **Valve Position Control**: Real-time flow rate adjustment (0-100%)
  - Position preserved across temperature changes
  - 0% closes the valve

#### Monitoring & Sensors

**Operational Sensors**
- **Faucet State**: Current operational state (idle, running, etc.)
- **Water Usage Today**: Daily cumulative water usage in liters
- **Last Dispense Volume**: Volume of last dispense operation in milliliters
- **Temperature**: Current water temperature in Celsius
- **API Status**: Cloud connection status (Connected/Disconnected)

**Diagnostic Sensors**
- **Last Update**: Timestamp of last successful data update from integration
- **WiFi Network**: Connected WiFi network name
- **WiFi Signal**: WiFi signal strength in dBm
- **WiFi Connected**: WiFi connection status
- **Battery**: Battery percentage (if applicable)
- **Firmware Version**: Device firmware version
- **Last Connect**: Timestamp of last cloud connection from device

#### Programmatic Control Services

All services support response data for use in automations and scripts:

1. **start_water**: Start continuous water flow with specified temperature and flow rate
   - Temperature: Numeric (°C) or preset ("coldest", "hottest", "equal")
   - Flow rate: 0-100%
   - Returns: success, temperature, flow_rate, current_state

2. **dispense_volume**: Dispense specific volume (wave hand to start, auto-stops when volume reached)
   - Volume: 50-2000ml (required)
   - Temperature: Optional (numeric or preset)
   - Flow rate automatically set to 100% for accurate dispensing
   - Returns: success, volume_ml, temperature, timeout, current_state

3. **stop_water**: Stop water flow immediately
   - Returns: success, current_state

4. **set_temperature**: Set water temperature with optional flow rate
   - Temperature: Required (0-100°C)
   - Flow rate: Optional (0-100%)
   - Returns: success, temperature, flow_rate, current_state

5. **set_default_flow_rate**: Set default flow rate for gesture activation
   - Default flow rate: 0-100%
   - Returns: success, default_flow_rate

6. **get_device_status**: Retrieve complete device shadow data
   - Returns: success, shadow (complete device state data)

7. **get_user_profile**: Get user profile information from Moen API
   - Returns: success, profile (user data)

#### Integration Architecture

**Configuration Flow**
- UI-based setup through Home Assistant's integration system
- Automatic device discovery
- Secure credential storage with OAuth token management
- Automatic token refresh to minimize re-authentication

**Data Management**
- Coordinator-based data updates for efficient polling
- Automatic device shadow synchronization
- Optimistic UI updates with API confirmation
- Error handling and retry logic

**API Integration**
- Reverse-engineered Moen cloud API integration
- OAuth 2.0 authentication with automatic token refresh
- Device shadow management for state synchronization
- Water usage tracking and reporting

#### Technical Highlights

- **Home Assistant 2024.12.0+** compatibility
- **Platform.VALVE** support for native valve entity
- **Cloud Polling** architecture (iot_class: cloud_polling)
- **Type hints** throughout codebase
- **Comprehensive error handling** and logging
- **Device-specific constraints** respected (flow rate limits, temperature ranges)
- **Response data** in all services for automation integration

#### Installation & Setup

- Available via HACS (Home Assistant Community Store)
- Manual installation supported
- Simple configuration flow requiring only Moen account credentials
- Automatic device discovery

#### Security & Privacy

- Credentials stored in Home Assistant's encrypted configuration storage
- OAuth tokens automatically managed and refreshed
- All communication uses HTTPS/TLS encryption
- No local network access required - all communication through Moen's cloud services

#### Compatibility

- Tested with MotionSense Wave Kitchen Faucets (Cia model)
- May work with other models in the same family
- Requires Moen Smart Water Network faucet connected to network
- Requires faucet registered with Moen account

This 1.0.0 release represents a complete, production-ready integration that provides full control and monitoring of Moen Smart Water faucets through Home Assistant, with comprehensive entity support, programmatic control services, and robust error handling.
