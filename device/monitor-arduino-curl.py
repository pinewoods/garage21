import os
import time

while True:
    with open('/tmp/arduino.txt','r') as fp:
        value = int(fp.read().strip())
        print value
    try:
        url = 'http://ws.pinewoods.com.br/api'
        #url = 'http://127.0.0.1:5000/api'
        os.system('curl --data "reading=%s" %s' % (value, url))
    except Exception as e:
        print e
    time.sleep(15)
