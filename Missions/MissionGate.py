from rumarino_package.msg import Centroid, ForwardsCommand
import rospy
from std_msgs.msg import Int32, Float32
import time
import Utils.Gate

side = 2  # 0 left point; 1 right point; other, center point

camCenterX = 640/2
camCenterY = 480/2

gate = Utils.Gate.gate()
gate.setter_centerx(-1)
gate.setter_centery(-1)
box_size = 50
box_left_edge = camCenterX-box_size
box_right_edge = camCenterX+box_size
align_interval = 5


setDepth = rospy.Publisher("depth_set_point", Float32)
forward = rospy.Publisher("forwards_command", ForwardsCommand)
align = rospy.Publisher("align_set_point", Float32)
currentAngle = rospy.wait_for_message("align_current", Float32, timeout=5)


def run_gate():  # values and Ros statements need to be adjusted
    desired_depth = 4
    current_depth = rospy.wait_for_message("depth_current", Float32, timeout=5)
    setDepth.publish(desired_depth)
    while desired_depth < current_depth:  # might cause infinite loop, waits for the AUV to submerge
        current_depth = rospy.wait_for_message("depth_current", Float32, timeout=5)
    set_center()
    see_gate()
    while gate.getter_centerx() != -1 and gate.getter_centery() != -1:
        if check_binding_box():
            move("F", 20, 2)
        else:
            align_with_centroid()
        set_center()
    move("F", 20, 6)


def set_center():  # Ros statements need to be modified
    global gate
    centroid = rospy.wait_for_message("Gate_Centroid", Centroid, timeout=5)
    if side == 0:
        gate.setter_centerx(centroid.x)
        gate.setter_centery(centroid.y)
    elif side == 1:
        gate.setter_centerx(centroid.x)
        gate.setter_centery(centroid.y)
    else:
        gate.setter_centerx(centroid.x)
        gate.setter_centery(centroid.y)


def check_binding_box():
    set_center()
    if (camCenterX-box_size) < gate.getter_centerx() < (camCenterX+box_size) and (camCenterY-box_size) < gate.getter_centery() < \
            (camCenterY+box_size):
        return True
    return False


def see_gate():
    while gate.getter_centerx() is None and gate.getter_centery() is None:
        align.publish(70)
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


def align_with_centroid():
    is_aligned = False
    while not is_aligned:
        centroid = rospy.wait_for_message()
        if centroid.x < box_left_edge:
            align.publish(0-align_interval)
        elif centroid.x > box_right_edge:
            align.publish(align_interval)
        else:
            is_aligned = True
        time.sleep(2)

            
def move(direction, intensity, interval):
    if direction == "F":
        forward.publish(intensity, True)
        time.sleep(interval)
        forward.publish(0, True)
    elif direction == "L":
        align.publish(90)
        move("F", 40, 1)
        align.publish(-90)
    elif direction == "R":
        align.publish(-90)
        move("F", 40, 1)
        align.publish(90)
