#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Tatiana Rodriguez and Carlos Morel
"""

#binding box from other gate
"""def check_binding_box(x,y):
    if (xPixels-50) < x < (xPixels+50) and (yPixels-50) < y < (yPixels+50):
        return True
    return False
"""
#Imports
from Utils.QualifyingGate import QGate
from Utils.QualifyingTube import QTube
from Utils import Movement

#Initialized Variables
x = 0
y = 0

#Functions
def findcenter():
    global x, y
    x = QGate.getcenterX()
    y = QGate.getcenterY()




Movement.forward(4)     #After passing the gate move forward 4 meters

seeTube = False     #Initial value for seeing the tube variable

def seeQTube(seeTube):  #Do I see the tube
    #VISION

def findQTube(g):    #Search algorithm of the qualifying tube
    global seeTube

while seeQTube(seeTube) == False:
    findQTube()
    Movement.forward(2)


#TO FIND THE QUALIFYNG GATE AFTER PASSING THE TUBE
'''def findQGate(h):   #Search algorithm for the qualifying gate
   global seeGate

  if h == False:
       Movement.rotate(-70)
       seeQGate(seeGate)
       h = seeGate
       if h == False:
           Movement.rotate(140)
           seeQGate(seeGate)
           h = seeGate
           if h == False:
               Movement.rotate(-70)
    seeGate = h


while seeQGate(seeGate) == False:
    findQGate()
    Movement.forward(0.5)
'''

#DO NOT KNOW WHY WE WILL USE THIS
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





