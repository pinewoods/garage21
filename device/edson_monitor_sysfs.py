import os
import time
import requests

os.system("echo 200 > /sys/class/gpio/export")
os.system("echo 232 > /sys/class/gpio/export")
os.system("echo 208 > /sys/class/gpio/export")
os.system("echo 214 > /sys/class/gpio/export")

while True:
    #url = 'http://192.128.0.148/?reading=%d'
    #url = 'http://127.0.0.1:5000/?reading=%d'
    url = 'http://ws.pinewoods.com.br/api?reading=%d'

    os.system("echo low > /sys/class/gpio/gpio214/direction")
    os.system("echo high > /sys/class/gpio/gpio200/direction")
    os.system("echo low > /sys/class/gpio/gpio232/direction")
    os.system("echo in > /sys/class/gpio/gpio208/direction")
    os.system("echo 261 > /sys/class/gpio/export 2>&1")
    os.system("echo high > /sys/class/gpio/gpio261/direction 2>&1")
    os.system("echo 1 > /sys/class/gpio/gpio261/value")
    os.system("echo high > /sys/class/gpio/gpio214/direction")

    try:
        with open(
        '/sys/bus/iio/devices/iio:device1/in_voltage0_raw', 'r') as fp:
        requests.post(url % fp.read())
        #requests.post(url % 666)  # Debug
    except Exception as e:
        print e
    time.sleep(15)
