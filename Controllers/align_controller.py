#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, Float32
from rumarino_package.msg import HorizontalMotors, ControllerSetup, ForwardsCommand

controller_gain = 0.5
MOTOR_CAP = 20
FORWARDS_CAP = 40
set_point = 60.0
error = 0
polarity = 1

controller_flag = False
forwards_speed = 0
moving_forwards = False

motor_message = HorizontalMotors()

def forwards_command_callback(data):
    global forwards_speed
    global moving_forwards
    forwards_speed = data.forwardsIntensity
    moving_forwards = data.movingForwards


def controller_setup_callback(data):
    global controller_flag
    global controller_gain
    global polarity

    controller_flag = data.controllerRunning
    if(data.controller_gain > 0):
        controller_gain = data.controllerGain
    
    if(data.polarity):
        polarity = 1
    else:
        polarity = 0


def align_measurement_callback(data):
    global align_current
    global controller_flag

    align_current = data.data
    if(controller_flag == True):
        run_controller(data)
    else:
        motor_pub.publish(0,0)

def align_set_point_callback(data):
    global align_set_point
    align_set_point = data.data

def run_controller(yaw):
    global error
    global controller_gain
    global forwards_speed
    global polarity
    global moving_forwards
    global motor_message
    #Calculate the error from the set point
    error = set_point-yaw.data
    
    #Get least path
    if(error > 180):
        error -= 360
    elif (error < -180):
        error += 360
    
    #Multiply by controller gain
    motor_speed = error*controller_gain
    

    #Saturation
    if(motor_speed > MOTOR_CAP):
        motor_speed = MOTOR_CAP
    elif( motor_speed < MOTOR_CAP*-1):
        motor_speed = -1*MOTOR_CAP
    


    #Assign motor speed to motor message
    if (motor_speed < MOTOR_CAP*0.90 & moving_forwards):
        motor_message.leftMotor = forwards_speed - polarity*motor_speed
        motor_message.rightMotor = forwards_speed + polarity*motor_speed
    else: 
        motor_message.leftMotor = polarity*motor_speed
        motor_message.rightMotor = polarity*motor_speed


    motor_pub.publish(motor_message)


def initialize_node():

    rospy.init_node('depth_controller')
    
    global motor_pub
    global error_pub
    global error
    
    motor_pub = rospy.Publisher('horizontal_motors', HorizontalMotors, queue_size=10)
    error_pub = rospy.Publisher('align_error', Float32, queue_size = 10)

    rospy.Subscriber('align_set_point', Float32, align_set_point_callback)
    rospy.Subscriber('align_current', Float32, align_measurement_callback)
    

    rospy.Subscriber('forwards_command', ForwardsCommand, forwards_command_callback)
    rospy.Subscriber('align_controller_setup', ControllerSetup, controller_setup_callback)
    
    
    motor_pub.publish(0,0)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Align Controller %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        error_pub.publish(error)
        rate.sleep()


if __name__ == '__main__':
    initialize_node()