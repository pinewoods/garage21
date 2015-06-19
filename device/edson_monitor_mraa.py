import time
import requests
import mraa

pin = mraa.Aio(0)

while True:
    #url = 'http://192.128.0.148/?reading=%d'
    #url = 'http://127.0.0.1:5000/?reading=%d'
    url = 'http://ws.pinewoods.com.br/api?reading=%d'
    try:
        requests.post(url % pin.read())
        #requests.post(url % 666)  # Debug
    except Exception as e:
        print e
    time.sleep(15)
