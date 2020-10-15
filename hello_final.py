#!/usr/bin/env python3

from time import sleep                                       #import sleep method from time library

def say_hello():                                             #define the say_hello function
    print("Hello, World...from inside of a function!")       #print function


print("We're about to call the say hello function")          #print function
sleep(3)                                                     #sleep for 3 seconds
say_hello()                                                  #call the say_hello function
sleep(3)                                                     #sleep for 3 seconds
print("We just called the say hello function")               #print function
