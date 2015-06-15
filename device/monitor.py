import time
import requests
import pingo

board = pingo.detect.get_board()
sensor = board.pins['A0']
sensor.mode = 'ANALOG'

while True:
    #url = 'http://192.128.0.148/?reading=%d'
    #url = 'http://127.0.0.1:5000/?reading=%d'
    url = 'http://ws.pinewoods.com.br/api?reading=%d'
    try:
        #requests.post(url % sensor.value)
        requests.post(url % 666)  # Debug
    except Exception as e:
        print e
    time.sleep(15)
