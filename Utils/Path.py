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
    def setlongerLineLeft(self, received):
        self.longerLineLeft = received
    def setlongerLineRight(self, received):
        self.longerLineRight = received
    def setwumbo(self, received):
        self.wumbo = received

#Getters
    def getlongerLineLeft(self):
        return self.longerLineLeft
    def getlongerLineRight(self):
        return self.longerLineRight
    def getwumbo(self):
        return self.wumbo


