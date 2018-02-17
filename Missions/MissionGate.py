import math
from Utils import Movement
from Utils.Gate import Gate

def seeGate(bool1):
    if bool1==False:
        Movement.rotate(70)
        seeGate()
"""        return False
    else:
        return True"""

def allign(d,theta):
    a=math.cos(theta)*d
    if theta < 0:
        Movement.left(a)
        Movement.forward(d)
    elif theta > 0:
        Movement.right(a)
        Movement.forward(d)
    else:
        Movement.forward(d)

def main():
 """   boolean = seeGate()
    while boolean == False:
        boolean = seeGate()"""
    seeGate()
    allign()