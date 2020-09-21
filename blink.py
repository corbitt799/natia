#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
led_pin = 16
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        sleep(.75)
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
