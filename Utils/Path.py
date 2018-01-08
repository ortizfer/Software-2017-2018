#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Charlie and The Painter
"""
#all units are in meters
class Path:

    pathColor = orange #Color of the path
    pathWidth = 0.2 #Width of the path
    pathLength = 0.4 #Length of the path
    distPathFromBottom = 0.75 #Distance of the path from the bottom of the pool

    def __init__(self):

        xpathMassCenter = 2 #X coordinate of the path mass center
        xcenterBlueGate = 0.5 #X coordinate of the blue gate center from the first mission
#Setters
    def setxpathMassCenter(self, received):
        self.xpathMassCenter = received
    def setxcenterBlueGate(self,received):
        self.xcenterBlueGate = received

#Getters
    def getxpathMassCenter(self):
        return self.xpathMassCenter
    def getxcenterBlueGate(self):
        return self.xcenterBlueGate


