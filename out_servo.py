import wiringpi
import time

#use Broadcom pin numbers
wiringpi.wiringPiSetupGpio()

# setup WiringPi PWM
SERVO_PIN = 18
PWM_DIVISOR = 384
PWM_RANGE = 1000

# setup pin as an output
wiringpi.pinMode(SERVO_PIN, 1)
# wiringpi.pinMode(SERVO_PIN,2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(PWM_DIVISOR)
wiringpi.pwmSetRange(PWM_RANGE)
wiringpi.pwmWrite(SERVO_PIN, 40)

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
                wiringpi.pwmWrite(18, 0)
                print("exiting.")
                break
    if pos == 1:
        while True:
            try:
                wiringpi.pwmWrite(18,120)
            except KeyboardInterrupt:
                # clean up
                wiringpi.pwmWrite(18, 0)
                print("exiting.")
                break
    if pos == 2:
        while True:
            try:
                wiringpi.pwmWrite(18,200)
            except KeyboardInterrupt:
                # clean up
                wiringpi.pwmWrite(18, 0)
                print("exiting.")
                break
