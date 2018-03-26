#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@authors: Tatiana Rodriguez and Carlos Morel
"""

class QGate:
    # all units are in meters
    gateTubeDiameter = 0.0635  # Diameter of the qualifying gate tubes
    distTopGateFromSurf = 1  # Distance of top of gate from surface

    def __init__(self):
        self.centroid = (0,0)
        self.boundingBox = [0,0,0,0]
        self.value = 5
        self.angle = 0
        self.camera = 1
        self.seeGate = False

#Setters
    def setcentroid(self,received):
        self.centroid = received     #A variable from VISION that give us the x coordinate

    def setboundingBox(self,received):
        self.boundingBox = received

    def setCamera(self,received):
        self.camera = received

    def setseeGate(self, received):
        self.seeGate = received

#Getters

    def getcentroid(self):
        return self.centroid

    def getboundingBox(self):
        return self.boundingBox

    def getcamera(self):
        return self.camera

    def getseeGate(self):
        return self.seeGate
