#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@authors: Tatiana Rodriguez and Carlos Morel
"""

class QGate:
    # all units are in meters
    gateTubeDiameter = 0.0635  # Diameter of the qualifying gate tubes
    distTopGateFromSurf = 1  # Distance of top of gate from surface
    distBetweenTubes = 2  # The distance between the tubes of the qualifying gate
    allowance= 0.4  # This is the minimum allowance that the submarine can be to a tube

    def __init__(self):

        xCenterDist = 1.5  # X coordinate from the center to a tube of the qualifying gate
        allowableRight = 0.7    #Right approach to the right tube
        allowableLeft = 0.7     #Left approach to the left tube
        gateLeftCorner = 0.2   #Left corner of the gate
        gateRightCorner = 32    #Right corner of the gate

#Setters
    def setxCenterDist(self,received):
        self.xCenterDist = received     #A variable from VISION that give us the x coordinate

    def setallowableRight(self,received):
        self.allowableRight = received

    def setallowableLeft (self, received):
        self.allowableLeft = received

    def setgateLeftCorner(self, received):
        self.gateLeftCorner = received

    def setgateRightCorner(self,received):
        self.gateRightCorner = received

    #Getters
    def getgateTubeDiameter(self):
        return self.gateTubeDiameter

    def getdistTopGateFromSurf(self):
        return self.distTopGateFromSurf

    def getxCenterDist(self):
        return self.xCenterDist

    def getallowableRight(self):
        return self.allowableRight

    def getallowableLeft(self):
        return self.allowableLeft

    def getgateLeftCorner(self):
        return self.gateLeftCorner

    def getgateRightCorner(self):
        return self.gateRightCorner




