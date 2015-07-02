#!/user/bin/python
# -*- coding: utf-8 -*-

import serial

from Temperature import Temperature as temp
from DissolvedOxygen import dissolved_oxygen

tempSensor = temp()
ser = serial.Serial('/dev/ttyAMA0', 38400)
do_sensor = dissolved_oxygen(ser)

do_sensor.turnOnLED()

while True:
    do_sensor.pass_temperature(tempSensor.read_temp_celsius())

    print(tempSensor.read_temp_celsius(), tempSensor.read_temp_fahrenheit(), dissolved_oxygen.get_data(), "North Carroll")
