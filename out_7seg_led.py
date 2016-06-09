import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO.BOARD is used here!!!
GPIO.setwarnings(False)
# GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# segments = (24,10,19,21,23,22,15,11)
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
GPIO.setup(segments, GPIO.OUT, initial=0)
#loop below is the same as line of code above
# for segment in segments:
#     GPIO.setup(segment, GPIO.OUT)
#     GPIO.output(segment, 0)

# digits = (26,18,16,13)
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
GPIO.setup(digits, GPIO.OUT, initial=1)
#loop below is the same as line of code above
# for digit in digits:
#     GPIO.setup(digit, GPIO.OUT)
#     GPIO.output(digit, 1)

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

# #Commode katode 7segLED specs
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


def display_4digits(code):
    """ 
    Params:
        digits: string of 4 digits code or 4-digit number
    Returns: 
        High output on appropriate 7-segment LED
    """

    # try:
    #     while True:
    if code:
        s = str(code).rjust(4)
        print(s)


    # for digit in range(4):
    #     GPIO.output(segments, (num[s[digit]]))
    #     GPIO.output(digits[digit], 0)
    #     time.sleep(0.001)
    #     GPIO.output(digits[digit], 1)
   
    for digit in range(4):
        print("Output digit on LED: {}".format(s[digit]))

        GPIO.output(segments, (num[s[digit]]))
        loop below is the same as line of code above
        for loop in range(0,7):
            GPIO.output(segments[loop], num[s[digit]][loop])
            GPIO.output(digits[digit], 0)
            time.sleep(0.001)
            GPIO.output(digits[digit], 1)


                    # print("GPIO.output({}, {})".format(segments[loop], num[s[digit]][loop]))
    # except KeyboardInterrupt:
    #     GPIO.cleanup()



###Test display_4digits()
code = '9991'
try:
    n = 999
    while n >= 0:
        display_4digits(code)
        n -= 1

finally:
    GPIO.cleanup()

# try:
#     while True:
#         display_4digits(code)

# except KeyboardInterrupt:
#     GPIO.cleanup()