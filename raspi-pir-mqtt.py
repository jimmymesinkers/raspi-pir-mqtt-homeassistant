import time
from signal import pause
from gpiozero import MotionSensor
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import mqtt_settings as settings

# Connect to MQTT
# Read PIR sensor
# On motion: send motion payload

def mqtt_message(payload):
    publish.single(settings.mqtt_channel,
      payload=payload,
      hostname=settings.mqtt_hostname,
      client_id=settings.client_id,
      auth=settings.auth,
      port=settings.mqtt_port,
      protocol=mqtt.MQTTv311)

def when_motion():
    print('Motion On')
    mqtt_message(settings.motion_detected)

def when_no_motion():
    print('Motion off')
    mqtt_message(settings.motion_undetected)

pir = MotionSensor(settings.pir_sensor_pin, queue_len=settings.queue_length)
pir.when_motion = when_motion
pir.when_no_motion = when_no_motion
pause()
