#!/usr/bin/python 

import RPi.GPIO as GPIO
import time
import threading
import random
import wiringpi

from twitter_stream import listenTwitter
import led_7seg
import servo 


#use Broadcom (BCM) pin numbers
GPIO.setmode(GPIO.BCM)

#settings for servo 
servo.set_servo_position(0)

try:
    while True:

        ### Generate #code
        code = "{code}".format(code=random.randint(1000, 9999))
        print("PRINT code:", code, "\n")
  
        ### Wait for Button press
        print("Make a tweet with following: @fun_robots and #{code}".format(code=code))
        
        #Display code on 7seg-LED
        display = threading.Thread(target=led_7seg.display_4digits, args=(code,))
        display.start() 


        ### Mode 2: Listen Twitter Stream API and get a candy automaticallynani
        get_candy = listenTwitter(track='@fun_robots, #fun_robots, #funrobots.ru', code=code)
        ### Control candy dispenser servo 
        if get_candy:
            print(get_candy)
            # switch off display 
            display.display_on = False 

            ### Open Candy Jar 
            servo.set_servo_position(20)
            print("Left")
            time.sleep(0.25)

            ### Close Candy Jar 
            servo.set_servo_position(0)
            print("Right")
            time.sleep(1)
 
        else: 
            print("It seems you don't want a candy! Or, are you kidding me? ")

    print("Good bye!")

except KeyboardInterrupt:
        GPIO.cleanup()

finally:
        GPIO.cleanup()
