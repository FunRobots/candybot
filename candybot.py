#!/usr/bin/python 

import RPi.GPIO as GPIO
import time
import random
from events_tw import checkMentionInTwitter
import out_7seg_led

from gpiozero.pins.native import NativePin
import gpiozero.devices
# Force the default pin implementation to be NativePin
gpiozero.devices.DefaultPin = NativePin
from gpiozero import Button


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
p=GPIO.PWM(18,50)
c_pos = 7.5
l_pos = 12.5
r_pos = 2.5
p.start(5)
button = Button(14)


# #setup 7segLED
# GPIO.setwarnings(False)
# GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# segments = (24,10,19,21,23,22,15,11)
# for segment in segments:
#     GPIO.setup(segment, GPIO.OUT)
#     GPIO.output(segment, 0)
# digits = (26,18,16,13)
# for digit in digits:
#     GPIO.setup(digit, GPIO.OUT)
#     GPIO.output(digit, 1)

try:
    while True:

        ### Generate #code
        code = "{code}".format(code=random.randint(1000, 9999))
        # print("PRINT code:", code, "\n")

        
        ### Wait for Button press
        print("Make a tweet with following: @fun_robots and #{code}  And then, press the BUTTON".format(code=code))
        
        # while True:
        #     print("Make a tweet with following: @fun_robots and #{code}  And then, press the BUTTON".format(code=code))
        #     try:
        #         mode = input("Print DONE and press Enter \n")
        #         if mode:
        #             break
        #     except ValueError:
        #         print("Not a number")

        ###Display code on 7seg-LED
        while button.wait_for_press():
            out_7seg_led.display_4digits(code)            

        ### Check for Twitter mentions and #code
        get_candy = checkMentionInTwitter(code)
        if get_candy:
            print(get_candy)

            ### Open Candy Jar 
            p.ChangeDutyCycle(l_pos) #put servo to left position
            print("Left")
            time.sleep(1)

            # # p.ChangeDutyCycle(c_pos) #put servo to middle position
            # # print "Center"
            # # time.sleep(1)

            ### Close Candy Jar 
            p.ChangeDutyCycle(r_pos) #put servo to right position
            print("Right")
            time.sleep(1)

            ### Finish loop  
        else: 
            print("It seems you don't want a candy! Or, are you kidding me? ")

    print("Good bye!")

except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

finally:
        GPIO.cleanup()
