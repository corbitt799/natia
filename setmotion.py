#!/usr/bin/env python3

#Short script to help tune the motion sensor
#Attach trigger of motion sensor to GPIO 5
#Attach LED to GPIO 21
#When the motion sensor triggers the LED with light and stay lit until the sensor no longer reports motion
#Use this to set timing and sensitivity

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
