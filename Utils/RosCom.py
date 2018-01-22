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


##Node creation for publishers
def createPublisherNodes():
    rospy.init_node('Depth_Motors', anonymous=True)
    rospy.init_node('Heading_Motors', anonymous=True)
    rospy.init_node('LED_Array', anonymous=True)


##---------------------Publishers---------------------------##

def setDepth(depth):  # Sends integers in feet; moves the submarine to the specified depth
    pub = rospy.Publisher('depthMotors', Int32, queue_size=10)
    #rate = rospy.Rate(10) # 10hz
    if not rospy.is_shutdown():
        rospy.loginfo(depth)
        pub.publish(depth)
        ##rate.sleep()

def setLedArray(ledPattern):  #  Sends a string corresponding to an RGB value to be displayed
    pub = rospy.Publisher('ledArray', String, queue_size=10)
    #rate = rospy.Rate(10) # 10hz
    if not rospy.is_shutdown():
        rospy.loginfo(ledPattern)
        pub.publish(ledPattern)
        ##rate.sleep()


def setHM1(headingMotorCommand):   #  Sends an integer corresponding to a predetermined command
    pub = rospy.Publisher('headingMotor1', Int32, queue_size=10)
    #rate = rospy.Rate(10) # 10hz
    if not rospy.is_shutdown():
        rospy.loginfo(hMData)
        pub.publish(hMData)
        ##rate.sleep()


def setHM2(headingMotorCommand):    #  Sends an integer corresponding to a predetermined command
    pub = rospy.Publisher('headingMotor2', Int32, queue_size=10)
    #rate = rospy.Rate(10) # 10hz
    if not rospy.is_shutdown():
        rospy.loginfo(hMData)
        pub.publish(hMData)
        ##rate.sleep()


def setHM3(headingMotorCommand):    #  Sends an integer corresponding to a predetermined command
    pub = rospy.Publisher('headingMotor3', Int32, queue_size=10)
    #rate = rospy.Rate(10) # 10hz
    if not rospy.is_shutdown():
        rospy.loginfo(hMData)
        pub.publish(hMData)
        ##rate.sleep()


def setHM4(headingMotorCommand):    #  Sends an integer corresponding to a predetermined command
    pub = rospy.Publisher('headingMotor4', Int32, queue_size=10)
    #rate = rospy.Rate(10) # 10hz
    if not rospy.is_shutdown():
        rospy.loginfo(hMData)
        pub.publish(hMData)
        ##rate.sleep()


##---------------------Subscribers---------------------------##

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
    Jan 8. 7:40 P.M. CFigueroa and CAnibal 
    Documented publisher functions.
"""