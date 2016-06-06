#!/usr/bin/python 

import RPi.GPIO as GPIO
import time
import random
from events_tw import checkMentionInTwitter

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
# GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #button switch 
p=GPIO.PWM(18,50)
c_pos = 7.5
l_pos = 12.5
r_pos = 2.5
p.start(5)


try:
    while True:

        ### Generate #code
        code = "#{code}".format(code=random.randint(1000, 9999))
        # print("PRINT code:", code, "\n")

        ### Wait for Button press
        while True:
            print("Make a tweet with following: @fun_robots and {code}".format(code=code))
            try:
                mode = input("Print DONE and press Enter \n")
                if mode:
                    break
            except ValueError:
                print("Not a number")
        time.sleep(5)

        ### Check for Twitter mentions and #code
        get_candy = checkMentionInTwitter(code)
        if get_candy:
            print(get_candy)

            ### Open Candy Jar 
            p.ChangeDutyCycle(l_pos)
            print("Left")
            time.sleep(1)
            # # p.ChangeDutyCycle(c_pos)
            # # print "Center"
            # # time.sleep(1)

            ### Close Candy Jar 
            p.ChangeDutyCycle(r_pos)
            print("Right")
            time.sleep(1)

            ### Finish loop  
        else: 
            print("It seems you don't want a candy! Or, are you kidding me? ")

    print("Good bye!")

except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
        # print('KeyboardInterrupt')

#code for button switch
# input_state = GPIO.input(18)
#     if input_state == False:
#         print('Button Pressed')
#         time.sleep(0.2)