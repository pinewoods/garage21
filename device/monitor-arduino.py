import time
import requests

while True:
    url = 'http://ws.pinewoods.com.br/api?reading=%d'
    with open('/tmp/arduino.txt','r') as fp:
    	value = int(fp.read().strip())
    	print value
    try:
        requests.post(url % value)
    except Exception as e:
        print e
    time.sleep(15)
