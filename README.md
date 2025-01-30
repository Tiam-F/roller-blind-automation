# roller-blind-automation
automation of roller blinds


This script fetches the sun’s elevation and controls (IKEA) blinds using IKEA DIRIGERA hub and MQTT.

Requirements:

  1. Home Assistant or Zigbee2MQTT integrated with IKEA DIRIGERA.
  2. MQTT broker (e.g., Mosquitto) configured in Home Assistant.
  3. Entity ID of your blinds (e.g., cover.blind_livingroom).
  4. Python dependencies.
  Install required modules if needed:
  ```
pip install paho-mqtt astral pytz
```
