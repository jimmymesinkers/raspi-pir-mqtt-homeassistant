# raspi-pir-mqtt-homeassistant
Simple script to read PIR sensor on Raspberry Pi and publish to MQTT, for use in HomeAssistant.

# Instructions:
* Uses Paho MQTT library
* Connect PIR sensor to 5V, GND, and GPIO 4 on the Raspberry Pi
* Edit mqtt_settings_eg.py with your MQTT details and GPIO pin etc.
* Rename mqtt_settings_eg.py as mqtt_settings.py

# Integration with Home Assistant
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

# Service
There is now a systemd service to run this.  

To set this up, edit the .service file:
```> nano raspi-pir-mqtt.service```
You have to edit the working
 directory (```WorkingDirectory```) to point to the directory containing this repository.

Save and exit.  Copy into ```/etc/systemd/system```:
```> sudo raspi-pir-mqtt.service /etc/systemd/system/raspi-pir-mqtt.service```

Now start the service:
```sudo systemctl start raspi-pir-mqtt.service```

You can enable the service to start on reboot with:
```sudo systemctl enable raspi-pir-mqtt.service```







