import wiringpi
import time

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
    
    if pos == 0:
        print("pos == 0")
        while True:
            try:
                wiringpi.pwmWrite(18,40)
                time.sleep(1)
                print("wiringpi.pwmWrite(18,40)")
            except KeyboardInterrupt:
                # clean up
                wiringpi.pwmWrite(18, 40)
                print("KeyboardInterrupt Exception")
                break
            finally:
                wiringpi.pwmWrite(18,0)
                print("Cleanup GPIO")
                break
    if pos == 90:
        print("pos == 90")
        while True:
            try:
                wiringpi.pwmWrite(18,120)
                time.sleep(1)
                wiringpi.pwmWrite(18,40)
                time.sleep(1)
            except KeyboardInterrupt:
                # clean up
                wiringpi.pwmWrite(18, 0)
                print("KeyboardInterrupt Exception")
                break
            finally:
                wiringpi.pwmWrite(18,0)
                print("Cleanup GPIO")
                break
    if pos == 180:
        print("pos == 180")
        while True:
            try:
                wiringpi.pwmWrite(18,200)
                time.sleep(1)
                wiringpi.pwmWrite(18,40)
                time.sleep(1)
                print("wiringpi.pwmWrite(18,200)")
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