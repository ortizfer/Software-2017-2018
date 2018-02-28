import math
from Utils import Movement
from Utils.Gate import Gate

camCenterX = 480/2
camCenterY = 640/2

bool1 = False #for identifying if gate is in frame

def check_binding_box(x,y):
    if (camCenterX-50) < x < (camCenterX+50) and (camCenterY-50) < y < (camCenterY+50):
        return True
    return False


def see_gate():
    if bool1:
        Movement.rotate(70)
        see_gate()


def allign():
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
