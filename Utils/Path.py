#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Charlie and Tatiana
"""
#all units are in meters
class Path:

    def __init__(self):
        self.wumbo = 0   # Angle from the horizontal line of the camera and the path
        self.longerLineLeft = False   # Tell us if the left line of the path is longer
        self.longerLineRight = False   # Tell us if the left line of the path is longer

#Setters
    def setxpathMassCenter(self, received):
        self.xpathMassCenter = received

#Getters
    def getxpathMassCenter(self):
        return self.xpathMassCenter



