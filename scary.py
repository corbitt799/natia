#!/usr/bin/env python3

#import needed libraries
import RPi.GPIO as GPIO
from time import sleep
import os
import subprocess
import random
import datetime

def arm_trick(channel):
    global armed
    sleep(.3)
    if GPIO.input(arm_pin):
        armed=True
    else:
        armed=False
    print("Switch change detected / System armed: ", armed)

def trick(channel):
    global last_trigger_time
    time_since_last_trigger=(datetime.datetime.now()-last_trigger_time).seconds
    if armed and time_since_last_trigger >= dwell_time:
        print("Motion Detected")
        wav_file=random.choice(sound_effects)
        subprocess.Popen(['omxplayer',  wav_file], stdin=subprocess.PIPE, stdout=None, stderr=None)
        leds=[led1_pin, led2_pin]
        print(leds)
        for x in range(20):
            GPIO.output((leds[0]), 1)
            GPIO.output((leds[1]), 0)
            sleep(.25)
            leds.reverse()
        GPIO.output(leds, 0)
        last_trigger_time=datetime.datetime.now()
    else:
        pass


#define a list of wav file names
sound_effects=['sound/wolf.wav', 'sound/haunt.wav', 'sound/evil.wav', 'sound/laugh.wav']

#define variables to hold pin numbers
motion_pin=5
led1_pin=13
led2_pin=21
arm_pin=24

dwell_time=10


#set warnings messages off
GPIO.setwarnings(False)

#set GPIO pin numbers to BCM
GPIO.setmode(GPIO.BCM)

#set pins as input or output and add pull up or down resistors
GPIO.setup(motion_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(arm_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led2_pin, GPIO.OUT, initial=GPIO.LOW)

#add event detect for motion sensor and arming switch
GPIO.add_event_detect(motion_pin, GPIO.RISING, callback=trick, bouncetime=200)
GPIO.add_event_detect(arm_pin, GPIO.BOTH, callback=arm_trick, bouncetime=200)

#get initial state of arm switch
if GPIO.input(arm_pin):
    armed=True
else:
    armed=False 
print("System Armed:", armed)

#set initial last trigger time
last_trigger_time=datetime.datetime.now()

#loop
try:
    while True:
        pass
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
