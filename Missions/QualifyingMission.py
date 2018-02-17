#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Tatiana Rodriguez and Carlos Morel
"""
from Utils import QualifyingGate, QualifyingTube, Movement

seeGate = False

def seeQGate(seeGate): #Do I see the gate
    #VISION

def findQGate(h):
   global seeGate

  if h == False:
       Movement.rotate(-60)
       seeQGate(seeGate)
       h = seeGate
       if h == False:
           Movement.rotate(120)
           seeQGate(seeGate)
           h = seeGate
           if h == False:
               Movement.rotate(-60)
    seeGate = h


while seeQGate(seeGate) == False:
    findQGate()
    Movement.foward(0.5)


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
findQTube()





def findQTube():
    return bool



