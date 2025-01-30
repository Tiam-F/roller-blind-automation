import paho.mqtt.client as mqtt
from astral import LocationInfo
from astral.sun import sun
from datetime import datetime
import pytz

# MQTT Configuration
MQTT_BROKER = "192.168.1.100"  # Replace with your MQTT broker IP
MQTT_PORT = 1883
MQTT_TOPIC_BLIND = "homeassistant/cover/blind_livingroom/set"

# Location Configuration (Adjust for your location)
LATITUDE = 59.3293  # Example: Stockholm
LONGITUDE = 18.0686
TIMEZONE = "Europe/Stockholm"
SUN_THRESHOLD = 15  # Sun elevation threshold for opening/closing blinds

# Connect to MQTT broker
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def get_sun_altitude():
    """ Retrieves the current sun elevation based on location and time. """
    city = LocationInfo(latitude=LATITUDE, longitude=LONGITUDE)
    s = sun(city.observer, date=datetime.now(pytz.timezone(TIMEZONE)))
    now = datetime.now(pytz.timezone(TIMEZONE))
    
    if s["sunrise"] < now < s["sunset"]:
        altitude = (s["sunset"] - now).total_seconds() / (s["sunset"] - s["sunrise"]).total_seconds() * 90
    else:
        altitude = 0  # Nighttime
    
    return altitude

def control_blinds():
    """ Controls blinds based on the sun's elevation. """
    sun_altitude = get_sun_altitude()
    print(f"Sun Elevation: {sun_altitude:.2f}°")

    if sun_altitude > SUN_THRESHOLD:
        print("Opening blinds")
        client.publish(MQTT_TOPIC_BLIND, '{"state": "open"}')
    else:
        print("Closing blinds")
        client.publish(MQTT_TOPIC_BLIND, '{"state": "closed"}')

# Run script
if __name__ == "__main__":
    control_blinds()
    client.loop_forever()
