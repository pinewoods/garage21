import time

import pingo

board = pingo.detect.get_board()
sensor = board.pins['A0']
sensor.mode = 'ANALOG'

while True:
    print sensor.value()
    time.sleep()
