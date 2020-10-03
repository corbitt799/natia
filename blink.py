#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

#set GPIO numbering / options are GPIO.BOARD or GPIO.BCM
GPIO.setmode(GPIO.BCM)
#define the pin number for the LED
led_pin = 21
#set the LED pin as an output
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        sleep(.75)
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
