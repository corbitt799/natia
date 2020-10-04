#!/usr/bin/env python3

#import needed libraries
import RPi.GPIO as GPIO
from time import sleep


def fire_missile(channel):
    if GPIO.input(door_pin):
        GPIO.output(relay_pin, False)
        sleep(2)
        GPIO.output(relay_pin, True)
    else:
        pass

#define variables to hold pin numbers
door_pin=5
relay_pin=12

#set warnings messages off
GPIO.setwarnings(False)

#set GPIO pin numbers to BCM
GPIO.setmode(GPIO.BCM)

#set pins as input or output and add pull up resistor
GPIO.setup(door_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(relay_pin, GPIO.OUT)

#set relay off initially
GPIO.output(relay_pin, True)

#add event detect for door opening
GPIO.add_event_detect(door_pin, GPIO.BOTH, callback=fire_missile, bouncetime=200)


try:
    while True:
        pass
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
