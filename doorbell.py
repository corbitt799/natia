#!/usr/bin/env python3

#import needed libraries
import RPi.GPIO as GPIO
from time import sleep

#define variables to hold pin numbers
button_pin=5
buzzer_pin=16

#set warnings messages off
GPIO.setwarnings(False)

#set GPIO pin numbers to BCM
GPIO.setmode(GPIO.BCM)

#set pins as input or output and add pull up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:                                 #start while loop
        if GPIO.input(button_pin)==True:        #if button is pressed / can also be just if 'GPIO.input(button_pin)'
            GPIO.output(buzzer_pin, 1)          #set buzzer pin high/true/1
        else:                                   #if button is not pressed
            GPIO.output(buzzer_pin, 0)          #set buzzer pin low/false/0
        sleep(.5)                               #sleep for .5 seconds
except KeyboardInterrupt:
    pass
    GPIO.cleanup()
