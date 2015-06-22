import time
import threading

import mraa

_pulse_count = 0
echo_response = threading.Event()
falling_timestamp = None
rising_timestamp = None

def ack_edge_detected():
    self._pulse_count += 1
    if _pulse_count % 2 == 0:
        falling_timestamp = time.time()
        echo_response.set()
    else:
        rising_timestamp = time.time()

trigger = mraa.Pwm(9)
echo = mraa.Gpio(7)
echo.dir(mraa.DIR_IN)
echo.isr(
    mraa.EDGE_BOTH,
    self.ack_edge_detected,
    self.ack_edge_detected)

trigger.enable(True)
trigger.period_us(7968)
trigger.pulsewidth_us(10)
trigger.enable(False)

echo_response.clear()
echo_response.wait(100)

print falling_timestamp - rising_timestamp