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

#Variables
xGate = 0       # X coordinate from the center of the gate with respect to the center of the camera
xPole = 0       # X coordinate from the center of the pole with respect to the center of the camera
xPixels = 640   # Total x pixels of camera
yPixels = 480   # Total y pixels of camera
seeGate = False # Do I see gate
seePoleFrontCam = False # Do I see pole with the front camera
seePoleSideCam = False # Do I see pole with the side camera
boxRadius = 50  # Bounding box for the gate
topGateDist = QGate.distTopGateFromSurf  # Top distance from the surface to gate
noNameHeight = 0.5  # Submarine height
passingDepth = topGateDist + 2 * noNameHeight # Safe y coordinate to pass the gate


#Functions
def findCenterGate():   # update center of gate with respect to center of the camera
    global xGate
    gateCoor = QGate.getcentroid()
    xGate = gateCoor[0]

def findCenterPole():   # update center of gate with respect to center of the camera
    global xPole
    poleCoor = QTube.getcentroid()
    xPole = poleCoor[0]

def seeGateVision():    # Asks vision if I see gate or not
    global seeGate
    seeGate = QGate.getseePole

def seePoleFrontCamVision():    # Asks vision if I see pole or not
    global seePoleFrontCam
    if QGate.getcamera() == 1:
        seePoleFrontCam = QGate.getseePole()

def seePoleSideCamVision():    # Asks vision if I see pole or not
    global seePoleSideCam
    if QGate.getcamera() == 2:
        seePoleSideCam = QGate.getseePole()

#Mission Logic
RosCom.setPoint()
RosCom.setMission(0)    # Tells vision we are doing the qualifying maneuver
seeGateVision()

while seeGate:
    RosCom.setDepth(True, passingDepth)  # Submerge using the safe distance
    findCenterGate()

    if abs(xGate - xPixels/2) > boxRadius:
        if xGate - xPixels/2 > 0:
            RosCom.moveLeft(True,0.3) # Move to the left to align with the center
        else:
            RosCom.moveRight(True,0.3) # Move to the right to align with the center
    else:
        RosCom.moveFoward(True,5)

while not seePoleFrontCam:
    RosCom.moveFoward(1)

while seePoleFrontCam:
