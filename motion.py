#!/usr/bin/env python3

#import needed libraries
import RPi.GPIO as GPIO
from time import sleep


def sound_alarm(channel):                #function to sound alarm
    print("Motion Detected")             #print function to help with troubleshooting
    GPIO.output(buzzer_pin, True)        #set buzzer pin True or on
    for x in range(10):                  #create for loop to cycle through range up to 10, LEDs will flash 10 times 
        GPIO.output(led_pin, True)       #set LED True or on
        sleep(.5)                        #sleep .5 seconds
        GPIO.output(led_pin, False)      #set LED Fasle or off
        sleep(.5)                        #sleep .5 seconds
    GPIO.output(buzzer_pin, False)       #once LED flashing is complete set buzzer pin to False or off


#define variables to hold pin numbers
motion_pin=5
buzzer_pin=16
led_pin=21

#set warnings messages off
GPIO.setwarnings(False)

#set GPIO pin numbers to BCM
GPIO.setmode(GPIO.BCM)

#set pins as input or output and add pull up resistor
GPIO.setup(motion_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

#add event detect for door opening
GPIO.add_event_detect(motion_pin, GPIO.RISING, callback=sound_alarm, bouncetime=200)

#set LED off initially  / this can be done in the setup method
GPIO.output(led_pin, False)

try:                   #simple loop to keep script running
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
