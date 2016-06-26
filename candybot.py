#!/usr/bin/python 

import RPi.GPIO as GPIO
import time
import random
import wiringpi
from gpiozero import Button
import gpiozero.devices
from gpiozero.pins.native import NativePin

from twitter_api import checkMentionInTwitter
from twitter_stream import listenTwitter
import led_7seg
import servo 


#use Broadcom (BCM) pin numbers
GPIO.setmode(GPIO.BCM)
gpiozero.devices.DefaultPin = NativePin


#settings for servo 
servo.set_servo_position(0)

#settigns for button
button = Button(14)


try:
    while True:

        ### Generate #code
        code = "{code}".format(code=random.randint(1000, 9999))
        print("PRINT code:", code, "\n")
  
        ### Wait for Button press
        print("Make a tweet with following: @fun_robots and #{code}  And then, press the BUTTON".format(code=code))

        ### Mode 1: Check @fun_robots mentioned in Twitter, press Button to check
        # #Display code on 7seg-LED
        # while button.is_pressed != True: 
        #     led_7seg.display_4digits(code)                   

        # ##Check for Twitter mentions and #code
        # get_candy = checkMentionInTwitter(code)

        ### Mode 2: Listen Twitter Stream API and get a candy automatically
        get_candy = listenTwitter(track='@fun_robots', code=code)


        ### Control candy dispenser servo 
        if get_candy:
            print(get_candy)

            ### Open Candy Jar 
            out_servo.set_servo_position(180)
            print("Left")
            time.sleep(1)

            ### Close Candy Jar 
            out_servo.set_servo_position(0)
            print("Right")
            time.sleep(1)
 
        else: 
            print("It seems you don't want a candy! Or, are you kidding me? ")

    print("Good bye!")

except KeyboardInterrupt:
        GPIO.cleanup()

finally:
        GPIO.cleanup()
