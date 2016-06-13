#!/usr/bin/python 

import RPi.GPIO as GPIO
import time
import random
import wiringpi
from gpiozero import Button
import gpiozero.devices
from gpiozero.pins.native import NativePin

from events_tw import checkMentionInTwitter
import out_7seg_led
import out_servo 


#use Broadcom (BCM) pin numbers
GPIO.setmode(GPIO.BCM)
gpiozero.devices.DefaultPin = NativePin


#settings for servo 
out_servo.servo_position(0)

#settigns for button
button = Button(14)


try:
    while True:

        ### Generate #code
        code = "{code}".format(code=random.randint(1000, 9999))
        print("PRINT code:", code, "\n")
  
        ### Wait for Button press
        print("Make a tweet with following: @fun_robots and #{code}  And then, press the BUTTON".format(code=code))

        ###Display code on 7seg-LED
        while button.is_pressed != True: 
            out_7seg_led.display_4digits(code)                   

        ### Check for Twitter mentions and #code
        get_candy = checkMentionInTwitter(code)

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
