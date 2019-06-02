# raspi-pir-mqtt-homeassistant
Simple script to read PIR sensor on Raspberry Pi and publish to MQTT, for use in HomeAssistant.

Instructions:
* Uses Paho MQTT library & process managed by forever
* Connect PIR sensor to 5v, Ground, and GPIO 4 on the Raspberry Pi
* Edit mqtt_settings_eg.py with your MQTT details and GPIO pin etc.
* Rename as mqtt_settings.py

In Home Assistant, using the MQTT Binary Sensor component:
https://home-assistant.io/components/binary_sensor.mqtt/

```yaml
binary_sensor:
  - platform: mqtt
    state_topic: "CHANNEL/Motion/Switch"
    device_class: motion
    payload_on: "1"
    payload_off: "0"
    name: "Motion Sensor"
```

