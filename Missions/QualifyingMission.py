#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Tatiana Rodriguez and Carlos Morel
"""
from QualifyingGate import *
from QualifyingTube import *
from Movement import *

def seeQGate():
    return bool

def findQGate(seeQGate):

    count = 0

    while seeQGate() == False and count < 6:
        Movement.rotate(60)
        seeQGate()
        count += 1
    seeCount = [seeQGate(),count]
    return seeCount

while seeQGate() == False:
    Movement.foward(0.5)
    findQGate()

while QGate.xCenterDist == 0:


'''def getAllowableRightFromVision():
    return ARFV #Allowable Right From Vision

def getAllowableLeftFromVision():
    return ALFV #Allowable Left From Vision

QGate.setallowableRight(getAllowableRightFromVision())  #NPI
QGate.setallowableLeft(getAllowableLeftFromVision())

GAR = QGate.getallowableRight()
GAL = QGate.getallowableLeft()
DTGFS = QGate.distTopGateFromSurf
AT = QGate.allowanceTop
GD = Movement.depth(AT+DTGFS)

while GAR < 0 or GAL < 0:
    if GAR < 0:
        Movement.left(-GAR)
    elif GAL < 0:
        Movement.right(-GAL)'''

foward()

def findQTube():
    return bool
findQTube()

