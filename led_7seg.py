import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM) # GPIO.BOARD is used here!!!
GPIO.setwarnings(False)
# GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# segments = (24,10,19,21,23,22,15,11)
segments =  (11,4,23,8,7,10,15,25)
GPIO.setup(segments, GPIO.OUT, initial=1)

# digits = (26,18,16,13)
digits = (22,27,17,24)
GPIO.setup(digits, GPIO.OUT, initial=0)

#Commode anode 7segLED specs
#          (a,b,c,d,e,f,g,dp)
num = {' ':(0,0,0,0,0,0,0,0),
    '0':(0,0,0,0,0,0,1,1),
    '1':(1,0,0,1,1,1,1,1),
    '2':(0,0,1,0,0,1,0,1),
    '3':(0,0,0,0,1,1,0,1),
    '4':(1,0,0,1,1,0,0,1),
    '5':(0,1,0,0,1,0,0,1),
    '6':(0,1,0,0,0,0,0,1),
    '7':(0,0,0,1,1,1,1,1),
    '8':(0,0,0,0,0,0,0,1),
    '9':(0,0,0,0,1,0,0,1)}

# #Commode cathode 7segLED specs
# #          (a,b,c,d,e,f,g,dp)
# num = {' ':(0,0,0,0,0,0,0,0),
#     '0':(1,1,1,1,1,1,0,0),
#     '1':(0,1,1,0,0,0,0,0),
#     '2':(1,1,0,1,1,0,0,0),
#     '3':(1,1,1,1,0,0,0,0),
#     '4':(0,1,1,0,0,1,0,0),
#     '5':(1,0,1,1,0,1,0,0),
#     '6':(1,0,1,1,1,1,0,0),
#     '7':(1,1,1,0,0,0,0,0),
#     '8':(1,1,1,1,1,1,0,0),
#     '9':(1,1,1,1,0,1,0,0)}


def display_4digits(code, display_on=True):
    """ 
    Control 7seg LED display to show #code

    Params:
        code: string of 4 digits code or 4-digit number
        display_on: boolean value on True (means  'start') or False (means 'stop') to control display
    Returns: 
        High output on appropriate 7-segment LEDs
    """

    print("Display is on: {}".format(display_on))


    t = threading.currentThread()
    while getattr(t, "display_on", True):
        if code:
            s = str(code).rjust(4)
        for digit in range(4):
            # print("Output digit on LED: {}".format(s[digit]))
            GPIO.output(segments, (num[s[digit]]))
            GPIO.output(digits[digit], 1)
            time.sleep(0.001)
            GPIO.output(digits[digit], 0)

    # #clean up GPIO to correct dispaly next digits
    # GPIO.cleanup()
    print("Stopping as you wish.") 


###Test display_4digits()
def test_display_4digits(code):
    try:
        n = 499
        while n >= 0:
            display_4digits(code)
            n -= 1
    finally:
        GPIO.cleanup()

print("Module out_7seg_led.py have imported")