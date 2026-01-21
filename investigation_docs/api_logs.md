# Store debug logs for later reference

## Update Cycle with Debug Logging

2026-01-20 23:18:52.379 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Starting coordinator data update
2026-01-20 23:18:52.380 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Coordinator received 1 devices
2026-01-20 23:18:52.380 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadows for 1 devices
2026-01-20 23:18:52.380 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadow for device 101046568
2026-01-20 23:18:52.380 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Getting device shadow for 101046568
2026-01-20 23:18:52.380 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:18:52.380 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow request payload: {'parse': False, 'fn': 'smartwater-app-shadow-api-prod-get', 'escape': False, 'body': {'clientId': '101046568', 'shadow': True, 'locale': 'en_US'}}
2026-01-20 23:18:52.621 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow response status: 200
2026-01-20 23:18:52.621 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"state\":{\"desired\":{\"deviceLost\":true,\"dispenseActivateTimeout\":120,\"handleTimeout\":300,\"freezeEnable\":false,\"sensorTimeout\":300,\"voiceTimeout\":300},\"reported\":{\"firmwareVersion\":\"v1.1.8c\",\"wifiNetwork\":\"temp\",\"connected\":true,\"lastConnect\":1768964307943,\"wifiRssi\":-77,\"wifiNoPoll\":false,\"state\":\"idle\",\"flowCalSrc\":\"factory\",\"assemblyAirTemp\":19,\"isFreezing\":false,\"beeperVolume\":0,\"sensorDisable\":0,\"freezeEnable\":false,\"defaultFlowRate\":30,\"maxFlowRate\":100,\"trickleFlowRate\":10,\"purgeTimeout\":120,\"handleTimeout\":300,\"sensorTimeout\":300,\"voiceTimeout\":300,\"dispenseActivateTimeout\":120,\"safetyLimitTemp\":48.889999,\"safetyModeEnabled\":true,\"childLimitTemp\":40.560001,\"childModeEnabled\":false,\"defaultTemp\":\"equal\",\"handleReverse\":false,\"gestureMode\":\"na\",\"setpointColdTemp\":0,\"setpointWarmTemp\":40.556,\"setpointHotTemp\":100,\"lowFlowRate\":127,\"unwinterizeTimeout\":60,\"healthProtectTimeout\":120,\"sensorConfig\":\"gesture_handle\",\"handleFW\":\"v0.6.23b\",\"latchFW\":\"v0.6.8a\",\"sensorCommError\":false,\"handleCommError\":false,\"batteryLifeRemaining\":-1,\"batteryPercentage\":100,\"batterySavingLevel\":\"normal\",\"powerSource\":\"battery\",\"volume\":1071969,\"temperature\":12.631,\"temperatureLast\":12.724,\"learnedMinTemp\":12.546,\"learnedMaxTemp\":53.959,\"temperatureGoal\":\"coldest\"},\"delta\":{\"deviceLost\":true}},\"metadata\":{\"desired\":{\"deviceLost\":{\"timestamp\":1767074340},\"dispenseActivateTimeout\":{\"timestamp\":1768977075},\"handleTimeout\":{\"timestamp\":1768977075},\"freezeEnable\":{\"timestamp\":1768977075},\"sensorTimeout\":{\"timestamp\":1768977075},\"voiceTimeout\":{\"timestamp\":1768977075}},\"reported\":{\"firmwareVersion\":{\"timestamp\":1768964310},\"wifiNetwork\":{\"timestamp\":1768964310},\"connected\":{\"timestamp\":1768964310},\"lastConnect\":{\"timestamp\":1768964310},\"wifiRssi\":{\"timestamp\":1768964310},\"wifiNoPoll\":{\"timestamp\":1768964310},\"state\":{\"timestamp\":1768979786},\"flowCalSrc\":{\"timestamp\":1768964310},\"assemblyAirTemp\":{\"timestamp\":1768964310},\"isFreezing\":{\"timestamp\":1768964310},\"beeperVolume\":{\"timestamp\":1768964310},\"sensorDisable\":{\"timestamp\":1768964310},\"freezeEnable\":{\"timestamp\":1768964310},\"defaultFlowRate\":{\"timestamp\":1768978218},\"maxFlowRate\":{\"timestamp\":1768964310},\"trickleFlowRate\":{\"timestamp\":1768964310},\"purgeTimeout\":{\"timestamp\":1768964310},\"handleTimeout\":{\"timestamp\":1768964310},\"sensorTimeout\":{\"timestamp\":1768964310},\"voiceTimeout\":{\"timestamp\":1768964310},\"dispenseActivateTimeout\":{\"timestamp\":1768964310},\"safetyLimitTemp\":{\"timestamp\":1768964310},\"safetyModeEnabled\":{\"timestamp\":1768964310},\"childLimitTemp\":{\"timestamp\":1768964310},\"childModeEnabled\":{\"timestamp\":1768964310},\"defaultTemp\":{\"timestamp\":1768972077},\"handleReverse\":{\"timestamp\":1768964310},\"gestureMode\":{\"timestamp\":1768964310},\"setpointColdTemp\":{\"timestamp\":1768964310},\"setpointWarmTemp\":{\"timestamp\":1768964310},\"setpointHotTemp\":{\"timestamp\":1768964310},\"lowFlowRate\":{\"timestamp\":1768964310},\"unwinterizeTimeout\":{\"timestamp\":1768964310},\"healthProtectTimeout\":{\"timestamp\":1768964310},\"sensorConfig\":{\"timestamp\":1768964310},\"handleFW\":{\"timestamp\":1768964310},\"latchFW\":{\"timestamp\":1768964310},\"sensorCommError\":{\"timestamp\":1768964310},\"handleCommError\":{\"timestamp\":1768964310},\"batteryLifeRemaining\":{\"timestamp\":1768964310},\"batteryPercentage\":{\"timestamp\":1768964310},\"batterySavingLevel\":{\"timestamp\":1768964310},\"powerSource\":{\"timestamp\":1768964310},\"volume\":{\"timestamp\":1768979786},\"temperature\":{\"timestamp\":1768979786},\"temperatureLast\":{\"timestamp\":1768979786},\"learnedMinTemp\":{\"timestamp\":1768979786},\"learnedMaxTemp\":{\"timestamp\":1768964735},\"temperatureGoal\":{\"timestamp\":1768978206}}},\"version\":6949,\"timestamp\":1768979932}}"
}
2026-01-20 23:18:52.621 INFO (SyncWorker_2) [custom_components.moen_smart_water.api] Retrieved device shadow for 101046568
2026-01-20 23:18:52.621 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow parsed data: {
  "state": {
    "desired": {
      "deviceLost": true,
      "dispenseActivateTimeout": 120,
      "handleTimeout": 300,
      "freezeEnable": false,
      "sensorTimeout": 300,
      "voiceTimeout": 300
    },
    "reported": {
      "firmwareVersion": "v1.1.8c",
      "wifiNetwork": "temp",
      "connected": true,
      "lastConnect": 1768964307943,
      "wifiRssi": -77,
      "wifiNoPoll": false,
      "state": "idle",
      "flowCalSrc": "factory",
      "assemblyAirTemp": 19,
      "isFreezing": false,
      "beeperVolume": 0,
      "sensorDisable": 0,
      "freezeEnable": false,
      "defaultFlowRate": 30,
      "maxFlowRate": 100,
      "trickleFlowRate": 10,
      "purgeTimeout": 120,
      "handleTimeout": 300,
      "sensorTimeout": 300,
      "voiceTimeout": 300,
      "dispenseActivateTimeout": 120,
      "safetyLimitTemp": 48.889999,
      "safetyModeEnabled": true,
      "childLimitTemp": 40.560001,
      "childModeEnabled": false,
      "defaultTemp": "equal",
      "handleReverse": false,
      "gestureMode": "na",
      "setpointColdTemp": 0,
      "setpointWarmTemp": 40.556,
      "setpointHotTemp": 100,
      "lowFlowRate": 127,
      "unwinterizeTimeout": 60,
      "healthProtectTimeout": 120,
      "sensorConfig": "gesture_handle",
      "handleFW": "v0.6.23b",
      "latchFW": "v0.6.8a",
      "sensorCommError": false,
      "handleCommError": false,
      "batteryLifeRemaining": -1,
      "batteryPercentage": 100,
      "batterySavingLevel": "normal",
      "powerSource": "battery",
      "volume": 1071969,
      "temperature": 12.631,
      "temperatureLast": 12.724,
      "learnedMinTemp": 12.546,
      "learnedMaxTemp": 53.959,
      "temperatureGoal": "coldest"
    },
    "delta": {
      "deviceLost": true
    }
  },
  "metadata": {
    "desired": {
      "deviceLost": {
        "timestamp": 1767074340
      },
      "dispenseActivateTimeout": {
        "timestamp": 1768977075
      },
      "handleTimeout": {
        "timestamp": 1768977075
      },
      "freezeEnable": {
        "timestamp": 1768977075
      },
      "sensorTimeout": {
        "timestamp": 1768977075
      },
      "voiceTimeout": {
        "timestamp": 1768977075
      }
    },
    "reported": {
      "firmwareVersion": {
        "timestamp": 1768964310
      },
      "wifiNetwork": {
        "timestamp": 1768964310
      },
      "connected": {
        "timestamp": 1768964310
      },
      "lastConnect": {
        "timestamp": 1768964310
      },
      "wifiRssi": {
        "timestamp": 1768964310
      },
      "wifiNoPoll": {
        "timestamp": 1768964310
      },
      "state": {
        "timestamp": 1768979786
      },
      "flowCalSrc": {
        "timestamp": 1768964310
      },
      "assemblyAirTemp": {
        "timestamp": 1768964310
      },
      "isFreezing": {
        "timestamp": 1768964310
      },
      "beeperVolume": {
        "timestamp": 1768964310
      },
      "sensorDisable": {
        "timestamp": 1768964310
      },
      "freezeEnable": {
        "timestamp": 1768964310
      },
      "defaultFlowRate": {
        "timestamp": 1768978218
      },
      "maxFlowRate": {
        "timestamp": 1768964310
      },
      "trickleFlowRate": {
        "timestamp": 1768964310
      },
      "purgeTimeout": {
        "timestamp": 1768964310
      },
      "handleTimeout": {
        "timestamp": 1768964310
      },
      "sensorTimeout": {
        "timestamp": 1768964310
      },
      "voiceTimeout": {
        "timestamp": 1768964310
      },
      "dispenseActivateTimeout": {
        "timestamp": 1768964310
      },
      "safetyLimitTemp": {
        "timestamp": 1768964310
      },
      "safetyModeEnabled": {
        "timestamp": 1768964310
      },
      "childLimitTemp": {
        "timestamp": 1768964310
      },
      "childModeEnabled": {
        "timestamp": 1768964310
      },
      "defaultTemp": {
        "timestamp": 1768972077
      },
      "handleReverse": {
        "timestamp": 1768964310
      },
      "gestureMode": {
        "timestamp": 1768964310
      },
      "setpointColdTemp": {
        "timestamp": 1768964310
      },
      "setpointWarmTemp": {
        "timestamp": 1768964310
      },
      "setpointHotTemp": {
        "timestamp": 1768964310
      },
      "lowFlowRate": {
        "timestamp": 1768964310
      },
      "unwinterizeTimeout": {
        "timestamp": 1768964310
      },
      "healthProtectTimeout": {
        "timestamp": 1768964310
      },
      "sensorConfig": {
        "timestamp": 1768964310
      },
      "handleFW": {
        "timestamp": 1768964310
      },
      "latchFW": {
        "timestamp": 1768964310
      },
      "sensorCommError": {
        "timestamp": 1768964310
      },
      "handleCommError": {
        "timestamp": 1768964310
      },
      "batteryLifeRemaining": {
        "timestamp": 1768964310
      },
      "batteryPercentage": {
        "timestamp": 1768964310
      },
      "batterySavingLevel": {
        "timestamp": 1768964310
      },
      "powerSource": {
        "timestamp": 1768964310
      },
      "volume": {
        "timestamp": 1768979786
      },
      "temperature": {
        "timestamp": 1768979786
      },
      "temperatureLast": {
        "timestamp": 1768979786
      },
      "learnedMinTemp": {
        "timestamp": 1768979786
      },
      "learnedMaxTemp": {
        "timestamp": 1768964735
      },
      "temperatureGoal": {
        "timestamp": 1768978206
      }
    }
  },
  "version": 6949,
  "timestamp": 1768979932
}
2026-01-20 23:18:52.621 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Successfully fetched shadow for device 101046568
2026-01-20 23:18:52.622 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetched 1 device shadows
2026-01-20 23:18:52.622 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Finished fetching moen_smart_water data in 0.243 seconds (success: True)
2026-01-20 23:18:52.622 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Raw state data for device 101046568: {'firmwareVersion': 'v1.1.8c', 'wifiNetwork': 'temp', 'connected': True, 'lastConnect': 1768964307943, 'wifiRssi': -77, 'wifiNoPoll': False, 'state': 'idle', 'flowCalSrc': 'factory', 'assemblyAirTemp': 19, 'isFreezing': False, 'beeperVolume': 0, 'sensorDisable': 0, 'freezeEnable': False, 'defaultFlowRate': 30, 'maxFlowRate': 100, 'trickleFlowRate': 10, 'purgeTimeout': 120, 'handleTimeout': 300, 'sensorTimeout': 300, 'voiceTimeout': 300, 'dispenseActivateTimeout': 120, 'safetyLimitTemp': 48.889999, 'safetyModeEnabled': True, 'childLimitTemp': 40.560001, 'childModeEnabled': False, 'defaultTemp': 'equal', 'handleReverse': False, 'gestureMode': 'na', 'setpointColdTemp': 0, 'setpointWarmTemp': 40.556, 'setpointHotTemp': 100, 'lowFlowRate': 127, 'unwinterizeTimeout': 60, 'healthProtectTimeout': 120, 'sensorConfig': 'gesture_handle', 'handleFW': 'v0.6.23b', 'latchFW': 'v0.6.8a', 'sensorCommError': False, 'handleCommError': False, 'batteryLifeRemaining': -1, 'batteryPercentage': 100, 'batterySavingLevel': 'normal', 'powerSource': 'battery', 'volume': 1071969, 'temperature': 12.631, 'temperatureLast': 12.724, 'learnedMinTemp': 12.546, 'learnedMaxTemp': 53.959, 'temperatureGoal': 'coldest'}
2026-01-20 23:18:52.623 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Parsed values - device_state=idle, flow_rate=None, temperature=12.631°C (54.7°F)
2026-01-20 23:18:52.623 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Using API data, is_valve_open=False
2026-01-20 23:18:52.623 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Setting to CLOSED
2026-01-20 23:18:52.623 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Updated state to closed, position=0
