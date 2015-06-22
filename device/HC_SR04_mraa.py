import time
import threading

import mraa

MAX_PERIOD = 7968
TRIGGER_PULSE = 10

class HCSR04(Object):
    def __init__(self, triggerPin, echoPin):
        self.trigger = mraa.Pwm(triggerPin)
        self.echo = mraa.Gpio(echoPin)
        self.echo.dir(mraa.DIR_IN)
        self.echo.isr(
            mraa.EDGE_BOTH,
            self.ack_edge_detected,
            self.ack_edge_detected)

        self._pulse_count = 0
        self.echo_response = threading.Event()

    def get_distance(self):
        self.trigger.enable(True)
        self.trigger.period_us(MAX_PERIOD)
        self.trigger.pulsewidth_us(TRIGGER_PULSE)
        self.trigger.enable(False)

        self.echo_response.clear()
        self.echo_response.wait(100)

        return self.falling_timestamp - self.rising_timestamp

    def ack_edge_detected(self):
        self._pulse_count += 1
        if _pulse_count % 2 == 0:
            self.falling_timestamp = time.time()
            self.echo_response.set()
        else:
            self.rising_timestamp = time.time()


if __name__ == '__main__':
    my_hcsr04 = HCSR04(7,8)
    while True:
        print my_hcsr04.get_distance()
        time.sleep(1)
