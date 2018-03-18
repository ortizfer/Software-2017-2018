#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Tatiana Rodriguez and Carlos Morel
"""

#binding box from other gate

#Imports
from Utils.QualifyingGate import QGate
from Utils.QualifyingTube import QTube
from Utils import RosCom
from time import *


#Variables
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

#Functions
def findCenterGate():                    # update center of gate with respect to center of the camera
    global xGate
    gateCoor = QGate.getcentroid()
    xGate = gateCoor[0]

def findCenterPole():                    # update center of gate with respect to center of the camera
    global xPole
    poleCoor = QTube.getcentroid()
    xPole = poleCoor[0]

def seeGateVision():                     # Asks vision if I see gate or not
    global seeGate
    seeGate = QTube.getseePole()

def seePoleFrontCamVision():             # Asks vision if I see pole or not
    global seePoleFrontCam
    if QGate.getcamera() == 1:
        seePoleFrontCam = QTube.getseePole()

def seePoleSideCamVision():              # Asks vision if I see pole or not
    global seePoleSideCam
    if QGate.getcamera() == 2:
        seePoleSideCam = QTube.getseePole()

def move(direction,intensity, time):    # Forward Left Right Backward movements
    if direction == "L":
        RosCom.moveLeft(intensity)
        time.sleep(time)
        RosCom.moveLeft(0)
    elif direction == "R":
        RosCom.moveRight(intensity)
        time.sleep(time)
        RosCom.moveRight(0)
    elif direction == "F":
        RosCom.moveFoward(intensity)
        time.sleep(time)
        RosCom.moveFoward(0)
    elif direction == "B":
        RosCom.moveBackward(intensity)
        time.sleep(time)
        RosCom.moveBackward(0)

#Mission Logic
RosCom.headingMotors(1, 0, 0)
RosCom.setVisionMission(0)               # Tells vision we are doing the qualifying maneuver
seeGateVision()

while seeGate:
    RosCom.setDepth(True, passingDepth)  # Submerge using the safe distance
    findCenterGate()

    if abs(xGate - xPixels/2) > boxRadius:
        if xGate - xPixels/2 > 0:
            RosCom.moveLeft(20)           # Move to the left to align with the center
        else:
            RosCom.moveRight(20)           # Move to the right to align with the center
    else:
        RosCom.moveLeft(0)
        RosCom.moveRight(0)
        move("F", 40, 6)
    seeGateVision()

while not seePoleFrontCam:
    RosCom.moveFoward(40)
    seePoleFrontCamVision()

RosCom.moveFoward(0)

while seePoleFrontCam:
    findCenterPole()                   # Move left to see the pole with the left cameras

    if xPole < frontCamPoleBB:
        RosCom.moveLeft(20)             # HALP Im gonna keep moving left  # How do I tell it to stop
    else:
        RosCom.moveFoward(40)

    seePoleFrontCamVision()

while not seePoleSideCam:
    RosCom.moveFoward(40)
    seePoleSideCamVision()

while seePoleSideCam:
    findCenterPole()
    if abs(xPole - xPixels / 2) > sideCamBoxRadius:
        if xPole - xPixels / 2 > 0:
            RosCom.moveBackward(20)  # Move to the left to align with the center
        else:
            RosCom.moveFoward(20)  # Move to the right to align with the center
    else:
        RosCom.headingMotors(1, 0, 0)
        RosCom.headingMotors(1, 1, turnDegree)
        counter = counter + turnDegree
        if counter == -180:
            break
    seePoleSideCamVision()

seeGateVision()

while not seeGate:
    RosCom.moveFoward(40)
    seeGateVision()

while seeGate:
    findCenterGate()

    if abs(xGate - xPixels/2) > boxRadius:
        if xGate - xPixels/2 > 0:
            RosCom.moveLeft(20)           # Move to the left to align with the center
        else:
            RosCom.moveRight(20)           # Move to the right to align with the center
    else:
        RosCom.moveLeft(0)
        RosCom.moveRight(0)
        RosCom.moveFoward(30)
    seeGateVision()
