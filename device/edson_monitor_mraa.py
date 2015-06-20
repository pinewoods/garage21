import time
import math

import requests

import mraa
import pyupm_i2clcd as lcd

def ratio(_value, from_min=162, from_max=299, to_min=0.0, to_max=100.0):
    return (float(_value - from_min) * (to_max - to_min) /
        (from_max - from_min) + to_min)


pin = mraa.Aio(0)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.setColor(0, 255, 128)
while True:
    #url = 'http://192.128.0.148/?reading=%d'
    #url = 'http://127.0.0.1:5000/?reading=%d'
    url = 'http://ws.pinewoods.com.br/api?reading=%d'
    reading = 0
    try:
        reading = pin.read()
        requests.post(url % reading)
        #requests.post(url % 666)  # Debug
    except Exception as e:
        print e

    myLcd.setCursor(0, 0)
    sensor = 'Sensor: %d' % reading
    myLcd.write(sensor)
    print sensor

    myLcd.setCursor(1, 0)
    #distance = 87.09576644*math.exp(-0.004870217643*reading)
    level = ratio(reading)
    myLcd.write('                ') # clean
    nivel = 'Nivel: %.2f %%' % (level)
    myLcd.write(nivel)
    print nivel

    time.sleep(10)
