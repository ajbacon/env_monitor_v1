#!/usr/bin/env python

import bme680
import time
import datetime

print("""temperature-pressure-humidity.py - Displays temperature, pressure, and humidity.

If you don't need gas readings, then you can read temperature,
pressure and humidity quickly.

Press Ctrl+C to exit

""")

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

print('Polling:')

if sensor.get_sensor_data():
    temp = sensor.data.temperature
    pres = sensor.data.pressure
    humi = sensor.data.humidity
    currentDT = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    oFile = open("/var/www/html/index.html","w")

    message = """<html>
    <head>
    <meta http-equiv="refresh" content="15">
    </head>
    <body>
    <p>Temperature = {0:.2f} degC<p>
    <p>Pressure = {1:.1f} mBar<p>
    <p>Humidity = {2:.2f} %RH<p>
    <p> <p>
    <p>Last Reading: {3}<p>
    </body>
    </html>""".format(temp, pres, humi, currentDT)

    oFile.write(message)
    oFile.close

    output = '{0:.2f} C,{1:.2f} hPa,{2:.3f} %RH'.format(
        temp,
        pres,
        humi)
    print(output)
