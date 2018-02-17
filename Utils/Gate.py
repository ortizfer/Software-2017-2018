#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Fernando Guzman and Angel Burgos
"""


class Gate:

    def __init__(self):

        #recievedThing = 1

        distCenterRed = 0   #distance to the center between the red strips
        distCenterBlack = 0 #distance to the center between the black strips
        angleRed = 0
        angleBlack = 0


    """def setterExample(self, recieved):
        self.recievedThing = recieved

    def getterExample(self):
        return self.recievedThing
    """

    def setterCenterR(self, d):
        self.distCenterRed = d


    def setterCenterB(self, d):
        self.distCenterBlack = d


    def setterAngleR(self, theta):
        self.angleRed = theta


    def setterAngleB(self, theta):
        self.angleBlack = theta


    def getterCenterR(self):
        return self.distCenterRed


    def getterCenterB(self):
        return self.distCenterBlack


    def getterAngleR(self):
        return self.angleRed


    def getterAngleB(self):
        return self.angleBlack