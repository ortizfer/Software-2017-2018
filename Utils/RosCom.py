#!/usr/bin/env python
#

"""
    The RosCom.py folder  contains the necessary functions to properly
    maintain a set of communication nodes. These nodes consist of both
    publishers and subscribers, which  alternate to essentially create
    two way  channels of communication  between internal processes, as
    well as processes outside the main computer.
"""
import rospy
from std_msgs.msg import *
from rumarino.msg import *


##---------------------Publishers---------------------------##

def initCommunications():	
    rospy.init_node('RosCom', anonymous=True)

    global depth_pub
    global align_pub
    global led_pub
    global vision_pub
    global move_pub
    depth_pub = rospy.Publisher('vertical_controller', depth_controller_setup, queue_size=10)
    align_pub = rospy.Publisher('horizontal_controller', align_controller_setpoint, queue_size=10) 
    move_pub = rospy.Publisher('horizontal_controller', movement, queue_size=10)
    vision_pub = rospy.Publisher('movement', Int32, queue_size=10)
    led_pub = rospy.Publisher('led_array', Int32, queue_size=10)
    

def setDepth(enable, depth):  # Sends integers in feet; moves the submarine to the specified depth
    if not rospy.is_shutdown():
        command.enable = enable
        command.feet = depth
        rospy.loginfo(command)
        depth_pub.publish(command)


def headingMotors(enable, mode, angle):   #  Sends 
    if not rospy.is_shutdown():
	command.enable = enable
        command.mode = mode
        command.angle = angle
        rospy.loginfo(command)
        align_pub.publish(command)


def moveFoward(motorIntensity):   #  Sends 
    if not rospy.is_shutdown():
        command.direction = 0
        command.intensity = motorIntensity
        rospy.loginfo(command)
        move_pub.publish(command)


def moveBackward(motorIntensity):   #  Sends 
    if not rospy.is_shutdown():
        command.direction = 1
        command.intensity = motorIntensity
        rospy.loginfo(command)
        move_pub.publish(command)


def moveLeft(motorIntensity):   #  Sends 
    if not rospy.is_shutdown():
        command.direction = 2
        command.intensity = motorIntensity
        rospy.loginfo(command)
        move_pub.publish(command)


def moveRight(motorIntensity):   #  Sends 
    if not rospy.is_shutdown():
        command.direction = 3
        command.intensity = motorIntensity
        rospy.loginfo(command)
        move_pub.publish(command)


def setVisionMission(mission):   #  Sends 
    if not rospy.is_shutdown():
        rospy.loginfo(mission)
       	vision_pub.publish(mission)


def setLedArray(ledPattern):  #  Sends a string corresponding to an RGB value to be displayed
    if not rospy.is_shutdown():
        rospy.loginfo(ledPattern)
        led_pub.publish(ledPattern)




##---------------------Subscribers---------------------------##

"""
#
def getDepth():  #  Returns the current depth of the submarine
    rospy.init_node('getDepth', anonymous=True, disable_signals=True)
    rospy.Subscriber('chatter', Float32, getDepthCallback)
    rospy.spin()
    return currentDepth

#Pressure sensor subscriber callback function
def getDepthCallback(data): #
    global currentDepth
    currentDepth = data.data    
    rospy.signal_shutdown("Data received")
   

#
def getIMUData():
    rospy.init_node('getIMU', anonymous=True, disable_signals=True)
    rospy.Subscriber('IMU_Sensor', String, getIMUCallback)
    rospy.spin()
    return imuData

#Imu subscriber callback function
def getIMUCallback(data):
    global imuData
    imuData = data.data    
    rospy.signal_shutdown("Data received")
"""
   
