#!/usr/bin/python3

import RPI.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(led_pin, GPIO.HIGH)
sleep(10)
GPIO.output(led_pin, GPIO.LOW)
