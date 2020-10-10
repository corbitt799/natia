#!/usr/bin/env python3

#import needed libraries
import RPi.GPIO as GPIO
from time import sleep


def arm_alarm(channel):                      #function to arm or disarm the alarm system
    print("Switch change detected")          #print function to help with troubleshooting
    global armed                             #must delare global variable armed as we intend to change the value in this function
    sleep(.25)                               #sleep a short period to allow the switch to settle before reading
    if GPIO.input(arm_pin):                  #read switch pin and if it is True, meaning switch is turned on
        armed=True                           #set the armed variable to True
    else:                                    #else if the input from the arm pin is False, meaning the setich is turned off
        armed=False                          #set the armed variable to False
    print("System armed: ", armed)           #print armed status

def sound_alarm(channel):                    #function to sound alarm
    if armed:                                #if armed then proceed otherwise go to else / no need for global as only reading variable
        print("Motion Detected")             #print function to help with troubleshooting
        GPIO.output(buzzer_pin, True)        #set buzzer pin True or on
        for x in range(10):                  #create for loop to cycle through range up to 10, LEDs will flash 10 times 
            GPIO.output(led_pin, True)       #set LED True or on
            sleep(.5)                        #sleep .5 seconds
            GPIO.output(led_pin, False)      #set LED Fasle or off
            sleep(.5)                        #sleep .5 seconds
        GPIO.output(buzzer_pin, False)       #once LED flashing is complete set buzzer pin to False or off
    else:                                    #else part of if else runs if armed is not True
        pass                                 #pass or exit the function


#define variables to hold pin numbers
motion_pin=5
buzzer_pin=16
led_pin=21
arm_pin=17

#set warnings messages off
GPIO.setwarnings(False)

#set GPIO pin numbers to BCM
GPIO.setmode(GPIO.BCM)

#set pins as input or output and add pull up resistor
GPIO.setup(motion_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(arm_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

#add event detect for door opening
GPIO.add_event_detect(motion_pin, GPIO.RISING, callback=sound_alarm, bouncetime=200)
GPIO.add_event_detect(arm_pin, GPIO.BOTH, callback=arm_alarm, bouncetime=200)

#get the initial state of the arm switch
armed=GPIO.input(arm_pin)
print("Initial armed state: ", armed)

#set LED off initially  / this can be done in the setup method
GPIO.output(led_pin, False)

try:                   #simple loop to keep script running
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
