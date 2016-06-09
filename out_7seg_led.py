import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # GPIO.BOARD is used here!!!
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
segments = (24,10,19,21,23,22,15,11)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

digits = (26,18,16,13)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)



def display_4digits(code):
    """ 
    Params:
        digits: string of 4 digits code or 4-digit number
    Returns: 
        High output on appropriate 7-segment LED
    """

    num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}

    # try:
    #     while True:
    if code:
        s = str(code).rjust(4)
        print(s)
   
    for digit in range(4):
        print("Output digit on LED: {}".format(s[digit]))
        for loop in range(0,7):
            GPIO.output(segments[loop], num[s[digit]][loop])

                    # print("GPIO.output({}, {})".format(segments[loop], num[s[digit]][loop]))
    # except KeyboardInterrupt:
    #     GPIO.cleanup()



###Test display_4digits()
code = '4234'

try:
    while True:
        display_4digits(code)

except KeyboardInterrupt:
    GPIO.cleanup()