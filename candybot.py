#!/usr/bin/python 

import RPi.GPIO as GPIO
import time
import random
from events_tw import checkMentionInTwitter
import out_7seg_led
from gpiozero_ servo import Servo

from gpiozero.pins.native import NativePin
import gpiozero.devices

print("import gpiozero.devices")
# Force the default pin implementation to be NativePin
gpiozero.devices.DefaultPin = NativePin
from gpiozero import Button, PWMOutputDevice
from gpiozero.pins.pigpiod import PiGPIOPin

print("PiGPIOPin")


GPIO.setmode(GPIO.BCM)

#settings for servo 
# GPIO.setup(18,GPIO.OUT)
# p=GPIO.PWM(18,50)
# c_pos = 7.5
# l_pos = 12.5
# r_pos = 2.5
# p.start(5)

servo = Servo(18)
serv.angle(180)

# servo = PWMOutputDevice(PiGPIOPin())
# servo.set_servo_pulsewidth(18, 0)
# Set servo on GPIO17 to 900.s (0.9ms)
# servo.set_servo(18, 900)
# Set servo on GPIO17 to 2000.s (2.0ms)
#servo.set_servo(17, 2000)

#settigns for button
button = Button(14)


try:
    while True:

        ### Generate #code
        code = "{code}".format(code=random.randint(1000, 9999))
        print("PRINT code:", code, "\n")

        
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
        while button.is_pressed != True: 
            out_7seg_led.display_4digits(code)

                        

        ### Check for Twitter mentions and #code
        get_candy = checkMentionInTwitter(code)

        ### Move servo
        if get_candy:
            print(get_candy)

            ### Open Candy Jar 
            # p.ChangeDutyCycle(l_pos) #put servo to left position
            # servo.set_servo(18, 1200)
            # servo.set_servo_pulsewidth(18, 1000)
            print("Left")
            time.sleep(1)

            # # p.ChangeDutyCycle(c_pos) #put servo to middle position
            # # print "Center"
            # # time.sleep(1)

            ### Close Candy Jar 
            # p.ChangeDutyCycle(r_pos) #put servo to right position
            # servo.set_servo(18, 2500)
            # servo.set_servo_pulsewidth(18, 2000)
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
