# roller-blind-automation
automation of roller blinds


This script fetches the sun’s elevation and controls (IKEA smart) blinds using IKEA DIRIGERA hub and MQTT.

Requirements:

  1. Home Assistant or Zigbee2MQTT integrated with IKEA DIRIGERA.
  2. MQTT broker (e.g., Mosquitto) configured in Home Assistant.
  3. Entity ID of your blinds (e.g., cover.blind_livingroom).
  4. Python dependencies.
  Install required modules if needed:
  ```
pip install paho-mqtt astral pytz
```


Files:

* Settings.py
  1. Fetches the sun’s elevation using ```astral```.
  2. If the sun is above 15°, the blinds open.
  3. If the sun is below 15°, the blinds close.
  4. Uses MQTT to send the command to Home Assistant (or Zigbee2MQTT).

* Configuration.yaml
  1. Trigger: Runs every 5 minutes.
  2. Condition: Checks sun’s elevation ```(sun.sun)```.
    * If the sun’s elevation is above 15°, the blinds open.
    * If the sun’s elevation is below 15°, the blinds close.
  3. Action: Uses ```cover.open_cover``` and ```cover.close_cover``` to control IKEA smart blinds.
