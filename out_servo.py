import wiringpi
import time

#use Broadcom pin numbers
wiringpi.wiringPiSetupGpio()

# setup WiringPi PWM
SERVO_PIN = 18
PWM_DIVISOR = 384
PWM_RANGE = 1000

# setup pin as an output
wiringpi.pinMode(SERVO_PIN, 2)
# wiringpi.pinMode(SERVO_PIN,2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(PWM_DIVISOR)
wiringpi.pwmSetRange(PWM_RANGE)
wiringpi.pwmWrite(SERVO_PIN, 40)

print("Module out_servo.py have imported")

def servo_position(pos):
    """ 
    Params:
        0 - 0 degrees
        1 - 90  degrees
        2 - 180 degrees
    """
    
    if pos == 0:
        while True:
            try:
                wiringpi.pwmWrite(18,40)
            except KeyboardInterrupt:
                # clean up
                wiringpi.pwmWrite(18, 40)
                print("KeyboardInterrupt Exception")
                break
            finally:
                wiringpi.pwmWrite(18,40)
                print("Cleanup GPIO")
                break
    if pos == 1:
        while True:
            try:
                wiringpi.pwmWrite(18,120)
            except KeyboardInterrupt:
                # clean up
                wiringpi.pwmWrite(18, 40)
                print("KeyboardInterrupt Exception")
                break
            finally:
                wiringpi.pwmWrite(18,40)
                print("Cleanup GPIO")
                break
    if pos == 2:
        while True:
            try:
                wiringpi.pwmWrite(18,200)
            except KeyboardInterrupt:
                # clean up
                wiringpi.pwmWrite(18, 40)
                print("KeyboardInterrupt Exception")
                break
            finally:
                wiringpi.pwmWrite(18,40)
                print("Cleanup GPIO")
                break

