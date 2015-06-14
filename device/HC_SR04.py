#hcsr04.py

import mraa
import time
import sys

# digital output - trig
trigPin = mraa.Gpio(7)
trigPin.dir(mraa.DIR_OUT)
trigPin.write(0);

# digital input - echo
echoPin = mraa.Gpio(8)
echoPin.dir(mraa.DIR_IN)

time.sleep(0.3)
pulseOff = time.time()

trigPin.write(1)
time.sleep(0.00001)
trigPin.write(0)

while echoPin.Read() == 0:
    time.sleep(0)

    pulseOn = time.time()

    timeDifference = pulseOn - pulseOff
    Distance = timeDifference * 170145
    centimeters = Distance / 10

    print centimeters
    centimetersStr = str(centimeters)
