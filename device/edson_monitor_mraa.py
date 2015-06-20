import time
import requests

import mraa
import pyupm_i2clcd as lcd

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
    nivel = 'Nivel: %.2f' % (1.0/reading+0.42)
    myLcd.write(nivel)
    print nivel

    time.sleep(10)
