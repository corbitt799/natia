#!/usr/bin/env python3

#import needed libraries
import RPi.GPIO as GPIO
from time import sleep


def fire_missile(channel):               #define our function which is called when an event on door_pin is detected
    if GPIO.input(door_pin):             #double checking the door trigger, if True (open) then run:
        GPIO.output(relay_pin, True)     #set relay pin HIGH/True to trigger relay
        sleep(2)                         #sleep 2 seconds
        GPIO.output(relay_pin, False)    #set relay pin LOW/False to turn relay off
    else:                                #else of if test runs if door is not open
        pass                             #pass out of loop/function

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
GPIO.output(relay_pin, False)

#add event detect for door opening
GPIO.add_event_detect(door_pin, GPIO.RISING, callback=fire_missile, bouncetime=200)


try:
    while True:
        pass
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
