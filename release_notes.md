## Changes in this release

### Bug Fixes
- Fixed water usage sensor device class to use `WATER` instead of `VOLUME` for proper Home Assistant water usage tracking
  - This resolves the "Unexpected device class" warning in Home Assistant's water usage tracking feature
  - The sensor will now be properly recognized for individual water device tracking

### Maintenance
- Updated test manifest validation to align with HACS requirements
- Cleaned up HACS workflow configuration by removing unused ignores tag
