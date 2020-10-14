#!/usr/bin/env python3

#import libraries
import RPi.GPIO as GPIO
from time import sleep

#set GPIO numbering / options are GPIO.BOARD or GPIO.BCM
GPIO.setmode(GPIO.BCM)

#define the pin number for the LED
led_pin = 21

#set the LED pin as an output
GPIO.setup(led_pin, GPIO.OUT)

try:                                                  #start try except 
    print("Set up complete now entering While loop")  #status print statement
    while True:                                       #start while loop 
        GPIO.output(led_pin, GPIO.HIGH)               #set LED pin on
        sleep(1)                                      #sleep 1 second
        GPIO.output(led_pin, GPIO.LOW)                #set LED pin off
        sleep(.75)                                    #sleep .75 seconds
except KeyboardInterrupt:                             #except runs if keyboard interrupt is detected
    print("Interrupt detected reset GPIO and exit")   #status print statement
    GPIO.cleanup()                                    #reset all GPIO pins
    pass                                              #exit try except
