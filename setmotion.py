#!/usr/bin/env python3


import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.OUT)


while True:
    if GPIO.input(5):
        GPIO.output(21, 1)
    else:
        GPIO.output(21, 0)
    sleep(.1)
