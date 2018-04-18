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
    forwards_speed = (data.forwardsIntensity)*FORWARDS_CAP
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
    align_set_point += data.data


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
    

    #Saturation (Cap at maximum value)
    if(motor_speed > MOTOR_CAP):
        motor_speed = MOTOR_CAP
    elif( motor_speed < MOTOR_CAP*-1):
        motor_speed = -1*MOTOR_CAP
    

    twist_speed = polarity*motor_speed
    #Assign motor speed to motor message
    #If you are turning a moderate amount, and you want to go forwards
    if (motor_speed < MOTOR_CAP*0.90 & moving_forwards):
        
        motor_message.leftMotor = forwards_speed - twist_speed
        motor_message.rightMotor = forwards_speed + twist_speed
    
    #If you are turning too much simply spin in place
    else: 
        motor_message.leftMotor = twist_speed
        motor_message.rightMotor = twist_speed


    motor_pub.publish(motor_message)


def initialize_node():

    rospy.init_node('depth_controller')
    
    global motor_pub
    global error_pub
    global error
    


    motor_pub = rospy.Publisher('horizontal_motors', HorizontalMotors, queue_size=10)
    error_pub = rospy.Publisher('align_error', Float32, queue_size = 10)

    #Received from the user, here you set the set point
    rospy.Subscriber('align_set_point', Float32, align_set_point_callback)
    
    #Received from imu, do not alter
    rospy.Subscriber('align_current', Float32, align_measurement_callback)
    
    #Received from the user. 
    #Contains the intensity you want to go forwards - int32 forwardsIntensity (0-100)
    #Contains if it is on or not - Bool movingForwards (True - False)
    rospy.Subscriber('forwards_command', ForwardsCommand, forwards_command_callback)

    #Received from user
    #Contains if the controller is on or not - Bool controllerRunning (True - False)
    #Changes the polarity of the horizontal thrusters. (true changes the polarity) - Bool polarity (True - False)
    #Changes the gain of the controller - float32 controllerGain (1-20)
    rospy.Subscriber('align_controller_setup', ControllerSetup, controller_setup_callback)
    
    #Initialize motors to 0
    motor_pub.publish(0,0)


    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Align Controller %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        error_pub.publish(error)
        rate.sleep()


if __name__ == '__main__':
    initialize_node()