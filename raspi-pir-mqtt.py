import time
from signal import pause
from gpiozero import MotionSensor
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import mqtt_settings as set

# Connect to MQTT
# Read PIR sensor
# On motion: send motion payload

def mqtt_message(payload):
    publish.single(set.mqtt_channel,
      payload=payload,
      hostname=set.mqtt_hostname,
      client_id=set.client_id,
      auth=set.auth,
      port=set.mqtt_port,
      protocol=mqtt.MQTTv311)

def when_motion():
    print('Motion On')
    mqtt_message(set.motion_detected)

def when_no_motion():
    print('Motion off')
    mqtt_message(set.motion_undetected)

pir = MotionSensor(set.pir_sensor_pin, queue_len=set.queue_length)
pir.when_motion = when_motion
pir.when_no_motion = when_no_motion
pause()
