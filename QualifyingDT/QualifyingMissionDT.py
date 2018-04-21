#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Tatiana Rodriguez and Carlos Morel
"""

# Imports
from rumarino_package.msg import Centroid, ForwardsCommand
import rospy
from std_msgs.msg import Int32, Float32
from time import *


# Variables
xGate = 0                                # X coordinate from the center of the gate with respect to the center of the camera
xMarker = 0                              # X coordinate from the center of the pole with respect to the center of the camera
xPixels = 640                            # Total x pixels of camera
yPixels = 480                            # Total y pixels of camera
seeGate = False                          # Do I see gate
seeMarkerFrontCam = False                # Do I see pole with the front camera
seeMarkerSideCam = False                 # Do I see pole with the side camera
boxRadius = 50                           # Bounding box for the gate
topGateDist = QGate.distTopGateFromSurf  # Top distance from the surface to gate
noNameHeight = 1.5                       # Submarine height in ft
passingDepth = topGateDist + 2 * noNameHeight # Safe y coordinate to pass the gate
sideCamBoxRadius = 25
frontCamPoleBB = 80
turnDegree = -10
counter = 0

# Functions
"""update center of gate with respect to 
center of the camera"""
def findCenterGate():
    global xGate
    gateCentroid = rospy.wait_for_message("Centroid_Gate_Front", Centroid, timeout=5)
    xGate = gateCentroid.x

"""update center of marker with respect to 
center of the camera"""
def findCenterMarker(cam):
    global xMarker
    if cam == "Front":
        markerCentroid = rospy.wait_for_message("Centroid_Marker_Front", Centroid, timeout=5)
        xMarker = markerCentroid.x
    elif cam == "Side":
        markerCentroid = rospy.wait_for_message("Centroid_Marker_Side", Centroid, timeout=5)
        xMarker = markerCentroid.x

"""Asks vision if I see gate or not"""
def seeGateVision():
    global seeGate
    gateCentroid = rospy.wait_for_message("Centroid_Gate_Front", Centroid, timeout=5)
    y = gateCentroid.y
    if y == -1:
        seeGate = False
    else:
        seeGate = True

"""Asks vision if I see marker or not"""
def seeMarkerVision(cam):
    global seeMarkerFrontCam
    global seeMarkerSideCam
    if cam == "Front":
        markerCentroid = rospy.wait_for_message("Centroid_Marker_Front", Centroid, timeout=5)
        y = markerCentroid.y
        if y == -1:
            seeMarkerFrontCam = False
        else:
            seeMarkerFrontCam = True
    elif cam == "Side":
        markerCentroid = rospy.wait_for_message("Centroid_Marker_Side", Centroid, timeout=5)
        y = markerCentroid.y
        if y == -1:
            seeMarkerSideCam = False
        else:
            seeMarkerSideCam = True

"""Forward Left Right Backward movements"""
def move(direction, intensity, time):
    if direction == "F":
        forwardsCommand = rospy.Publisher("forwards_command", ForwardsCommand)
        forwardsCommand.publish(intensity, True)
        time.sleep(time)
        forwardsCommand.publish(0, True)
    elif direction == "B":
        backwardsCommand = rospy.Publisher("forwards_command", ForwardsCommand)
        backwardsCommand.publish(-intensity, True)
        time.sleep(time)
        backwardsCommand.publish(0, True)

# Mission Logic
def runQualifying():

    """Initializes seeGate variable"""
    seeGateVision()


    setDepth = rospy.Publisher("depth_set_point", Float32)
    forward = rospy.Publisher("forwards_command", ForwardsCommand)
    align = rospy.Publisher("align_set_point", Float32)
    currentAngle = rospy.wait_for_message("align_current", Float32)

    """Submerges to a safe distance from the top 
       of the gate and checks if I am looking at the 
       horizontal center of the gate, if not, it 
       will align with it and go through"""
    while seeGate:

        setDepth.publish(passingDepth)

        findCenterGate()

        if abs(xGate - xPixels/2) > boxRadius:
            if xGate - xPixels/2 > 0:
                align.publish(90)
                move("F", 40, 1)
                align.publish(-90)
            else:
                align.publish(-90)
                move("F", 40, 1)
                align.publish(90)
        else:
            move("F", 40, 6)
        seeGateVision()

    """if I cannot see the marker, I will keep moving
    forward until I find it"""

    while not seeMarkerFrontCam:
        forward.publish(40, True)
        seeMarkerVision("Front")

    forward.publish(0, True)

    """When the marker is found, it will check if it
    is on the right side of the camera, if not, it 
    will move to the left until it is, otherwise it
    will go forward"""
    while seeMarkerFrontCam:
        findCenterMarker("Front")
        if xMarker < frontCamPoleBB:
            align.publish(90)
            move("F", 40, 1)
            align.publish(-90)
        else:
            seeMarkerVision("Front")

    """It will keep moving forward until I see it 
    with the side camera"""
    while not seeMarkerSideCam:
        forward.publish(40)
        seeMarkerVision("Side")

    """Once seen with the side camera, it checks if
    its in the center of the picture, if not, it will
    align the center of the marker with the center of
    the camera otherwise it will start to go around 
    the marker"""
    while seeMarkerSideCam:
        findCenterMarker("Side")
        if abs(xMarker - xPixels / 2) > sideCamBoxRadius:
            if xMarker - xPixels / 2 > 0:
                forward.publish(-20)
            else:
                forward.publish(20)
        else:
            global counter
            align.publish(turnDegree)
            counter = counter + turnDegree
            if counter < -180:
                break
        seeMarkerVision("Side")

    seeGateVision()

    """After the turn, it will keep going forward until
    the gate is seen"""
    while not seeGate:
        forward.publish(40)
        seeGateVision()

    """Once found, it will make sure we are looking at 
    its center and go forward until we cannot see it 
    completely"""
    while seeGate:
        findCenterGate()

        if abs(xGate - xPixels/2) > boxRadius:
            if xGate - xPixels/2 > 0:
                align.publish(90)
                move("F", 40, 1)
                align.publish(-90)
            else:
                align.publish(-90)
                move("F", 40, 1)
                align.publish(90)
        else:
            forward.publish(40)
        seeGateVision()

    seeMarkerVision("Side")

    """To make sure we are going through, we will 
    check the side cam for the side of the gate 
    which is similar to the marker and once we see it,
    it will go forward for 2 seconds"""
    while not seeMarkerSideCam:
        forward.publish(20)
        seeMarkerVision("Side")

    if seeMarkerSideCam:
        move("F", 40, 2)