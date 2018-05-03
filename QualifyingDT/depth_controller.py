#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, Float32, Bool
from rumarino_package.msg import ControllerSetup


controller_flag = False
depth_set_point = 0
error = 0

controller_gain= 6.25
controller_bias = 0
depth_current = 0
FEET_TO_PWM = 6.25
FEET_TO_METERS = 3.281
MOTOR_CAP = 50
polarity = 1
MARRON = 10

def controller_setup_callback(data):
    global controller_flag
    global controller_gain
    global controller_bias
    global depth_current
    global polarity

    controller_flag = data.controllerRunning
    if(data.controllerGain > 0):
        controller_gain = data.controllerGain
    if(data.controllerBias > 0):
        controller_bias = data.controllerBias
    if(data.controllerBias == 1000):
        controller_bias = depth_current
    if(data.changePolarity):
        polarity = -1
    else:
        polarity = 1

def depth_measurement_callback(data):
    global depth_current
    global controller_flag

    depth_current = data.data
    if(controller_flag == True):
        run_controller(data)
    else:
        motor_pub.publish(0)


def depth_set_point_callback(data):
    global depth_set_point
    depth_set_point = data.data


def run_controller(depth):
    global error
    global controller_gain
    global controller_bias
    global MARRON

    error = depth_set_point - depth.data*MARRON    
    motor_speed = (error - controller_bias)*controller_gain

    if(motor_speed > MOTOR_CAP):
        motor_speed = MOTOR_CAP
    if(motor_speed < -1*MOTOR_CAP):
        motor_speed = -1*MOTOR_CAP
    
    motor_pub.publish(int(motor_speed*polarity))


def initialize_node():

    rospy.init_node('depth_controller')
    
    global motor_pub
    global error_pub
    global error
    
    motor_pub = rospy.Publisher('vertical_motors', Int32, queue_size=10)
    error_pub = rospy.Publisher('depth_error', Float32, queue_size = 10)

    rospy.Subscriber('depth_set_point', Float32, depth_set_point_callback)
    rospy.Subscriber('depth_current', Float32, depth_measurement_callback)

    rospy.Subscriber('depth_controller_setup', ControllerSetup, controller_setup_callback)
    rospy.set_param('depth_controller_bias', '29')
    rospy.set_param('depth_controller_gain', '20.51')
    
    motor_pub.publish(0)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Depth Controller %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        error_pub.publish(error)
        rate.sleep()


if __name__ == '__main__':
    initialize_node()
