
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

    if code:
        s = str(code).rjust(4)
        print(s)
   
    for digit in range(4):
        for loop in range(0,7):
            print(GPIO.output(segments[loop], num[s[digit]][loop]))

