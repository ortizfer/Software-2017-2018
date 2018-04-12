#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Tatiana Rodriguez and Carlos Morel
"""

# Imports
from Utils.QualifyingGate import QGate
from Utils.QualifyingTube import QTube
from Utils import RosCom
from time import *


# Variables
xGate = 0                                # X coordinate from the center of the gate with respect to the center of the camera
xPole = 0                                # X coordinate from the center of the pole with respect to the center of the camera
xPixels = 640                            # Total x pixels of camera
yPixels = 480                            # Total y pixels of camera
seeGate = False                          # Do I see gate
seePoleFrontCam = False                  # Do I see pole with the front camera
seePoleSideCam = False                   # Do I see pole with the side camera
boxRadius = 50                           # Bounding box for the gate
topGateDist = QGate.distTopGateFromSurf  # Top distance from the surface to gate
noNameHeight = 0.5                       # Submarine height
passingDepth = topGateDist + 2 * noNameHeight # Safe y coordinate to pass the gate
sideCamBoxRadius = 25
frontCamPoleBB = xPixels - xPixels / 20
counter = 0
turnDegree = -10

# Functions
"""update center of gate with respect to 
center of the camera"""
def findCenterGate():
    global xGate
    gateCoor = QGate.getcentroid()
    xGate = gateCoor[0]

"""update center of gate with respect to 
center of the camera"""
def findCenterPole():
    global xPole
    poleCoor = QTube.getcentroid()
    xPole = poleCoor[0]

"""Asks vision if I see gate or not"""
def seeGateVision():
    global seeGate
    seeGate = QGate.getseeGate()

"""Asks vision if I see pole or not"""
def seePoleFrontCamVision():
    global seePoleFrontCam
    if QGate.getcamera() == 1:
        seePoleFrontCam = QTube.getseePole()

"""Asks vision if I see pole or not"""
def seePoleSideCamVision():
    global seePoleSideCam
    if QGate.getcamera() == 2:
        seePoleSideCam = QTube.getseePole()

"""Forward Left Right Backward movements"""
def move(direction,intensity, time):
    if direction == "F":
        RosCom.moveFoward(intensity)
        time.sleep(time)
        RosCom.moveFoward(0)
    elif direction == "B":
        RosCom.moveBackward(intensity)
        time.sleep(time)
        RosCom.moveBackward(0)

# Mission Logic
def runQualifying():
    """Sets my current direction as my north"""
    RosCom.headingMotors(1, 0, 0)

    """"Tells Vision which mission we are at"""
    RosCom.setVisionMission(0)

    """Initializes seeGate variable"""
    seeGateVision()

    """Submerges to a safe distance from the top 
    of the gate and checks if I am looking at the 
    horizontal center of the gate, if not, it 
    will align with it and go through"""
    while seeGate:
        RosCom.setDepth(True, passingDepth)
        findCenterGate()

        if abs(xGate - xPixels/2) > boxRadius:
            if xGate - xPixels/2 > 0:
                RosCom.moveLeft(20)
            else:
                RosCom.moveRight(20)
        else:
            RosCom.moveLeft(0)
            RosCom.moveRight(0)
            move("F", 40, 6)
        seeGateVision()

    """if I cannot see the marker, I will keep moving
    forward until I find it"""
    while not seePoleFrontCam:
        RosCom.moveFoward(40)
        seePoleFrontCamVision()

    RosCom.moveFoward(0)

    """When the marker is found, it will check if it
    is on the right side of the camera, if not, it 
    will move to the left until it is, otherwise it
    will go forward"""
    while seePoleFrontCam:
        findCenterPole()

        if xPole < frontCamPoleBB:
            RosCom.moveLeft(20)
        else:
            RosCom.moveFoward(40)

        seePoleFrontCamVision()

    """It will keep moving forward until I see it 
    with the side camera"""
    while not seePoleSideCam:
        RosCom.moveFoward(40)
        seePoleSideCamVision()

    """Once seen with the side camera, it checks if
    its in the center of the picture, if not, it will
    align the center of the marker with the center of
    the camera otherwise it will start to go around 
    the marker"""
    while seePoleSideCam:
        findCenterPole()
        if abs(xPole - xPixels / 2) > sideCamBoxRadius:
            if xPole - xPixels / 2 > 0:
                RosCom.moveBackward(20)
            else:
                RosCom.moveFoward(20)
        else:
            RosCom.headingMotors(1, 0, 0)
            RosCom.headingMotors(1, 1, turnDegree)
            counter = counter + turnDegree
            if counter == -180:
                break
        seePoleSideCamVision()

    seeGateVision()

    """After the turn, it will keep going forward until
    the gate is seen"""
    while not seeGate:
        RosCom.moveFoward(40)
        seeGateVision()

    """Once found, it will make sure we are looking at 
    its center and go forward until we cannot see it 
    completely"""
    while seeGate:
        findCenterGate()

        if abs(xGate - xPixels/2) > boxRadius:
            if xGate - xPixels/2 > 0:
                RosCom.moveLeft(20)
            else:
                RosCom.moveRight(20)
        else:
            RosCom.moveLeft(0)
            RosCom.moveRight(0)
            RosCom.moveFoward(40)
        seeGateVision()

    seePoleSideCamVision()

    """To make sure we are going through, we will 
    check the side cam for the side of the gate 
    which is similar to the marker and once we see it,
    it will go forward for 2 seconds"""
    while not seePoleSideCam:
        RosCom.moveFoward(20)
        seePoleSideCamVision()

    if seePoleSideCam:
        move("F", 40, 2)