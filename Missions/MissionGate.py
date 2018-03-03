import math
from Utils import RosCom
from Utils.Gate import Gate

side = 2 # 0 left point; 1 right point; other, center point

camCenterX = 480/2
camCenterY = 640/2

center_x = 0
center_y = 0

def set_center():
    global center_x, center_y
    if side == 0:
        center_x = Gate.getter_center_leftx()
        center_y = Gate.getter_center_lefty()
    elif side == 1:
        center_x = Gate.getter_center_rightx()
        center_y = Gate.getter_center_righty()
    else:
        center_x = Gate.getter_centerx()
        center_y = Gate.getter_centery()

def check_binding_box():
    if (camCenterX-50) < center_x < (camCenterX+50) and (camCenterY-50) < center_y < (camCenterY+50):
        return True
    return False

def see_gate():
    while center_x is None and center_y is None:
        RosCom.addHeading(70)
        set_center()

def align(): # movement values need to be adjusted

    current_depth = RosCom.getDepth()
    if center_x < camCenterX and center_y < camCenterY:
        RosCom.Left(1)
        RosCom.setDepth(current_depth - 1)
    elif center_x < camCenterX and center_y > camCenterY:
        RosCom.Left(1)
        RosCom.setDepth(current_depth + 1)
    elif center_x > camCenterX and center_y > camCenterY:
        RosCom.Right(1)
        RosCom.setDepth(current_depth + 1)
    elif center_x > camCenterX and center_y < camCenterY:
        RosCom.Right(1)
        RosCom.setDepth(current_depth - 1)
    elif center_x == camCenterX and center_y < camCenterY:
        RosCom.setDepth(current_depth - 1)
    elif center_x == camCenterX and center_y > camCenterY:
        RosCom.setDepth(current_depth + 1)
    elif center_x < camCenterX and center_y == camCenterY:
        RosCom.Left(1)
    elif center_x > camCenterX and center_y == camCenterY:
        RosCom.Right(1)


def main():
    set_center()
    see_gate()
    check_binding_box()