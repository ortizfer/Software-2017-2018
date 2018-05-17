from rumarino_package.msg import Centroid, ForwardsCommand
import rospy
from std_msgs.msg import Int32, Float32
from time import *

side = 2  # 0 left point; 1 right point; other, center point

camCenterX = 640/2
camCenterY = 480/2

gate = Gate()

setDepth = rospy.Publisher("depth_set_point", Float32)
forward = rospy.Publisher("forwards_command", ForwardsCommand)
align = rospy.Publisher("align_set_point", Float32)
currentAngle = rospy.wait_for_message("align_current", Float32)


def run_gate():  # values and Ros statements need to be adjusted
    setDepth.publish(4)
    set_center()
    see_gate()
    while gate.getter_centerx() is not None and gate.getter_centery() is not None:
        if check_binding_box():
            RosCom.Foward(2)
        else:
            align()
        set_center()
    RosCom.Foward(6)


def set_center():  # Ros statements need to be modified
    global gate
    if side == 0:
        gate.setter_centerx(RosCom.setvisual)
        gate.setter_centery(RosCom.setVisual)
    elif side == 1:
        gate.setter_centerx(RosCom.setvisual)
        gate.setter_centery(RosCom.setVisual)
    else:
        gate.setter_centerx(RosCom.setvisual)
        gate.setter_centery(RosCom.setVisual)


def check_binding_box():
    set_center()
    if (camCenterX-50) < gate.getter_centerx() < (camCenterX+50) and (camCenterY-50) < gate.getter_centery() < \
            (camCenterY+50):
        return True
    return False


def see_gate():
    while gate.getter_centerx() is None and gate.getter_centery() is None:
        RosCom.addHeading(70)
        set_center()


"""
def align():  # movement values need to be adjusted
    current_depth = RosCom.getDepth()
    set_center()
    if gate.getter_centerx() < camCenterX and gate.getter_centery() < camCenterY:
        RosCom.Left(1)
        RosCom.setDepth(current_depth - 1)
    elif gate.getter_centerx() < camCenterX and gate.getter_centery() > camCenterY:
        RosCom.Left(1)
        RosCom.setDepth(current_depth + 1)
    elif gate.getter_centerx() > camCenterX and gate.getter_centery() > camCenterY:
        RosCom.Right(1)
        RosCom.setDepth(current_depth + 1)
    elif gate.getter_centerx() > camCenterX and gate.getter_centery() < camCenterY:
        RosCom.Right(1)
        RosCom.setDepth(current_depth - 1)
    elif gate.getter_centerx() == camCenterX and gate.getter_centery() < camCenterY:
        RosCom.setDepth(current_depth - 1)
    elif gate.getter_centerx() == camCenterX and gate.getter_centery() > camCenterY:
        RosCom.setDepth(current_depth + 1)
    elif gate.getter_centerx() < camCenterX and gate.getter_centery() == camCenterY:
        RosCom.Left(1)
    elif gate.getter_centerx() > camCenterX and gate.getter_centery() == camCenterY:
        RosCom.Right(1)
 """


def move(direction, intensity, time):
    if direction == "F":
        forwardsCommand = rospy.Publisher("forwards_command", ForwardsCommand)
        forwardsCommand.publish(intensity, True)
        time.sleep(time)
        forwardsCommand.publish(0, True)
    elif direction == "L":
        align.publish(90)
        move("F", 40, 1)
        align.publish(-90)
    elif direction == "R":
        align.publish(-90)
        move("F", 40, 1)
        align.publish(90)
