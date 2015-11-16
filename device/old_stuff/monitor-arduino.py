#! /usr/bin/python

import time
import datetime
import urllib
import urllib2

while True:
    try:
        with open('/tmp/arduino.txt','r') as fp:
            value = int(fp.read().strip('\0'))
            # print value
        url = 'http://ws.pinewoods.com.br/api'
        #url = 'http://127.0.0.1:5000/api'
        values = {'reading' : str(value)}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)

        with open('/tmp/monitor.txt','w') as fp:
            r = response.getcode()
            st = datetime.datetime.fromtimestamp(
                    time.time()).strftime(
                    '%Y-%m-%d %H:%M:%S')
            fp.write('last:%s\nstatus: %s\n' % (str(st), str(r)))
    except Exception as e:
        with open('/tmp/monitor.txt','w') as fp:
            st = datetime.datetime.fromtimestamp(
                time.time()).strftime(
                '%Y-%m-%d %H:%M:%S')
            fp.write('last:%s\nstatus: %s\n' % (str(st), str(e)))

    time.sleep(15)
