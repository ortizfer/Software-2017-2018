#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, Float32, Bool

controller_flag = False
depth_set_point = 0
error = 0

FEET_TO_PWM = 6.25
FEET_TO_METERS = 3.281
MOTOR_CAP = 50


def toggle_controller_running_callback(data):
    global controller_flag
    controller_flag = data.data


def depth_measurement_callback(data):
    global current_depth
    global controller_flag

    current_depth = data.data
    if(controller_flag == True):
        run_controller(data)
    else:
        motor_pub.publish(0)


def depth_set_point_callback(data):
    global depth_set_point
    depth_set_point = data.data


def run_controller(yaw):
    global error
    error = set_point-yaw.data
    
    depth_error = (depth_set_point - current_depth)*FEET_TO_METERS
    motorSpeed = depth_error*depthError

    if(motorSpeed > MOTOR_CAP):
        motorSpeed = MOTOR_CAP
    if(motorSpeed < -1*MOTOR_CAP):
        motorSpeed = -1*MOTOR_CAP
    motor_pub.publish(int(motor_speed))


def initialize_node():

    rospy.init_node('depth_controller')
    
    global motor_pub
    global error_pub
    global error
    
    motor_pub = rospy.Publisher('vertical_motors', Int32, queue_size=10)
    error_pub = rospy.Publisher('depth_error', Int32, queue_size = 10)
    rospy.Subscriber('depth_set_point', Float32, depth_set_point_callback)
    rospy.Subscriber('depth_controller_running', Bool, toggle_controller_running_callback)
    rospy.Subscriber('current_depth', Float32, depth_measurement_callback)
    motor_pub.publish(0)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Depth Controller %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        error_pub.publish(error)
        rate.sleep()


if __name__ == '__main__':
    initialize_node()