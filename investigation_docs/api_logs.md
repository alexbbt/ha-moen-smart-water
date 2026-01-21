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


## Change valve and tempature logs

2026-01-20 23:31:06.379 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Starting coordinator data update
2026-01-20 23:31:06.380 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Coordinator received 1 devices
2026-01-20 23:31:06.380 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadows for 1 devices
2026-01-20 23:31:06.380 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadow for device 101046568
2026-01-20 23:31:06.380 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Getting device shadow for 101046568
2026-01-20 23:31:06.380 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Shadow request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:06.380 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Shadow request payload: {'parse': False, 'fn': 'smartwater-app-shadow-api-prod-get', 'escape': False, 'body': {'clientId': '101046568', 'shadow': True, 'locale': 'en_US'}}
2026-01-20 23:31:06.499 ERROR (Thread-5) [pychromecast.socket_client] [Garage TV(10.0.10.159):8009] Error reading from socket: socket connection broken
2026-01-20 23:31:06.554 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Shadow response status: 200
2026-01-20 23:31:06.554 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Shadow full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"state\":{\"desired\":{\"deviceLost\":true,\"dispenseActivateTimeout\":120,\"handleTimeout\":300,\"freezeEnable\":false,\"sensorTimeout\":300,\"voiceTimeout\":300},\"reported\":{\"firmwareVersion\":\"v1.1.8c\",\"wifiNetwork\":\"temp\",\"connected\":true,\"lastConnect\":1768964307943,\"wifiRssi\":-77,\"wifiNoPoll\":false,\"state\":\"idle\",\"flowCalSrc\":\"factory\",\"assemblyAirTemp\":16,\"isFreezing\":false,\"beeperVolume\":0,\"sensorDisable\":0,\"freezeEnable\":false,\"defaultFlowRate\":30,\"maxFlowRate\":100,\"trickleFlowRate\":10,\"purgeTimeout\":120,\"handleTimeout\":300,\"sensorTimeout\":300,\"voiceTimeout\":300,\"dispenseActivateTimeout\":120,\"safetyLimitTemp\":48.889999,\"safetyModeEnabled\":true,\"childLimitTemp\":40.560001,\"childModeEnabled\":false,\"defaultTemp\":\"equal\",\"handleReverse\":false,\"gestureMode\":\"na\",\"setpointColdTemp\":0,\"setpointWarmTemp\":40.556,\"setpointHotTemp\":100,\"lowFlowRate\":127,\"unwinterizeTimeout\":60,\"healthProtectTimeout\":120,\"sensorConfig\":\"gesture_handle\",\"handleFW\":\"v0.6.23b\",\"latchFW\":\"v0.6.8a\",\"sensorCommError\":false,\"handleCommError\":false,\"batteryLifeRemaining\":-1,\"batteryPercentage\":100,\"batterySavingLevel\":\"normal\",\"powerSource\":\"battery\",\"volume\":3053009,\"temperature\":34.803001,\"temperatureLast\":46.812,\"learnedMinTemp\":12.546,\"learnedMaxTemp\":53.959,\"temperatureGoal\":\"hottest\"},\"delta\":{\"deviceLost\":true}},\"metadata\":{\"desired\":{\"deviceLost\":{\"timestamp\":1767074340},\"dispenseActivateTimeout\":{\"timestamp\":1768977075},\"handleTimeout\":{\"timestamp\":1768977075},\"freezeEnable\":{\"timestamp\":1768977075},\"sensorTimeout\":{\"timestamp\":1768977075},\"voiceTimeout\":{\"timestamp\":1768977075}},\"reported\":{\"firmwareVersion\":{\"timestamp\":1768964310},\"wifiNetwork\":{\"timestamp\":1768964310},\"connected\":{\"timestamp\":1768964310},\"lastConnect\":{\"timestamp\":1768964310},\"wifiRssi\":{\"timestamp\":1768964310},\"wifiNoPoll\":{\"timestamp\":1768964310},\"state\":{\"timestamp\":1768980479},\"flowCalSrc\":{\"timestamp\":1768964310},\"assemblyAirTemp\":{\"timestamp\":1768980036},\"isFreezing\":{\"timestamp\":1768964310},\"beeperVolume\":{\"timestamp\":1768964310},\"sensorDisable\":{\"timestamp\":1768964310},\"freezeEnable\":{\"timestamp\":1768964310},\"defaultFlowRate\":{\"timestamp\":1768978218},\"maxFlowRate\":{\"timestamp\":1768964310},\"trickleFlowRate\":{\"timestamp\":1768964310},\"purgeTimeout\":{\"timestamp\":1768964310},\"handleTimeout\":{\"timestamp\":1768964310},\"sensorTimeout\":{\"timestamp\":1768964310},\"voiceTimeout\":{\"timestamp\":1768964310},\"dispenseActivateTimeout\":{\"timestamp\":1768964310},\"safetyLimitTemp\":{\"timestamp\":1768964310},\"safetyModeEnabled\":{\"timestamp\":1768964310},\"childLimitTemp\":{\"timestamp\":1768964310},\"childModeEnabled\":{\"timestamp\":1768964310},\"defaultTemp\":{\"timestamp\":1768972077},\"handleReverse\":{\"timestamp\":1768964310},\"gestureMode\":{\"timestamp\":1768964310},\"setpointColdTemp\":{\"timestamp\":1768964310},\"setpointWarmTemp\":{\"timestamp\":1768964310},\"setpointHotTemp\":{\"timestamp\":1768964310},\"lowFlowRate\":{\"timestamp\":1768964310},\"unwinterizeTimeout\":{\"timestamp\":1768964310},\"healthProtectTimeout\":{\"timestamp\":1768964310},\"sensorConfig\":{\"timestamp\":1768964310},\"handleFW\":{\"timestamp\":1768964310},\"latchFW\":{\"timestamp\":1768964310},\"sensorCommError\":{\"timestamp\":1768964310},\"handleCommError\":{\"timestamp\":1768964310},\"batteryLifeRemaining\":{\"timestamp\":1768964310},\"batteryPercentage\":{\"timestamp\":1768964310},\"batterySavingLevel\":{\"timestamp\":1768964310},\"powerSource\":{\"timestamp\":1768964310},\"volume\":{\"timestamp\":1768980479},\"temperature\":{\"timestamp\":1768980479},\"temperatureLast\":{\"timestamp\":1768980479},\"learnedMinTemp\":{\"timestamp\":1768979786},\"learnedMaxTemp\":{\"timestamp\":1768964735},\"temperatureGoal\":{\"timestamp\":1768980479}}},\"version\":6960,\"timestamp\":1768980666}}"
}
2026-01-20 23:31:06.554 INFO (SyncWorker_4) [custom_components.moen_smart_water.api] Retrieved device shadow for 101046568
2026-01-20 23:31:06.554 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Shadow parsed data: {
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
      "assemblyAirTemp": 16,
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
      "volume": 3053009,
      "temperature": 34.803001,
      "temperatureLast": 46.812,
      "learnedMinTemp": 12.546,
      "learnedMaxTemp": 53.959,
      "temperatureGoal": "hottest"
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
        "timestamp": 1768980479
      },
      "flowCalSrc": {
        "timestamp": 1768964310
      },
      "assemblyAirTemp": {
        "timestamp": 1768980036
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
        "timestamp": 1768980479
      },
      "temperature": {
        "timestamp": 1768980479
      },
      "temperatureLast": {
        "timestamp": 1768980479
      },
      "learnedMinTemp": {
        "timestamp": 1768979786
      },
      "learnedMaxTemp": {
        "timestamp": 1768964735
      },
      "temperatureGoal": {
        "timestamp": 1768980479
      }
    }
  },
  "version": 6960,
  "timestamp": 1768980666
}
2026-01-20 23:31:06.554 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Successfully fetched shadow for device 101046568
2026-01-20 23:31:06.554 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetched 1 device shadows
2026-01-20 23:31:06.554 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Finished fetching moen_smart_water data in 0.175 seconds (success: True)
2026-01-20 23:31:06.555 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Raw state data for device 101046568: {'firmwareVersion': 'v1.1.8c', 'wifiNetwork': 'temp', 'connected': True, 'lastConnect': 1768964307943, 'wifiRssi': -77, 'wifiNoPoll': False, 'state': 'idle', 'flowCalSrc': 'factory', 'assemblyAirTemp': 16, 'isFreezing': False, 'beeperVolume': 0, 'sensorDisable': 0, 'freezeEnable': False, 'defaultFlowRate': 30, 'maxFlowRate': 100, 'trickleFlowRate': 10, 'purgeTimeout': 120, 'handleTimeout': 300, 'sensorTimeout': 300, 'voiceTimeout': 300, 'dispenseActivateTimeout': 120, 'safetyLimitTemp': 48.889999, 'safetyModeEnabled': True, 'childLimitTemp': 40.560001, 'childModeEnabled': False, 'defaultTemp': 'equal', 'handleReverse': False, 'gestureMode': 'na', 'setpointColdTemp': 0, 'setpointWarmTemp': 40.556, 'setpointHotTemp': 100, 'lowFlowRate': 127, 'unwinterizeTimeout': 60, 'healthProtectTimeout': 120, 'sensorConfig': 'gesture_handle', 'handleFW': 'v0.6.23b', 'latchFW': 'v0.6.8a', 'sensorCommError': False, 'handleCommError': False, 'batteryLifeRemaining': -1, 'batteryPercentage': 100, 'batterySavingLevel': 'normal', 'powerSource': 'battery', 'volume': 3053009, 'temperature': 34.803001, 'temperatureLast': 46.812, 'learnedMinTemp': 12.546, 'learnedMaxTemp': 53.959, 'temperatureGoal': 'hottest'}
2026-01-20 23:31:06.555 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Parsed values - device_state=idle, flow_rate=None, temperature=34.803001°C (94.6°F)
2026-01-20 23:31:06.555 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Using API data, is_valve_open=False
2026-01-20 23:31:06.555 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Setting to CLOSED
2026-01-20 23:31:06.555 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Updated state to closed, position=0
2026-01-20 23:31:06.570 DEBUG (SyncWorker_0) [custom_components.moen_smart_water.api] Updating device shadow for 101046568
2026-01-20 23:31:06.570 DEBUG (SyncWorker_0) [custom_components.moen_smart_water.api] Update request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:06.570 DEBUG (SyncWorker_0) [custom_components.moen_smart_water.api] Update request payload: {
  "parse": false,
  "fn": "smartwater-app-shadow-api-prod-update",
  "escape": false,
  "body": {
    "payload": {
      "commandSrc": "app",
      "command": "run",
      "temperature": 29.444444444444443,
      "flowRate": 100
    },
    "locale": "en_US",
    "clientId": "101046568"
  }
}
2026-01-20 23:31:06.810 DEBUG (SyncWorker_0) [custom_components.moen_smart_water.api] Update response status: 200
2026-01-20 23:31:06.810 DEBUG (SyncWorker_0) [custom_components.moen_smart_water.api] Update full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"status\":true}}"
}
2026-01-20 23:31:06.810 INFO (SyncWorker_0) [custom_components.moen_smart_water.api] Updated device shadow for 101046568
2026-01-20 23:31:06.810 DEBUG (SyncWorker_0) [custom_components.moen_smart_water.api] Update parsed result: {
  "status": true
}
2026-01-20 23:31:06.810 INFO (MainThread) [custom_components.moen_smart_water.number] Set temperature to 29.4°C for device 101046568
2026-01-20 23:31:07.812 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Starting coordinator data update
2026-01-20 23:31:07.812 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Coordinator received 1 devices
2026-01-20 23:31:07.812 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadows for 1 devices
2026-01-20 23:31:07.812 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadow for device 101046568
2026-01-20 23:31:07.812 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Getting device shadow for 101046568
2026-01-20 23:31:07.812 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:07.812 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow request payload: {'parse': False, 'fn': 'smartwater-app-shadow-api-prod-get', 'escape': False, 'body': {'clientId': '101046568', 'shadow': True, 'locale': 'en_US'}}
2026-01-20 23:31:07.960 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow response status: 200
2026-01-20 23:31:07.960 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"state\":{\"desired\":{\"deviceLost\":true,\"dispenseActivateTimeout\":120,\"handleTimeout\":300,\"freezeEnable\":false,\"sensorTimeout\":300,\"voiceTimeout\":300,\"commandSrc\":\"app\",\"command\":\"run\",\"temperature\":29.444444444444443,\"flowRate\":100},\"reported\":{\"firmwareVersion\":\"v1.1.8c\",\"wifiNetwork\":\"temp\",\"connected\":true,\"lastConnect\":1768964307943,\"wifiRssi\":-77,\"wifiNoPoll\":false,\"state\":\"idle\",\"flowCalSrc\":\"factory\",\"assemblyAirTemp\":16,\"isFreezing\":false,\"beeperVolume\":0,\"sensorDisable\":0,\"freezeEnable\":false,\"defaultFlowRate\":30,\"maxFlowRate\":100,\"trickleFlowRate\":10,\"purgeTimeout\":120,\"handleTimeout\":300,\"sensorTimeout\":300,\"voiceTimeout\":300,\"dispenseActivateTimeout\":120,\"safetyLimitTemp\":48.889999,\"safetyModeEnabled\":true,\"childLimitTemp\":40.560001,\"childModeEnabled\":false,\"defaultTemp\":\"equal\",\"handleReverse\":false,\"gestureMode\":\"na\",\"setpointColdTemp\":0,\"setpointWarmTemp\":40.556,\"setpointHotTemp\":100,\"lowFlowRate\":127,\"unwinterizeTimeout\":60,\"healthProtectTimeout\":120,\"sensorConfig\":\"gesture_handle\",\"handleFW\":\"v0.6.23b\",\"latchFW\":\"v0.6.8a\",\"sensorCommError\":false,\"handleCommError\":false,\"batteryLifeRemaining\":-1,\"batteryPercentage\":100,\"batterySavingLevel\":\"normal\",\"powerSource\":\"battery\",\"volume\":3053009,\"temperature\":34.803001,\"temperatureLast\":46.812,\"learnedMinTemp\":12.546,\"learnedMaxTemp\":53.959,\"temperatureGoal\":\"hottest\"},\"delta\":{\"deviceLost\":true,\"commandSrc\":\"app\",\"command\":\"run\",\"temperature\":29.444444444444443,\"flowRate\":100}},\"metadata\":{\"desired\":{\"deviceLost\":{\"timestamp\":1767074340},\"dispenseActivateTimeout\":{\"timestamp\":1768977075},\"handleTimeout\":{\"timestamp\":1768977075},\"freezeEnable\":{\"timestamp\":1768977075},\"sensorTimeout\":{\"timestamp\":1768977075},\"voiceTimeout\":{\"timestamp\":1768977075},\"commandSrc\":{\"timestamp\":1768980666},\"command\":{\"timestamp\":1768980666},\"temperature\":{\"timestamp\":1768980666},\"flowRate\":{\"timestamp\":1768980666}},\"reported\":{\"firmwareVersion\":{\"timestamp\":1768964310},\"wifiNetwork\":{\"timestamp\":1768964310},\"connected\":{\"timestamp\":1768964310},\"lastConnect\":{\"timestamp\":1768964310},\"wifiRssi\":{\"timestamp\":1768964310},\"wifiNoPoll\":{\"timestamp\":1768964310},\"state\":{\"timestamp\":1768980479},\"flowCalSrc\":{\"timestamp\":1768964310},\"assemblyAirTemp\":{\"timestamp\":1768980036},\"isFreezing\":{\"timestamp\":1768964310},\"beeperVolume\":{\"timestamp\":1768964310},\"sensorDisable\":{\"timestamp\":1768964310},\"freezeEnable\":{\"timestamp\":1768964310},\"defaultFlowRate\":{\"timestamp\":1768978218},\"maxFlowRate\":{\"timestamp\":1768964310},\"trickleFlowRate\":{\"timestamp\":1768964310},\"purgeTimeout\":{\"timestamp\":1768964310},\"handleTimeout\":{\"timestamp\":1768964310},\"sensorTimeout\":{\"timestamp\":1768964310},\"voiceTimeout\":{\"timestamp\":1768964310},\"dispenseActivateTimeout\":{\"timestamp\":1768964310},\"safetyLimitTemp\":{\"timestamp\":1768964310},\"safetyModeEnabled\":{\"timestamp\":1768964310},\"childLimitTemp\":{\"timestamp\":1768964310},\"childModeEnabled\":{\"timestamp\":1768964310},\"defaultTemp\":{\"timestamp\":1768972077},\"handleReverse\":{\"timestamp\":1768964310},\"gestureMode\":{\"timestamp\":1768964310},\"setpointColdTemp\":{\"timestamp\":1768964310},\"setpointWarmTemp\":{\"timestamp\":1768964310},\"setpointHotTemp\":{\"timestamp\":1768964310},\"lowFlowRate\":{\"timestamp\":1768964310},\"unwinterizeTimeout\":{\"timestamp\":1768964310},\"healthProtectTimeout\":{\"timestamp\":1768964310},\"sensorConfig\":{\"timestamp\":1768964310},\"handleFW\":{\"timestamp\":1768964310},\"latchFW\":{\"timestamp\":1768964310},\"sensorCommError\":{\"timestamp\":1768964310},\"handleCommError\":{\"timestamp\":1768964310},\"batteryLifeRemaining\":{\"timestamp\":1768964310},\"batteryPercentage\":{\"timestamp\":1768964310},\"batterySavingLevel\":{\"timestamp\":1768964310},\"powerSource\":{\"timestamp\":1768964310},\"volume\":{\"timestamp\":1768980479},\"temperature\":{\"timestamp\":1768980479},\"temperatureLast\":{\"timestamp\":1768980479},\"learnedMinTemp\":{\"timestamp\":1768979786},\"learnedMaxTemp\":{\"timestamp\":1768964735},\"temperatureGoal\":{\"timestamp\":1768980479}}},\"version\":6961,\"timestamp\":1768980667}}"
}
2026-01-20 23:31:07.960 INFO (SyncWorker_1) [custom_components.moen_smart_water.api] Retrieved device shadow for 101046568
2026-01-20 23:31:07.960 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow parsed data: {
  "state": {
    "desired": {
      "deviceLost": true,
      "dispenseActivateTimeout": 120,
      "handleTimeout": 300,
      "freezeEnable": false,
      "sensorTimeout": 300,
      "voiceTimeout": 300,
      "commandSrc": "app",
      "command": "run",
      "temperature": 29.444444444444443,
      "flowRate": 100
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
      "assemblyAirTemp": 16,
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
      "volume": 3053009,
      "temperature": 34.803001,
      "temperatureLast": 46.812,
      "learnedMinTemp": 12.546,
      "learnedMaxTemp": 53.959,
      "temperatureGoal": "hottest"
    },
    "delta": {
      "deviceLost": true,
      "commandSrc": "app",
      "command": "run",
      "temperature": 29.444444444444443,
      "flowRate": 100
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
      },
      "commandSrc": {
        "timestamp": 1768980666
      },
      "command": {
        "timestamp": 1768980666
      },
      "temperature": {
        "timestamp": 1768980666
      },
      "flowRate": {
        "timestamp": 1768980666
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
        "timestamp": 1768980479
      },
      "flowCalSrc": {
        "timestamp": 1768964310
      },
      "assemblyAirTemp": {
        "timestamp": 1768980036
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
        "timestamp": 1768980479
      },
      "temperature": {
        "timestamp": 1768980479
      },
      "temperatureLast": {
        "timestamp": 1768980479
      },
      "learnedMinTemp": {
        "timestamp": 1768979786
      },
      "learnedMaxTemp": {
        "timestamp": 1768964735
      },
      "temperatureGoal": {
        "timestamp": 1768980479
      }
    }
  },
  "version": 6961,
  "timestamp": 1768980667
}
2026-01-20 23:31:07.960 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Successfully fetched shadow for device 101046568
2026-01-20 23:31:07.961 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetched 1 device shadows
2026-01-20 23:31:07.961 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Finished fetching moen_smart_water data in 0.149 seconds (success: True)
2026-01-20 23:31:07.961 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Raw state data for device 101046568: {'firmwareVersion': 'v1.1.8c', 'wifiNetwork': 'temp', 'connected': True, 'lastConnect': 1768964307943, 'wifiRssi': -77, 'wifiNoPoll': False, 'state': 'idle', 'flowCalSrc': 'factory', 'assemblyAirTemp': 16, 'isFreezing': False, 'beeperVolume': 0, 'sensorDisable': 0, 'freezeEnable': False, 'defaultFlowRate': 30, 'maxFlowRate': 100, 'trickleFlowRate': 10, 'purgeTimeout': 120, 'handleTimeout': 300, 'sensorTimeout': 300, 'voiceTimeout': 300, 'dispenseActivateTimeout': 120, 'safetyLimitTemp': 48.889999, 'safetyModeEnabled': True, 'childLimitTemp': 40.560001, 'childModeEnabled': False, 'defaultTemp': 'equal', 'handleReverse': False, 'gestureMode': 'na', 'setpointColdTemp': 0, 'setpointWarmTemp': 40.556, 'setpointHotTemp': 100, 'lowFlowRate': 127, 'unwinterizeTimeout': 60, 'healthProtectTimeout': 120, 'sensorConfig': 'gesture_handle', 'handleFW': 'v0.6.23b', 'latchFW': 'v0.6.8a', 'sensorCommError': False, 'handleCommError': False, 'batteryLifeRemaining': -1, 'batteryPercentage': 100, 'batterySavingLevel': 'normal', 'powerSource': 'battery', 'volume': 3053009, 'temperature': 34.803001, 'temperatureLast': 46.812, 'learnedMinTemp': 12.546, 'learnedMaxTemp': 53.959, 'temperatureGoal': 'hottest'}
2026-01-20 23:31:07.961 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Parsed values - device_state=idle, flow_rate=None, temperature=34.803001°C (94.6°F)
2026-01-20 23:31:07.961 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Using API data, is_valve_open=False
2026-01-20 23:31:07.961 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Setting to CLOSED
2026-01-20 23:31:07.961 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Updated state to closed, position=0
2026-01-20 23:31:08.538 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Updating device shadow for 101046568
2026-01-20 23:31:08.538 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:08.538 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update request payload: {
  "parse": false,
  "fn": "smartwater-app-shadow-api-prod-update",
  "escape": false,
  "body": {
    "payload": {
      "commandSrc": "app",
      "command": "run",
      "temperature": "hottest",
      "flowRate": 100
    },
    "locale": "en_US",
    "clientId": "101046568"
  }
}
2026-01-20 23:31:08.704 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update response status: 200
2026-01-20 23:31:08.705 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"status\":true}}"
}
2026-01-20 23:31:08.705 INFO (SyncWorker_2) [custom_components.moen_smart_water.api] Updated device shadow for 101046568
2026-01-20 23:31:08.705 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update parsed result: {
  "status": true
}
2026-01-20 23:31:08.705 INFO (MainThread) [custom_components.moen_smart_water.number] Set temperature to hottest (54.0°C) for device 101046568
2026-01-20 23:31:12.455 INFO (MainThread) [custom_components.moen_smart_water.valve] Setting valve position to 100% for device 101046568
2026-01-20 23:31:12.455 INFO (MainThread) [custom_components.moen_smart_water.valve] Starting water flow with coldest temperature and 100% flow rate
2026-01-20 23:31:12.455 DEBUG (SyncWorker_5) [custom_components.moen_smart_water.api] Updating device shadow for 101046568
2026-01-20 23:31:12.455 DEBUG (SyncWorker_5) [custom_components.moen_smart_water.api] Update request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:12.455 DEBUG (SyncWorker_5) [custom_components.moen_smart_water.api] Update request payload: {
  "parse": false,
  "fn": "smartwater-app-shadow-api-prod-update",
  "escape": false,
  "body": {
    "payload": {
      "commandSrc": "app",
      "command": "run",
      "temperature": "coldest",
      "flowRate": 100
    },
    "locale": "en_US",
    "clientId": "101046568"
  }
}
2026-01-20 23:31:12.725 DEBUG (SyncWorker_5) [custom_components.moen_smart_water.api] Update response status: 200
2026-01-20 23:31:12.725 DEBUG (SyncWorker_5) [custom_components.moen_smart_water.api] Update full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"status\":true}}"
}
2026-01-20 23:31:12.725 INFO (SyncWorker_5) [custom_components.moen_smart_water.api] Updated device shadow for 101046568
2026-01-20 23:31:12.725 DEBUG (SyncWorker_5) [custom_components.moen_smart_water.api] Update parsed result: {
  "status": true
}
2026-01-20 23:31:12.725 DEBUG (MainThread) [custom_components.moen_smart_water.valve] DELAYED CHECK: Waiting 3 seconds for API to update...
2026-01-20 23:31:15.728 DEBUG (MainThread) [custom_components.moen_smart_water.valve] DELAYED CHECK: Checking API after delay
2026-01-20 23:31:15.728 DEBUG (MainThread) [custom_components.moen_smart_water.valve] MANUAL UPDATE: Getting fresh API data
2026-01-20 23:31:15.728 DEBUG (SyncWorker_7) [custom_components.moen_smart_water.api] Getting device shadow for 101046568
2026-01-20 23:31:15.728 DEBUG (SyncWorker_7) [custom_components.moen_smart_water.api] Shadow request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:15.728 DEBUG (SyncWorker_7) [custom_components.moen_smart_water.api] Shadow request payload: {'parse': False, 'fn': 'smartwater-app-shadow-api-prod-get', 'escape': False, 'body': {'clientId': '101046568', 'shadow': True, 'locale': 'en_US'}}
2026-01-20 23:31:15.867 DEBUG (SyncWorker_7) [custom_components.moen_smart_water.api] Shadow response status: 200
2026-01-20 23:31:15.867 DEBUG (SyncWorker_7) [custom_components.moen_smart_water.api] Shadow full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"state\":{\"desired\":{\"deviceLost\":true,\"dispenseActivateTimeout\":120,\"handleTimeout\":300,\"freezeEnable\":false,\"sensorTimeout\":300,\"voiceTimeout\":300},\"reported\":{\"firmwareVersion\":\"v1.1.8c\",\"wifiNetwork\":\"temp\",\"connected\":true,\"lastConnect\":1768964307943,\"wifiRssi\":-77,\"wifiNoPoll\":false,\"state\":\"running\",\"flowCalSrc\":\"factory\",\"assemblyAirTemp\":16,\"isFreezing\":false,\"beeperVolume\":0,\"sensorDisable\":0,\"freezeEnable\":false,\"defaultFlowRate\":30,\"maxFlowRate\":100,\"trickleFlowRate\":10,\"purgeTimeout\":120,\"handleTimeout\":300,\"sensorTimeout\":300,\"voiceTimeout\":300,\"dispenseActivateTimeout\":120,\"safetyLimitTemp\":48.889999,\"safetyModeEnabled\":true,\"childLimitTemp\":40.560001,\"childModeEnabled\":false,\"defaultTemp\":\"equal\",\"handleReverse\":false,\"gestureMode\":\"na\",\"setpointColdTemp\":0,\"setpointWarmTemp\":40.556,\"setpointHotTemp\":100,\"lowFlowRate\":127,\"unwinterizeTimeout\":60,\"healthProtectTimeout\":120,\"sensorConfig\":\"gesture_handle\",\"handleFW\":\"v0.6.23b\",\"latchFW\":\"v0.6.8a\",\"sensorCommError\":false,\"handleCommError\":false,\"batteryLifeRemaining\":-1,\"batteryPercentage\":100,\"batterySavingLevel\":\"normal\",\"powerSource\":\"battery\",\"volume\":3053009,\"temperature\":34.803001,\"temperatureLast\":46.812,\"learnedMinTemp\":12.546,\"learnedMaxTemp\":53.959,\"temperatureGoal\":\"hottest\"},\"delta\":{\"deviceLost\":true}},\"metadata\":{\"desired\":{\"deviceLost\":{\"timestamp\":1767074340},\"dispenseActivateTimeout\":{\"timestamp\":1768977075},\"handleTimeout\":{\"timestamp\":1768977075},\"freezeEnable\":{\"timestamp\":1768977075},\"sensorTimeout\":{\"timestamp\":1768977075},\"voiceTimeout\":{\"timestamp\":1768977075}},\"reported\":{\"firmwareVersion\":{\"timestamp\":1768964310},\"wifiNetwork\":{\"timestamp\":1768964310},\"connected\":{\"timestamp\":1768964310},\"lastConnect\":{\"timestamp\":1768964310},\"wifiRssi\":{\"timestamp\":1768964310},\"wifiNoPoll\":{\"timestamp\":1768964310},\"state\":{\"timestamp\":1768980668},\"flowCalSrc\":{\"timestamp\":1768964310},\"assemblyAirTemp\":{\"timestamp\":1768980036},\"isFreezing\":{\"timestamp\":1768964310},\"beeperVolume\":{\"timestamp\":1768964310},\"sensorDisable\":{\"timestamp\":1768964310},\"freezeEnable\":{\"timestamp\":1768964310},\"defaultFlowRate\":{\"timestamp\":1768978218},\"maxFlowRate\":{\"timestamp\":1768964310},\"trickleFlowRate\":{\"timestamp\":1768964310},\"purgeTimeout\":{\"timestamp\":1768964310},\"handleTimeout\":{\"timestamp\":1768964310},\"sensorTimeout\":{\"timestamp\":1768964310},\"voiceTimeout\":{\"timestamp\":1768964310},\"dispenseActivateTimeout\":{\"timestamp\":1768964310},\"safetyLimitTemp\":{\"timestamp\":1768964310},\"safetyModeEnabled\":{\"timestamp\":1768964310},\"childLimitTemp\":{\"timestamp\":1768964310},\"childModeEnabled\":{\"timestamp\":1768964310},\"defaultTemp\":{\"timestamp\":1768972077},\"handleReverse\":{\"timestamp\":1768964310},\"gestureMode\":{\"timestamp\":1768964310},\"setpointColdTemp\":{\"timestamp\":1768964310},\"setpointWarmTemp\":{\"timestamp\":1768964310},\"setpointHotTemp\":{\"timestamp\":1768964310},\"lowFlowRate\":{\"timestamp\":1768964310},\"unwinterizeTimeout\":{\"timestamp\":1768964310},\"healthProtectTimeout\":{\"timestamp\":1768964310},\"sensorConfig\":{\"timestamp\":1768964310},\"handleFW\":{\"timestamp\":1768964310},\"latchFW\":{\"timestamp\":1768964310},\"sensorCommError\":{\"timestamp\":1768964310},\"handleCommError\":{\"timestamp\":1768964310},\"batteryLifeRemaining\":{\"timestamp\":1768964310},\"batteryPercentage\":{\"timestamp\":1768964310},\"batterySavingLevel\":{\"timestamp\":1768964310},\"powerSource\":{\"timestamp\":1768964310},\"volume\":{\"timestamp\":1768980479},\"temperature\":{\"timestamp\":1768980479},\"temperatureLast\":{\"timestamp\":1768980479},\"learnedMinTemp\":{\"timestamp\":1768979786},\"learnedMaxTemp\":{\"timestamp\":1768964735},\"temperatureGoal\":{\"timestamp\":1768980479}}},\"version\":6966,\"timestamp\":1768980675}}"
}
2026-01-20 23:31:15.867 INFO (SyncWorker_7) [custom_components.moen_smart_water.api] Retrieved device shadow for 101046568
2026-01-20 23:31:15.867 DEBUG (SyncWorker_7) [custom_components.moen_smart_water.api] Shadow parsed data: {
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
      "state": "running",
      "flowCalSrc": "factory",
      "assemblyAirTemp": 16,
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
      "volume": 3053009,
      "temperature": 34.803001,
      "temperatureLast": 46.812,
      "learnedMinTemp": 12.546,
      "learnedMaxTemp": 53.959,
      "temperatureGoal": "hottest"
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
        "timestamp": 1768980668
      },
      "flowCalSrc": {
        "timestamp": 1768964310
      },
      "assemblyAirTemp": {
        "timestamp": 1768980036
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
        "timestamp": 1768980479
      },
      "temperature": {
        "timestamp": 1768980479
      },
      "temperatureLast": {
        "timestamp": 1768980479
      },
      "learnedMinTemp": {
        "timestamp": 1768979786
      },
      "learnedMaxTemp": {
        "timestamp": 1768964735
      },
      "temperatureGoal": {
        "timestamp": 1768980479
      }
    }
  },
  "version": 6966,
  "timestamp": 1768980675
}
2026-01-20 23:31:15.867 DEBUG (MainThread) [custom_components.moen_smart_water.valve] MANUAL UPDATE: Raw state data for device 101046568: {'firmwareVersion': 'v1.1.8c', 'wifiNetwork': 'temp', 'connected': True, 'lastConnect': 1768964307943, 'wifiRssi': -77, 'wifiNoPoll': False, 'state': 'running', 'flowCalSrc': 'factory', 'assemblyAirTemp': 16, 'isFreezing': False, 'beeperVolume': 0, 'sensorDisable': 0, 'freezeEnable': False, 'defaultFlowRate': 30, 'maxFlowRate': 100, 'trickleFlowRate': 10, 'purgeTimeout': 120, 'handleTimeout': 300, 'sensorTimeout': 300, 'voiceTimeout': 300, 'dispenseActivateTimeout': 120, 'safetyLimitTemp': 48.889999, 'safetyModeEnabled': True, 'childLimitTemp': 40.560001, 'childModeEnabled': False, 'defaultTemp': 'equal', 'handleReverse': False, 'gestureMode': 'na', 'setpointColdTemp': 0, 'setpointWarmTemp': 40.556, 'setpointHotTemp': 100, 'lowFlowRate': 127, 'unwinterizeTimeout': 60, 'healthProtectTimeout': 120, 'sensorConfig': 'gesture_handle', 'handleFW': 'v0.6.23b', 'latchFW': 'v0.6.8a', 'sensorCommError': False, 'handleCommError': False, 'batteryLifeRemaining': -1, 'batteryPercentage': 100, 'batterySavingLevel': 'normal', 'powerSource': 'battery', 'volume': 3053009, 'temperature': 34.803001, 'temperatureLast': 46.812, 'learnedMinTemp': 12.546, 'learnedMaxTemp': 53.959, 'temperatureGoal': 'hottest'}
2026-01-20 23:31:15.867 DEBUG (MainThread) [custom_components.moen_smart_water.valve] MANUAL UPDATE: Parsed values - device_state=running, flow_rate=None, temperature=34.803001°C (94.6°F)
2026-01-20 23:31:15.867 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Using API data, is_valve_open=True
2026-01-20 23:31:15.867 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Setting to OPEN
2026-01-20 23:31:15.867 DEBUG (MainThread) [custom_components.moen_smart_water.valve] Using last commanded flow rate: 100%
2026-01-20 23:31:15.867 DEBUG (MainThread) [custom_components.moen_smart_water.valve] MANUAL UPDATE: Updated state to open, position=100
2026-01-20 23:31:15.867 INFO (MainThread) [custom_components.moen_smart_water.valve] Successfully started water flow with 100% flow rate for device 101046568
2026-01-20 23:31:17.554 INFO (MainThread) [custom_components.moen_smart_water.valve] Setting valve position to 10% for device 101046568
2026-01-20 23:31:17.554 INFO (MainThread) [custom_components.moen_smart_water.valve] Starting water flow with coldest temperature and 10% flow rate
2026-01-20 23:31:17.555 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Updating device shadow for 101046568
2026-01-20 23:31:17.555 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Update request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:17.555 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Update request payload: {
  "parse": false,
  "fn": "smartwater-app-shadow-api-prod-update",
  "escape": false,
  "body": {
    "payload": {
      "commandSrc": "app",
      "command": "run",
      "temperature": "coldest",
      "flowRate": 10
    },
    "locale": "en_US",
    "clientId": "101046568"
  }
}
2026-01-20 23:31:17.730 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Update response status: 200
2026-01-20 23:31:17.731 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Update full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"status\":true}}"
}
2026-01-20 23:31:17.731 INFO (SyncWorker_4) [custom_components.moen_smart_water.api] Updated device shadow for 101046568
2026-01-20 23:31:17.731 DEBUG (SyncWorker_4) [custom_components.moen_smart_water.api] Update parsed result: {
  "status": true
}
2026-01-20 23:31:17.731 DEBUG (MainThread) [custom_components.moen_smart_water.valve] DELAYED CHECK: Waiting 3 seconds for API to update...
2026-01-20 23:31:17.962 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Starting coordinator data update
2026-01-20 23:31:17.962 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Coordinator received 1 devices
2026-01-20 23:31:17.963 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadows for 1 devices
2026-01-20 23:31:17.963 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadow for device 101046568
2026-01-20 23:31:17.964 DEBUG (SyncWorker_3) [custom_components.moen_smart_water.api] Getting device shadow for 101046568
2026-01-20 23:31:17.964 DEBUG (SyncWorker_3) [custom_components.moen_smart_water.api] Shadow request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:17.964 DEBUG (SyncWorker_3) [custom_components.moen_smart_water.api] Shadow request payload: {'parse': False, 'fn': 'smartwater-app-shadow-api-prod-get', 'escape': False, 'body': {'clientId': '101046568', 'shadow': True, 'locale': 'en_US'}}
2026-01-20 23:31:18.111 DEBUG (SyncWorker_3) [custom_components.moen_smart_water.api] Shadow response status: 200
2026-01-20 23:31:18.111 DEBUG (SyncWorker_3) [custom_components.moen_smart_water.api] Shadow full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"state\":{\"desired\":{\"deviceLost\":true,\"dispenseActivateTimeout\":120,\"handleTimeout\":300,\"freezeEnable\":false,\"sensorTimeout\":300,\"voiceTimeout\":300,\"commandSrc\":\"app\",\"command\":\"run\",\"temperature\":\"coldest\",\"flowRate\":10},\"reported\":{\"firmwareVersion\":\"v1.1.8c\",\"wifiNetwork\":\"temp\",\"connected\":true,\"lastConnect\":1768964307943,\"wifiRssi\":-77,\"wifiNoPoll\":false,\"state\":\"running\",\"flowCalSrc\":\"factory\",\"assemblyAirTemp\":16,\"isFreezing\":false,\"beeperVolume\":0,\"sensorDisable\":0,\"freezeEnable\":false,\"defaultFlowRate\":30,\"maxFlowRate\":100,\"trickleFlowRate\":10,\"purgeTimeout\":120,\"handleTimeout\":300,\"sensorTimeout\":300,\"voiceTimeout\":300,\"dispenseActivateTimeout\":120,\"safetyLimitTemp\":48.889999,\"safetyModeEnabled\":true,\"childLimitTemp\":40.560001,\"childModeEnabled\":false,\"defaultTemp\":\"equal\",\"handleReverse\":false,\"gestureMode\":\"na\",\"setpointColdTemp\":0,\"setpointWarmTemp\":40.556,\"setpointHotTemp\":100,\"lowFlowRate\":127,\"unwinterizeTimeout\":60,\"healthProtectTimeout\":120,\"sensorConfig\":\"gesture_handle\",\"handleFW\":\"v0.6.23b\",\"latchFW\":\"v0.6.8a\",\"sensorCommError\":false,\"handleCommError\":false,\"batteryLifeRemaining\":-1,\"batteryPercentage\":100,\"batterySavingLevel\":\"normal\",\"powerSource\":\"battery\",\"volume\":3053009,\"temperature\":34.803001,\"temperatureLast\":46.812,\"learnedMinTemp\":12.546,\"learnedMaxTemp\":53.959,\"temperatureGoal\":\"hottest\"},\"delta\":{\"deviceLost\":true,\"commandSrc\":\"app\",\"command\":\"run\",\"temperature\":\"coldest\",\"flowRate\":10}},\"metadata\":{\"desired\":{\"deviceLost\":{\"timestamp\":1767074340},\"dispenseActivateTimeout\":{\"timestamp\":1768977075},\"handleTimeout\":{\"timestamp\":1768977075},\"freezeEnable\":{\"timestamp\":1768977075},\"sensorTimeout\":{\"timestamp\":1768977075},\"voiceTimeout\":{\"timestamp\":1768977075},\"commandSrc\":{\"timestamp\":1768980677},\"command\":{\"timestamp\":1768980677},\"temperature\":{\"timestamp\":1768980677},\"flowRate\":{\"timestamp\":1768980677}},\"reported\":{\"firmwareVersion\":{\"timestamp\":1768964310},\"wifiNetwork\":{\"timestamp\":1768964310},\"connected\":{\"timestamp\":1768964310},\"lastConnect\":{\"timestamp\":1768964310},\"wifiRssi\":{\"timestamp\":1768964310},\"wifiNoPoll\":{\"timestamp\":1768964310},\"state\":{\"timestamp\":1768980668},\"flowCalSrc\":{\"timestamp\":1768964310},\"assemblyAirTemp\":{\"timestamp\":1768980036},\"isFreezing\":{\"timestamp\":1768964310},\"beeperVolume\":{\"timestamp\":1768964310},\"sensorDisable\":{\"timestamp\":1768964310},\"freezeEnable\":{\"timestamp\":1768964310},\"defaultFlowRate\":{\"timestamp\":1768978218},\"maxFlowRate\":{\"timestamp\":1768964310},\"trickleFlowRate\":{\"timestamp\":1768964310},\"purgeTimeout\":{\"timestamp\":1768964310},\"handleTimeout\":{\"timestamp\":1768964310},\"sensorTimeout\":{\"timestamp\":1768964310},\"voiceTimeout\":{\"timestamp\":1768964310},\"dispenseActivateTimeout\":{\"timestamp\":1768964310},\"safetyLimitTemp\":{\"timestamp\":1768964310},\"safetyModeEnabled\":{\"timestamp\":1768964310},\"childLimitTemp\":{\"timestamp\":1768964310},\"childModeEnabled\":{\"timestamp\":1768964310},\"defaultTemp\":{\"timestamp\":1768972077},\"handleReverse\":{\"timestamp\":1768964310},\"gestureMode\":{\"timestamp\":1768964310},\"setpointColdTemp\":{\"timestamp\":1768964310},\"setpointWarmTemp\":{\"timestamp\":1768964310},\"setpointHotTemp\":{\"timestamp\":1768964310},\"lowFlowRate\":{\"timestamp\":1768964310},\"unwinterizeTimeout\":{\"timestamp\":1768964310},\"healthProtectTimeout\":{\"timestamp\":1768964310},\"sensorConfig\":{\"timestamp\":1768964310},\"handleFW\":{\"timestamp\":1768964310},\"latchFW\":{\"timestamp\":1768964310},\"sensorCommError\":{\"timestamp\":1768964310},\"handleCommError\":{\"timestamp\":1768964310},\"batteryLifeRemaining\":{\"timestamp\":1768964310},\"batteryPercentage\":{\"timestamp\":1768964310},\"batterySavingLevel\":{\"timestamp\":1768964310},\"powerSource\":{\"timestamp\":1768964310},\"volume\":{\"timestamp\":1768980479},\"temperature\":{\"timestamp\":1768980479},\"temperatureLast\":{\"timestamp\":1768980479},\"learnedMinTemp\":{\"timestamp\":1768979786},\"learnedMaxTemp\":{\"timestamp\":1768964735},\"temperatureGoal\":{\"timestamp\":1768980479}}},\"version\":6967,\"timestamp\":1768980678}}"
}
2026-01-20 23:31:18.112 INFO (SyncWorker_3) [custom_components.moen_smart_water.api] Retrieved device shadow for 101046568
2026-01-20 23:31:18.112 DEBUG (SyncWorker_3) [custom_components.moen_smart_water.api] Shadow parsed data: {
  "state": {
    "desired": {
      "deviceLost": true,
      "dispenseActivateTimeout": 120,
      "handleTimeout": 300,
      "freezeEnable": false,
      "sensorTimeout": 300,
      "voiceTimeout": 300,
      "commandSrc": "app",
      "command": "run",
      "temperature": "coldest",
      "flowRate": 10
    },
    "reported": {
      "firmwareVersion": "v1.1.8c",
      "wifiNetwork": "temp",
      "connected": true,
      "lastConnect": 1768964307943,
      "wifiRssi": -77,
      "wifiNoPoll": false,
      "state": "running",
      "flowCalSrc": "factory",
      "assemblyAirTemp": 16,
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
      "volume": 3053009,
      "temperature": 34.803001,
      "temperatureLast": 46.812,
      "learnedMinTemp": 12.546,
      "learnedMaxTemp": 53.959,
      "temperatureGoal": "hottest"
    },
    "delta": {
      "deviceLost": true,
      "commandSrc": "app",
      "command": "run",
      "temperature": "coldest",
      "flowRate": 10
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
      },
      "commandSrc": {
        "timestamp": 1768980677
      },
      "command": {
        "timestamp": 1768980677
      },
      "temperature": {
        "timestamp": 1768980677
      },
      "flowRate": {
        "timestamp": 1768980677
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
        "timestamp": 1768980668
      },
      "flowCalSrc": {
        "timestamp": 1768964310
      },
      "assemblyAirTemp": {
        "timestamp": 1768980036
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
        "timestamp": 1768980479
      },
      "temperature": {
        "timestamp": 1768980479
      },
      "temperatureLast": {
        "timestamp": 1768980479
      },
      "learnedMinTemp": {
        "timestamp": 1768979786
      },
      "learnedMaxTemp": {
        "timestamp": 1768964735
      },
      "temperatureGoal": {
        "timestamp": 1768980479
      }
    }
  },
  "version": 6967,
  "timestamp": 1768980678
}
2026-01-20 23:31:18.112 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Successfully fetched shadow for device 101046568
2026-01-20 23:31:18.112 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetched 1 device shadows
2026-01-20 23:31:18.112 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Finished fetching moen_smart_water data in 0.150 seconds (success: True)
2026-01-20 23:31:18.113 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Raw state data for device 101046568: {'firmwareVersion': 'v1.1.8c', 'wifiNetwork': 'temp', 'connected': True, 'lastConnect': 1768964307943, 'wifiRssi': -77, 'wifiNoPoll': False, 'state': 'running', 'flowCalSrc': 'factory', 'assemblyAirTemp': 16, 'isFreezing': False, 'beeperVolume': 0, 'sensorDisable': 0, 'freezeEnable': False, 'defaultFlowRate': 30, 'maxFlowRate': 100, 'trickleFlowRate': 10, 'purgeTimeout': 120, 'handleTimeout': 300, 'sensorTimeout': 300, 'voiceTimeout': 300, 'dispenseActivateTimeout': 120, 'safetyLimitTemp': 48.889999, 'safetyModeEnabled': True, 'childLimitTemp': 40.560001, 'childModeEnabled': False, 'defaultTemp': 'equal', 'handleReverse': False, 'gestureMode': 'na', 'setpointColdTemp': 0, 'setpointWarmTemp': 40.556, 'setpointHotTemp': 100, 'lowFlowRate': 127, 'unwinterizeTimeout': 60, 'healthProtectTimeout': 120, 'sensorConfig': 'gesture_handle', 'handleFW': 'v0.6.23b', 'latchFW': 'v0.6.8a', 'sensorCommError': False, 'handleCommError': False, 'batteryLifeRemaining': -1, 'batteryPercentage': 100, 'batterySavingLevel': 'normal', 'powerSource': 'battery', 'volume': 3053009, 'temperature': 34.803001, 'temperatureLast': 46.812, 'learnedMinTemp': 12.546, 'learnedMaxTemp': 53.959, 'temperatureGoal': 'hottest'}
2026-01-20 23:31:18.113 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Parsed values - device_state=running, flow_rate=None, temperature=34.803001°C (94.6°F)
2026-01-20 23:31:18.113 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Using API data, is_valve_open=True
2026-01-20 23:31:18.113 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Setting to OPEN
2026-01-20 23:31:18.113 DEBUG (MainThread) [custom_components.moen_smart_water.valve] Using last commanded flow rate: 10%
2026-01-20 23:31:18.113 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Updated state to open, position=10
2026-01-20 23:31:20.733 DEBUG (MainThread) [custom_components.moen_smart_water.valve] DELAYED CHECK: Checking API after delay
2026-01-20 23:31:20.733 DEBUG (MainThread) [custom_components.moen_smart_water.valve] MANUAL UPDATE: Getting fresh API data
2026-01-20 23:31:20.733 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Getting device shadow for 101046568
2026-01-20 23:31:20.733 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:20.733 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow request payload: {'parse': False, 'fn': 'smartwater-app-shadow-api-prod-get', 'escape': False, 'body': {'clientId': '101046568', 'shadow': True, 'locale': 'en_US'}}
2026-01-20 23:31:20.882 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow response status: 200
2026-01-20 23:31:20.882 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"state\":{\"desired\":{\"deviceLost\":true,\"dispenseActivateTimeout\":120,\"handleTimeout\":300,\"freezeEnable\":false,\"sensorTimeout\":300,\"voiceTimeout\":300,\"commandSrc\":\"app\",\"command\":\"run\",\"temperature\":\"coldest\",\"flowRate\":10},\"reported\":{\"firmwareVersion\":\"v1.1.8c\",\"wifiNetwork\":\"temp\",\"connected\":true,\"lastConnect\":1768964307943,\"wifiRssi\":-77,\"wifiNoPoll\":false,\"state\":\"running\",\"flowCalSrc\":\"factory\",\"assemblyAirTemp\":16,\"isFreezing\":false,\"beeperVolume\":0,\"sensorDisable\":0,\"freezeEnable\":false,\"defaultFlowRate\":30,\"maxFlowRate\":100,\"trickleFlowRate\":10,\"purgeTimeout\":120,\"handleTimeout\":300,\"sensorTimeout\":300,\"voiceTimeout\":300,\"dispenseActivateTimeout\":120,\"safetyLimitTemp\":48.889999,\"safetyModeEnabled\":true,\"childLimitTemp\":40.560001,\"childModeEnabled\":false,\"defaultTemp\":\"equal\",\"handleReverse\":false,\"gestureMode\":\"na\",\"setpointColdTemp\":0,\"setpointWarmTemp\":40.556,\"setpointHotTemp\":100,\"lowFlowRate\":127,\"unwinterizeTimeout\":60,\"healthProtectTimeout\":120,\"sensorConfig\":\"gesture_handle\",\"handleFW\":\"v0.6.23b\",\"latchFW\":\"v0.6.8a\",\"sensorCommError\":false,\"handleCommError\":false,\"batteryLifeRemaining\":-1,\"batteryPercentage\":100,\"batterySavingLevel\":\"normal\",\"powerSource\":\"battery\",\"volume\":3053009,\"temperature\":34.803001,\"temperatureLast\":46.812,\"learnedMinTemp\":12.546,\"learnedMaxTemp\":53.959,\"temperatureGoal\":\"hottest\"},\"delta\":{\"deviceLost\":true,\"commandSrc\":\"app\",\"command\":\"run\",\"temperature\":\"coldest\",\"flowRate\":10}},\"metadata\":{\"desired\":{\"deviceLost\":{\"timestamp\":1767074340},\"dispenseActivateTimeout\":{\"timestamp\":1768977075},\"handleTimeout\":{\"timestamp\":1768977075},\"freezeEnable\":{\"timestamp\":1768977075},\"sensorTimeout\":{\"timestamp\":1768977075},\"voiceTimeout\":{\"timestamp\":1768977075},\"commandSrc\":{\"timestamp\":1768980677},\"command\":{\"timestamp\":1768980677},\"temperature\":{\"timestamp\":1768980677},\"flowRate\":{\"timestamp\":1768980677}},\"reported\":{\"firmwareVersion\":{\"timestamp\":1768964310},\"wifiNetwork\":{\"timestamp\":1768964310},\"connected\":{\"timestamp\":1768964310},\"lastConnect\":{\"timestamp\":1768964310},\"wifiRssi\":{\"timestamp\":1768964310},\"wifiNoPoll\":{\"timestamp\":1768964310},\"state\":{\"timestamp\":1768980668},\"flowCalSrc\":{\"timestamp\":1768964310},\"assemblyAirTemp\":{\"timestamp\":1768980036},\"isFreezing\":{\"timestamp\":1768964310},\"beeperVolume\":{\"timestamp\":1768964310},\"sensorDisable\":{\"timestamp\":1768964310},\"freezeEnable\":{\"timestamp\":1768964310},\"defaultFlowRate\":{\"timestamp\":1768978218},\"maxFlowRate\":{\"timestamp\":1768964310},\"trickleFlowRate\":{\"timestamp\":1768964310},\"purgeTimeout\":{\"timestamp\":1768964310},\"handleTimeout\":{\"timestamp\":1768964310},\"sensorTimeout\":{\"timestamp\":1768964310},\"voiceTimeout\":{\"timestamp\":1768964310},\"dispenseActivateTimeout\":{\"timestamp\":1768964310},\"safetyLimitTemp\":{\"timestamp\":1768964310},\"safetyModeEnabled\":{\"timestamp\":1768964310},\"childLimitTemp\":{\"timestamp\":1768964310},\"childModeEnabled\":{\"timestamp\":1768964310},\"defaultTemp\":{\"timestamp\":1768972077},\"handleReverse\":{\"timestamp\":1768964310},\"gestureMode\":{\"timestamp\":1768964310},\"setpointColdTemp\":{\"timestamp\":1768964310},\"setpointWarmTemp\":{\"timestamp\":1768964310},\"setpointHotTemp\":{\"timestamp\":1768964310},\"lowFlowRate\":{\"timestamp\":1768964310},\"unwinterizeTimeout\":{\"timestamp\":1768964310},\"healthProtectTimeout\":{\"timestamp\":1768964310},\"sensorConfig\":{\"timestamp\":1768964310},\"handleFW\":{\"timestamp\":1768964310},\"latchFW\":{\"timestamp\":1768964310},\"sensorCommError\":{\"timestamp\":1768964310},\"handleCommError\":{\"timestamp\":1768964310},\"batteryLifeRemaining\":{\"timestamp\":1768964310},\"batteryPercentage\":{\"timestamp\":1768964310},\"batterySavingLevel\":{\"timestamp\":1768964310},\"powerSource\":{\"timestamp\":1768964310},\"volume\":{\"timestamp\":1768980479},\"temperature\":{\"timestamp\":1768980479},\"temperatureLast\":{\"timestamp\":1768980479},\"learnedMinTemp\":{\"timestamp\":1768979786},\"learnedMaxTemp\":{\"timestamp\":1768964735},\"temperatureGoal\":{\"timestamp\":1768980479}}},\"version\":6967,\"timestamp\":1768980680}}"
}
2026-01-20 23:31:20.882 INFO (SyncWorker_1) [custom_components.moen_smart_water.api] Retrieved device shadow for 101046568
2026-01-20 23:31:20.882 DEBUG (SyncWorker_1) [custom_components.moen_smart_water.api] Shadow parsed data: {
  "state": {
    "desired": {
      "deviceLost": true,
      "dispenseActivateTimeout": 120,
      "handleTimeout": 300,
      "freezeEnable": false,
      "sensorTimeout": 300,
      "voiceTimeout": 300,
      "commandSrc": "app",
      "command": "run",
      "temperature": "coldest",
      "flowRate": 10
    },
    "reported": {
      "firmwareVersion": "v1.1.8c",
      "wifiNetwork": "temp",
      "connected": true,
      "lastConnect": 1768964307943,
      "wifiRssi": -77,
      "wifiNoPoll": false,
      "state": "running",
      "flowCalSrc": "factory",
      "assemblyAirTemp": 16,
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
      "volume": 3053009,
      "temperature": 34.803001,
      "temperatureLast": 46.812,
      "learnedMinTemp": 12.546,
      "learnedMaxTemp": 53.959,
      "temperatureGoal": "hottest"
    },
    "delta": {
      "deviceLost": true,
      "commandSrc": "app",
      "command": "run",
      "temperature": "coldest",
      "flowRate": 10
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
      },
      "commandSrc": {
        "timestamp": 1768980677
      },
      "command": {
        "timestamp": 1768980677
      },
      "temperature": {
        "timestamp": 1768980677
      },
      "flowRate": {
        "timestamp": 1768980677
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
        "timestamp": 1768980668
      },
      "flowCalSrc": {
        "timestamp": 1768964310
      },
      "assemblyAirTemp": {
        "timestamp": 1768980036
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
        "timestamp": 1768980479
      },
      "temperature": {
        "timestamp": 1768980479
      },
      "temperatureLast": {
        "timestamp": 1768980479
      },
      "learnedMinTemp": {
        "timestamp": 1768979786
      },
      "learnedMaxTemp": {
        "timestamp": 1768964735
      },
      "temperatureGoal": {
        "timestamp": 1768980479
      }
    }
  },
  "version": 6967,
  "timestamp": 1768980680
}
2026-01-20 23:31:20.882 DEBUG (MainThread) [custom_components.moen_smart_water.valve] MANUAL UPDATE: Raw state data for device 101046568: {'firmwareVersion': 'v1.1.8c', 'wifiNetwork': 'temp', 'connected': True, 'lastConnect': 1768964307943, 'wifiRssi': -77, 'wifiNoPoll': False, 'state': 'running', 'flowCalSrc': 'factory', 'assemblyAirTemp': 16, 'isFreezing': False, 'beeperVolume': 0, 'sensorDisable': 0, 'freezeEnable': False, 'defaultFlowRate': 30, 'maxFlowRate': 100, 'trickleFlowRate': 10, 'purgeTimeout': 120, 'handleTimeout': 300, 'sensorTimeout': 300, 'voiceTimeout': 300, 'dispenseActivateTimeout': 120, 'safetyLimitTemp': 48.889999, 'safetyModeEnabled': True, 'childLimitTemp': 40.560001, 'childModeEnabled': False, 'defaultTemp': 'equal', 'handleReverse': False, 'gestureMode': 'na', 'setpointColdTemp': 0, 'setpointWarmTemp': 40.556, 'setpointHotTemp': 100, 'lowFlowRate': 127, 'unwinterizeTimeout': 60, 'healthProtectTimeout': 120, 'sensorConfig': 'gesture_handle', 'handleFW': 'v0.6.23b', 'latchFW': 'v0.6.8a', 'sensorCommError': False, 'handleCommError': False, 'batteryLifeRemaining': -1, 'batteryPercentage': 100, 'batterySavingLevel': 'normal', 'powerSource': 'battery', 'volume': 3053009, 'temperature': 34.803001, 'temperatureLast': 46.812, 'learnedMinTemp': 12.546, 'learnedMaxTemp': 53.959, 'temperatureGoal': 'hottest'}
2026-01-20 23:31:20.882 DEBUG (MainThread) [custom_components.moen_smart_water.valve] MANUAL UPDATE: Parsed values - device_state=running, flow_rate=None, temperature=34.803001°C (94.6°F)
2026-01-20 23:31:20.882 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Using API data, is_valve_open=True
2026-01-20 23:31:20.882 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Setting to OPEN
2026-01-20 23:31:20.882 DEBUG (MainThread) [custom_components.moen_smart_water.valve] Using last commanded flow rate: 10%
2026-01-20 23:31:20.882 DEBUG (MainThread) [custom_components.moen_smart_water.valve] MANUAL UPDATE: Updated state to open, position=10
2026-01-20 23:31:20.883 INFO (MainThread) [custom_components.moen_smart_water.valve] Successfully started water flow with 10% flow rate for device 101046568
2026-01-20 23:31:25.004 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Updating device shadow for 101046568
2026-01-20 23:31:25.004 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:25.005 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update request payload: {
  "parse": false,
  "fn": "smartwater-app-shadow-api-prod-update",
  "escape": false,
  "body": {
    "payload": {
      "commandSrc": "app",
      "command": "run",
      "temperature": 47.77777777777778,
      "flowRate": 100
    },
    "locale": "en_US",
    "clientId": "101046568"
  }
}
2026-01-20 23:31:25.185 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update response status: 200
2026-01-20 23:31:25.185 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"status\":true}}"
}
2026-01-20 23:31:25.185 INFO (SyncWorker_2) [custom_components.moen_smart_water.api] Updated device shadow for 101046568
2026-01-20 23:31:25.185 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Update parsed result: {
  "status": true
}
2026-01-20 23:31:25.185 INFO (MainThread) [custom_components.moen_smart_water.number] Set temperature to 47.8°C for device 101046568
2026-01-20 23:31:28.114 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Starting coordinator data update
2026-01-20 23:31:28.114 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Coordinator received 1 devices
2026-01-20 23:31:28.114 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadows for 1 devices
2026-01-20 23:31:28.115 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetching shadow for device 101046568
2026-01-20 23:31:28.115 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Getting device shadow for 101046568
2026-01-20 23:31:28.115 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow request URL: https://exo9f857n8.execute-api.us-east-2.amazonaws.com/prod/v1/invoker
2026-01-20 23:31:28.115 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow request payload: {'parse': False, 'fn': 'smartwater-app-shadow-api-prod-get', 'escape': False, 'body': {'clientId': '101046568', 'shadow': True, 'locale': 'en_US'}}
2026-01-20 23:31:28.261 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow response status: 200
2026-01-20 23:31:28.261 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow full response: {
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":{\"state\":{\"desired\":{\"deviceLost\":true,\"dispenseActivateTimeout\":120,\"handleTimeout\":300,\"freezeEnable\":false,\"sensorTimeout\":300,\"voiceTimeout\":300,\"commandSrc\":\"app\",\"command\":\"run\",\"temperature\":47.77777777777778,\"flowRate\":100},\"reported\":{\"firmwareVersion\":\"v1.1.8c\",\"wifiNetwork\":\"temp\",\"connected\":true,\"lastConnect\":1768964307943,\"wifiRssi\":-77,\"wifiNoPoll\":false,\"state\":\"running\",\"flowCalSrc\":\"factory\",\"assemblyAirTemp\":16,\"isFreezing\":false,\"beeperVolume\":0,\"sensorDisable\":0,\"freezeEnable\":false,\"defaultFlowRate\":30,\"maxFlowRate\":100,\"trickleFlowRate\":10,\"purgeTimeout\":120,\"handleTimeout\":300,\"sensorTimeout\":300,\"voiceTimeout\":300,\"dispenseActivateTimeout\":120,\"safetyLimitTemp\":48.889999,\"safetyModeEnabled\":true,\"childLimitTemp\":40.560001,\"childModeEnabled\":false,\"defaultTemp\":\"equal\",\"handleReverse\":false,\"gestureMode\":\"na\",\"setpointColdTemp\":0,\"setpointWarmTemp\":40.556,\"setpointHotTemp\":100,\"lowFlowRate\":127,\"unwinterizeTimeout\":60,\"healthProtectTimeout\":120,\"sensorConfig\":\"gesture_handle\",\"handleFW\":\"v0.6.23b\",\"latchFW\":\"v0.6.8a\",\"sensorCommError\":false,\"handleCommError\":false,\"batteryLifeRemaining\":-1,\"batteryPercentage\":100,\"batterySavingLevel\":\"normal\",\"powerSource\":\"battery\",\"volume\":3053009,\"temperature\":34.803001,\"temperatureLast\":46.812,\"learnedMinTemp\":12.546,\"learnedMaxTemp\":53.959,\"temperatureGoal\":\"hottest\"},\"delta\":{\"deviceLost\":true,\"commandSrc\":\"app\",\"command\":\"run\",\"temperature\":47.77777777777778,\"flowRate\":100}},\"metadata\":{\"desired\":{\"deviceLost\":{\"timestamp\":1767074340},\"dispenseActivateTimeout\":{\"timestamp\":1768977075},\"handleTimeout\":{\"timestamp\":1768977075},\"freezeEnable\":{\"timestamp\":1768977075},\"sensorTimeout\":{\"timestamp\":1768977075},\"voiceTimeout\":{\"timestamp\":1768977075},\"commandSrc\":{\"timestamp\":1768980685},\"command\":{\"timestamp\":1768980685},\"temperature\":{\"timestamp\":1768980685},\"flowRate\":{\"timestamp\":1768980685}},\"reported\":{\"firmwareVersion\":{\"timestamp\":1768964310},\"wifiNetwork\":{\"timestamp\":1768964310},\"connected\":{\"timestamp\":1768964310},\"lastConnect\":{\"timestamp\":1768964310},\"wifiRssi\":{\"timestamp\":1768964310},\"wifiNoPoll\":{\"timestamp\":1768964310},\"state\":{\"timestamp\":1768980668},\"flowCalSrc\":{\"timestamp\":1768964310},\"assemblyAirTemp\":{\"timestamp\":1768980036},\"isFreezing\":{\"timestamp\":1768964310},\"beeperVolume\":{\"timestamp\":1768964310},\"sensorDisable\":{\"timestamp\":1768964310},\"freezeEnable\":{\"timestamp\":1768964310},\"defaultFlowRate\":{\"timestamp\":1768978218},\"maxFlowRate\":{\"timestamp\":1768964310},\"trickleFlowRate\":{\"timestamp\":1768964310},\"purgeTimeout\":{\"timestamp\":1768964310},\"handleTimeout\":{\"timestamp\":1768964310},\"sensorTimeout\":{\"timestamp\":1768964310},\"voiceTimeout\":{\"timestamp\":1768964310},\"dispenseActivateTimeout\":{\"timestamp\":1768964310},\"safetyLimitTemp\":{\"timestamp\":1768964310},\"safetyModeEnabled\":{\"timestamp\":1768964310},\"childLimitTemp\":{\"timestamp\":1768964310},\"childModeEnabled\":{\"timestamp\":1768964310},\"defaultTemp\":{\"timestamp\":1768972077},\"handleReverse\":{\"timestamp\":1768964310},\"gestureMode\":{\"timestamp\":1768964310},\"setpointColdTemp\":{\"timestamp\":1768964310},\"setpointWarmTemp\":{\"timestamp\":1768964310},\"setpointHotTemp\":{\"timestamp\":1768964310},\"lowFlowRate\":{\"timestamp\":1768964310},\"unwinterizeTimeout\":{\"timestamp\":1768964310},\"healthProtectTimeout\":{\"timestamp\":1768964310},\"sensorConfig\":{\"timestamp\":1768964310},\"handleFW\":{\"timestamp\":1768964310},\"latchFW\":{\"timestamp\":1768964310},\"sensorCommError\":{\"timestamp\":1768964310},\"handleCommError\":{\"timestamp\":1768964310},\"batteryLifeRemaining\":{\"timestamp\":1768964310},\"batteryPercentage\":{\"timestamp\":1768964310},\"batterySavingLevel\":{\"timestamp\":1768964310},\"powerSource\":{\"timestamp\":1768964310},\"volume\":{\"timestamp\":1768980479},\"temperature\":{\"timestamp\":1768980479},\"temperatureLast\":{\"timestamp\":1768980479},\"learnedMinTemp\":{\"timestamp\":1768979786},\"learnedMaxTemp\":{\"timestamp\":1768964735},\"temperatureGoal\":{\"timestamp\":1768980479}}},\"version\":6969,\"timestamp\":1768980688}}"
}
2026-01-20 23:31:28.261 INFO (SyncWorker_2) [custom_components.moen_smart_water.api] Retrieved device shadow for 101046568
2026-01-20 23:31:28.261 DEBUG (SyncWorker_2) [custom_components.moen_smart_water.api] Shadow parsed data: {
  "state": {
    "desired": {
      "deviceLost": true,
      "dispenseActivateTimeout": 120,
      "handleTimeout": 300,
      "freezeEnable": false,
      "sensorTimeout": 300,
      "voiceTimeout": 300,
      "commandSrc": "app",
      "command": "run",
      "temperature": 47.77777777777778,
      "flowRate": 100
    },
    "reported": {
      "firmwareVersion": "v1.1.8c",
      "wifiNetwork": "temp",
      "connected": true,
      "lastConnect": 1768964307943,
      "wifiRssi": -77,
      "wifiNoPoll": false,
      "state": "running",
      "flowCalSrc": "factory",
      "assemblyAirTemp": 16,
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
      "volume": 3053009,
      "temperature": 34.803001,
      "temperatureLast": 46.812,
      "learnedMinTemp": 12.546,
      "learnedMaxTemp": 53.959,
      "temperatureGoal": "hottest"
    },
    "delta": {
      "deviceLost": true,
      "commandSrc": "app",
      "command": "run",
      "temperature": 47.77777777777778,
      "flowRate": 100
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
      },
      "commandSrc": {
        "timestamp": 1768980685
      },
      "command": {
        "timestamp": 1768980685
      },
      "temperature": {
        "timestamp": 1768980685
      },
      "flowRate": {
        "timestamp": 1768980685
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
        "timestamp": 1768980668
      },
      "flowCalSrc": {
        "timestamp": 1768964310
      },
      "assemblyAirTemp": {
        "timestamp": 1768980036
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
        "timestamp": 1768980479
      },
      "temperature": {
        "timestamp": 1768980479
      },
      "temperatureLast": {
        "timestamp": 1768980479
      },
      "learnedMinTemp": {
        "timestamp": 1768979786
      },
      "learnedMaxTemp": {
        "timestamp": 1768964735
      },
      "temperatureGoal": {
        "timestamp": 1768980479
      }
    }
  },
  "version": 6969,
  "timestamp": 1768980688
}
2026-01-20 23:31:28.264 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Successfully fetched shadow for device 101046568
2026-01-20 23:31:28.264 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Fetched 1 device shadows
2026-01-20 23:31:28.264 DEBUG (MainThread) [custom_components.moen_smart_water.coordinator] Finished fetching moen_smart_water data in 0.150 seconds (success: True)
2026-01-20 23:31:28.265 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Raw state data for device 101046568: {'firmwareVersion': 'v1.1.8c', 'wifiNetwork': 'temp', 'connected': True, 'lastConnect': 1768964307943, 'wifiRssi': -77, 'wifiNoPoll': False, 'state': 'running', 'flowCalSrc': 'factory', 'assemblyAirTemp': 16, 'isFreezing': False, 'beeperVolume': 0, 'sensorDisable': 0, 'freezeEnable': False, 'defaultFlowRate': 30, 'maxFlowRate': 100, 'trickleFlowRate': 10, 'purgeTimeout': 120, 'handleTimeout': 300, 'sensorTimeout': 300, 'voiceTimeout': 300, 'dispenseActivateTimeout': 120, 'safetyLimitTemp': 48.889999, 'safetyModeEnabled': True, 'childLimitTemp': 40.560001, 'childModeEnabled': False, 'defaultTemp': 'equal', 'handleReverse': False, 'gestureMode': 'na', 'setpointColdTemp': 0, 'setpointWarmTemp': 40.556, 'setpointHotTemp': 100, 'lowFlowRate': 127, 'unwinterizeTimeout': 60, 'healthProtectTimeout': 120, 'sensorConfig': 'gesture_handle', 'handleFW': 'v0.6.23b', 'latchFW': 'v0.6.8a', 'sensorCommError': False, 'handleCommError': False, 'batteryLifeRemaining': -1, 'batteryPercentage': 100, 'batterySavingLevel': 'normal', 'powerSource': 'battery', 'volume': 3053009, 'temperature': 34.803001, 'temperatureLast': 46.812, 'learnedMinTemp': 12.546, 'learnedMaxTemp': 53.959, 'temperatureGoal': 'hottest'}
2026-01-20 23:31:28.265 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Parsed values - device_state=running, flow_rate=None, temperature=34.803001°C (94.6°F)
2026-01-20 23:31:28.265 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Using API data, is_valve_open=True
2026-01-20 23:31:28.265 DEBUG (MainThread) [custom_components.moen_smart_water.valve] VALVE STATE: Setting to OPEN
2026-01-20 23:31:28.265 DEBUG (MainThread) [custom_components.moen_smart_water.valve] Using last commanded flow rate: 10%
2026-01-20 23:31:28.265 DEBUG (MainThread) [custom_components.moen_smart_water.valve] COORDINATOR UPDATE: Updated state to open, position=10
