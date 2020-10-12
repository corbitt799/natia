#!/usr/bin/env python3


import RPi.GPIO as GPIO
from time import sleep

def test_motion(chanel):
    print("Motion Detected")



GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.OUT)

#GPIO.add_event_detect(5, GPIO.RISING, callback=test_motion)


while True:
    if GPIO.input(5):
        GPIO.output(21, 1)
    else:
        GPIO.output(21, 0)
    sleep(.1)
