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
#by pulling button pin HIGH it will read True/1/On at rest
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)

#initially set buzzer pin off
GPIO.output(buzzer_pin, 0)

try:
    print("Press button to sound buzzer")
    while True:                                 #start while loop
        if GPIO.input(button_pin)==False:       #if button is pressed / can also be just if 'GPIO.input(button_pin)'
            GPIO.output(buzzer_pin, 1)          #set buzzer pin high/true/1
        else:                                   #if button is not pressed
            GPIO.output(buzzer_pin, 0)          #set buzzer pin low/false/0
        sleep(.25)                              #sleep for .25 seconds
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
