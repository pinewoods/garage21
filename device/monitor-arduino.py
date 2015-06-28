import time
import urllib
import urllib2

while True:
    with open('/tmp/arduino.txt','r') as fp:
        value = int(fp.read().strip('\0'))
        print value
    try:
        url = 'http://ws.pinewoods.com.br/api'
        #url = 'http://127.0.0.1:5000/api'
        values = {'reading' : str(value)}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
    except Exception as e:
        print e
    time.sleep(15)
