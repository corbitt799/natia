#!/usr/bin/env python3


import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

contact_pin=5

GPIO.setup(contact_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    status=GPIO.input(contact_pin)
    if status==GPIO.HIGH:   #GPIO.HIGH can be replaced with True or 1
        print("door open")
    else:
        print("door closed")
    print(status)
    sleep(.25)
