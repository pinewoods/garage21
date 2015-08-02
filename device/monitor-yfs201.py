#! /usr/bin/python

import time
import datetime
import urllib
import urllib2
import json

def log_response_status(response, e = None):
    with open('/tmp/monitor.txt','w') as fp:
        r = response.getcode() if response else e
        st = datetime.datetime.fromtimestamp(
                time.time()).strftime(
                '%Y-%m-%d %H:%M:%S')
        fp.write('last:%s\nstatus: %s\n' % (str(st), str(r)))

while True:
    try:
        with open('/tmp/arduino.json','r') as fp:
            sensor_read = json.load(fp)
        url = 'http://ws.pinewoods.com.br/api'
        #url = 'http://127.0.0.1:5000/api'
        data = urllib.urlencode(sensor_read)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        log_response_status(response)

    except Exception as e:
        log_response_status(None, e)

    time.sleep(60)
