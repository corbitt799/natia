#!/usr/bin/env python3

from time import sleep

def say_hello():
    print("Hello world from inside of a function!")


print("We're about to call the say hello function")
sleep(3)
say_hello()
sleep(3)
print("We just called the say hello function")
