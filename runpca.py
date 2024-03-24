import time
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)

#0 - INDEX
#1 - MIDDLE
#2 - RING
#3 - PINKY
#4 - THUMB

# IMPORTANT
# BEFORE TESTING RUN calibrate()!!!
# The hand should open, then the four finger should close then open, and the thumb will close then open.

# If this test fails, complete the following:
# 1. Disconnect digits 0-4 and set servos 0-4 to 0.
# 2. Reconnect digits 0-3 such that the plastic connectors for 0 and 1 are parallel to the edges of their servo motors and plastic connectors for 2 and 3 are pointed slightly left of center.
# 3. Set servos 0-3 to 180. Digits 0-4 should be at the same height.
# 4. Connect digit 4 such that the plastic connector is parallel to the edges of its servo. 
# 5. Set servo 4 to 100.

# run initial calibration with disconnected digits
def calibrate():
    '''
    Confirm that the servos are calbrated correctly. 

    Hand should start open, then the four fingers should
    close and then open again. Then the thumb should close and open again.

    '''
    kit.servo[0].angle=180
    kit.servo[1].angle=180
    kit.servo[2].angle=180
    kit.servo[3].angle=180
    kit.servo[4].angle=180

    for i in range(0, 180):
        if kit.servo[0].angle>0:
            kit.servo[0].angle=180-i
            kit.servo[1].angle=180-i
            kit.servo[2].angle=180-i
            kit.servo[3].angle=180-i
        time.sleep(0.001)

    for i in range(0, 180):
        if kit.servo[0].angle<180:
            kit.servo[0].angle=i
            kit.servo[1].angle=i
            kit.servo[2].angle=i
            kit.servo[3].angle=i
        time.sleep(0.001)

    for i in range(0, 180):
        if kit.servo[4].angle>0:
            kit.servo[4].angle=180-i
        time.sleep(0.001)

    for i in range(0, 180):
        if kit.servo[4].angle<180:
            kit.servo[4].angle=i
        time.sleep(0.001)

   

# Small grasp, thumb on outside

def small_grasp_out(lag=0.005):

    '''
    Closes the hand from an open position to a small grasp with the thumb on the outside.
    Inputs:

        - lag      Smaller values close the hand faster.

    '''

    kit.servo[0].angle=180
    kit.servo[1].angle=180
    kit.servo[2].angle=180
    kit.servo[3].angle=180
    kit.servo[4].angle=180

    for i in range(0, 180):
        if kit.servo[0].angle>0:
            kit.servo[0].angle=180-i
            kit.servo[1].angle=180-i
            kit.servo[2].angle=180-i
            kit.servo[3].angle=180-i
        if kit.servo[4].angle>100:
            kit.servo[4].angle=180-i
        time.sleep(lag)

   
# Small grasp, thumb on inside

def small_grasp_in(lag=0.005):

    '''
    Closes the hand from an open position to a small grasp with the thumb on the inside.
    Inputs:

        - lag      Smaller values close the hand faster.

    '''

    kit.servo[0].angle=180
    kit.servo[1].angle=180
    kit.servo[2].angle=180
    kit.servo[3].angle=180
    kit.servo[4].angle=180

    for i in range(0, 230, 3):
        if kit.servo[3].angle>0:
            kit.servo[3].angle=180-i
            kit.servo[4].angle=180-i
        if kit.servo[3].angle<=130 and kit.servo[2].angle>50:
            kit.servo[2].angle=180+50-i
        if kit.servo[3].angle<=100 and kit.servo[1].angle>70:
            kit.servo[1].angle=180+80-i
        if kit.servo[3].angle<=90 and kit.servo[0].angle>60:
            kit.servo[0].angle=180+90-i
        time.sleep(lag)

# Point

def point(lag=0.005):

    '''
    Closes the hand from an open position to pointing with the index finger.
    Inputs:

        - lag      Smaller values close the hand faster.

    '''

    kit.servo[0].angle=180
    kit.servo[1].angle=180
    kit.servo[2].angle=180
    kit.servo[3].angle=180
    kit.servo[4].angle=180
    for i in range(0, 210):
        if kit.servo[3].angle>0:
            kit.servo[3].angle=180-i
            kit.servo[2].angle=180-i
            kit.servo[1].angle=180-i
        if kit.servo[3].angle<=150 and kit.servo[4].angle>50:
            kit.servo[4].angle=180+30-i
        time.sleep(lag)

def open(fast=True):

    '''
    Opens the hand from any position.
    Inputs:

        - fast      Smaller values close the hand faster.

    '''

    if fast==True:

        kit.servo[0].angle=180
        kit.servo[1].angle=180
        kit.servo[2].angle=180
        kit.servo[3].angle=180
        kit.servo[4].angle=180

    else:
        zero=int(kit.servo[0].angle)
        one=int(kit.servo[1].angle)
        two=int(kit.servo[2].angle)
        three=int(kit.servo[3].angle)
        four=int(kit.servo[4].angle)
        for i in range(0, 180):
            if kit.servo[3].angle<180:
                kit.servo[3].angle=three+i
            if kit.servo[2].angle<180:
                kit.servo[2].angle=two+i
            if kit.servo[1].angle<180:
                kit.servo[1].angle=one+i
            if kit.servo[4].angle<180:
                kit.servo[4].angle=four+i
            if kit.servo[0].angle<180:
               kit.servo[0].angle=zero+i
            time.sleep(0.0005)

def neutral(fast=True):

    '''
    Returns the hand to neutral position.
    Inputs:

        - fast      Smaller values close the hand faster.

    '''

    if fast==True:

        kit.servo[0].angle=180
        kit.servo[1].angle=180
        kit.servo[2].angle=180
        kit.servo[3].angle=180
        kit.servo[4].angle=100

    else:
        zero=int(kit.servo[0].angle)
        one=int(kit.servo[1].angle)
        two=int(kit.servo[2].angle)
        three=int(kit.servo[3].angle)
        four=int(kit.servo[4].angle)
        for i in range(0, 180):
            if kit.servo[3].angle<180:
                kit.servo[3].angle=three+i
            if kit.servo[2].angle<180:
                kit.servo[2].angle=two+i
            if kit.servo[1].angle<180:
                kit.servo[1].angle=one+i
            if kit.servo[4].angle<100:
                kit.servo[4].angle=four+i
            if kit.servo[0].angle<180:
               kit.servo[0].angle=zero+i
            time.sleep(0.0005)














