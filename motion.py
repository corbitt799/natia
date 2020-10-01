#!/usr/bin/env python3

#import needed libraries
import RPi.GPIO as GPIO
from time import sleep


def arm_alarm(channel):
    sleep(1)
    if GPIO.input(arm_pin):
        armed=True
    else:
        armed=False

def sound_alarm(channel):
    if armed:
        GPIO.output(motion_pin, True)
        for x in range(10):
            GPIO.output(led_pin, True)
            sleep(.5)
            GPIO.output(led_pin, False)
            sleep(.5)
    else:
        pass

#define variables to hold pin numbers
motion_pin=5
buzzer_pin=16
led_pin=21
arm_pin=4

#set warnings messages off
GPIO.setwarnings(False)

#set GPIO pin numbers to BCM
GPIO.setmode(GPIO.BCM)

#set pins as input or output and add pull up resistor
GPIO.setup(motion_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(relay_pin, GPIO.OUT)

#add event detect for door opening
GPIO.add_event_detect(motion_pin, GPIO.RISING, callback=sound_alarm, bouncetime=200)
GPIO.add_event_detect(arm_pin, GPIO.BOTH, callback=arm_alarm, bouncetime=200)


try:
    while True:
        pass
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
