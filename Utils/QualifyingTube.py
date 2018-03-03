#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Carlos Morel and Tatiana Rodriguez
"""



class QTube:

    tubeDiameter = 0.0762
    allowableTubeApproach = 1

    def __init__(self):
        centroid = (0, 0)
        boundingBox = [0, 0, 0, 0]
        value = 5
        angle = 0
        camera = 1
        seePole = False

# Setters

    def setcentroid(self, received):
        self.centroid = received  # A variable from VISION that give us the x coordinate

    def setboundingBox(self, received):
        self.boundingBox = received

    def setCamera(self, received):
        self.camera = received

    def setseePole(self, received):
        self.seePole = received

# Getters

    def getcentroid(self):
        return self.centroid

    def getboundingBox(self):
        return self.boundingBox

    def getcamera(self):
        return self.camera

    def getseePole(self):
        return self.seePole
