import math
from Utils import Movement
angulo = math.acos(w)
w = adj/hyp

def seeGate():
    return boolean1

def seeRedStrips():
    return boolean2

def allign(d,theta):
    a=math.cos(theta)*d
    if theta < 0:
        Movement.left(a)
    elif theta > 0:
        Movement.right(a)
    else:
        Movement.forward(d)



def rotate():
    while seeGate() == False:
        """"rotate 60 degrees"""

"""def moveForward():
    while seeGate() == True and seeRedStrips()== False:
        move foward"""

def redStrips():
    while seeRedStrips == True and angulo == 90:

        """stop moving forward, move towards red side of gate."""







