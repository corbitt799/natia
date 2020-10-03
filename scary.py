#!/usr/bin/env python3

#import needed libraries
import RPi.GPIO as GPIO
from time import sleep
import os
import random

def arm_trick(channel):
    sleep(1)
    if GPIO.input(arm_pin):
        armed=True
    else:
        armed=False

def trick(channel):
    if armed:
        wav_file=random.choice(sound_effects)
        os.system('omxplayer ' + wav_file)
        leds=[led1_pin, led2_pin]
        for x in range(20):
            GPIO.output(leds[0], True)
            GPIO.output(leds[1], False)
            sleep(.5)
            leds=leds.reverse()
    else:
        pass


#define a list of wav file names
sound_effects=['wolf.wav', 'haunt.wav', 'evil.wav', 'laugh.wav']

#define variables to hold pin numbers
motion_pin=5
led1_pin=16
led2_pin=21
arm_pin=4

#set warnings messages off
GPIO.setwarnings(False)

#set GPIO pin numbers to BCM
GPIO.setmode(GPIO.BCM)

#set pins as input or output and add pull up or down resistors
GPIO.setup(motion_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(arm_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)

#add event detect for motion sensor and arming switch
GPIO.add_event_detect(motion_pin, GPIO.RISING, callback=trick, bouncetime=200)
GPIO.add_event_detect(arm_pin, GPIO.BOTH, callback=arm_trick, bouncetime=200)


try:
    while True:
        pass
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
