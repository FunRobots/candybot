#!/usr/bin/python 

import RPi.GPIO as GPIO
import time
import random
from events_tw import checkMentionInTwitter
from out_7seg_led import display_4digits
from gpiozero import Button

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
p=GPIO.PWM(12,50)
c_pos = 7.5
l_pos = 12.5
r_pos = 2.5
p.start(5)
button = Button(8)

try:
    while True:

        ### Generate #code
        code = "{code}".format(code=random.randint(1000, 9999))
        # print("PRINT code:", code, "\n")

        ###Display code on 7seg-LED
        display_4digits(code)

        ### Wait for Button press
        while True:
            print("Make a tweet with following: @fun_robots and #{code}  And then, press the BUTTON".format(code=code))
            try:
                mode = input("Print DONE and press Enter \n")
                if mode:
                    break
            except ValueError:
                print("Not a number")
        # time.sleep(5)
        button.wait_for_press()

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
