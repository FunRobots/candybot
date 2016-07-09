#!/usr/bin/python

import wiringpi
import time
import math

#use Broadcom pin numbers
wiringpi.wiringPiSetupGpio()

# setup WiringPi PWM
SERVO_PIN = 18
PWM_DIVISOR = 384 # clock at 50kHz (20us tick)
PWM_RANGE = 1000  # range at 1000 ticks (20ms)

# setup pin as an output
wiringpi.pinMode(SERVO_PIN, 2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(PWM_DIVISOR)
wiringpi.pwmSetRange(PWM_RANGE)
wiringpi.pwmWrite(SERVO_PIN, 0) #theretically 50 (1ms) to 100 (2ms) on my servo 40-200 works ok

def set_servo_position(pos):
    """ 
    Params:
        0 - 0 degrees
        90 - 90  degrees
        180 - 180 degrees
    """
    
    move = 40 + math.floor(pos * (200 - 40) / 180)
    if move:
        print("move: ", move)
        while True:
            try:
                wiringpi.pwmWrite(18,move)
                time.sleep(0.5)
                print("wiringpi.pwmWrite(18,{})".format(pos))
            except KeyboardInterrupt:
                # clean up
                wiringpi.pwmWrite(18, 0)
                print("KeyboardInterrupt Exception")
                break
            finally:
                wiringpi.pwmWrite(18,0)
                print("Cleanup GPIO")
                break

print("Module out_servo.py have imported")



###Test display_4digits()
def test_servo(pos):
    while True:
        try:
            ### Open Candy Jar 
            set_servo_position(pos)
            print("Left")
            time.sleep(0.25)

            ### Close Candy Jar 
            servo.set_servo_position(0)
            print("Right")
            time.sleep(1)

        except KeyboardInterrupt:
            # clean up
            set_servo_position(0)
            print("KeyboardInterrupt Exception")
            break
        finally:
            set_servo_position(0)
            print("Cleanup GPIO")
            break


if __name__ == "__main__":
    test_servo(20)