from Utils import Movement
from Utils import Path
"""


@author: Carlos Morel and Tatiana Rodriguez
"""
#Code
# Definitions
#Definitions from Vision
def frontCamFoundPath():
    global foundPath
    # VISION
    return #HERE WE WILL USE A VARIABLE THAT RETURN A TRUE OR FALSE

def bottomCamFoundPath():
    global foundPathBottom
    #VISION
    return

def searchForPath(x): #Search for the path
    global foundPath
    if not x:
        foundPath = frontCamFoundPath()
        if not foundPath:
            Movement.rotate(60)
            foundPath = frontCamFoundPath()
            if not foundPath:
                Movement.rotate(-120)


def searchForPathBottom(y): #Find path with the bottom camera
    global foundPathBottom
    count = 0
 '''   while not y and count < 6:
        Movement.rotate(60)
        bottomCamFoundPath(foundPathBottom)
        count += 1
    return foundPathBottom'''

foundPath = False #Initial value that will make the submarine look for the path
foundPathBottom = False

Movement.depth(3.9624) #Submerge so we are able to see the path with the frontal camera

if not foundPath: #if I dont see the path with the frontal camera look right
    global foundPath
    Movement.rotate(60) #Do not know what function use in this part
    frontCamFoundPath(foundPath)
    searchForPath(foundPath)


Cameras.onDownCamera    #Command to turn on the down camera



while (not foundPathBottom):
    global foundPathBottom
    Movement.foward() #By how many meters should the submarine move foward
    searchForPathBottom(foundPathBottom)

"""CMOREL NEW PATH BEGINNING

# Imports
from Utils import Path
from Utils import RosCom
from Missions.QualifyingMission import move

# Variables

seePath = False  # Do I see path

# Functions
def seePathVision():
    global seePath
    seePath = Path.getseePath()



# Mission Logic

"""Tells VISION in what mission we are"""
RosCom.setVisionMission(2)

"""Initialize seePath variable"""
seePathVision()  # Can I see the path from the bottom camera at our initial depth

"""What Charlie thinks the mission will continue
WAITING ON THE STUPED HOE FROM TATS"""

"""After seeing the path with the bottom camera
at the initial depth"""

RosCom.setDepth(enable,12)  # Go down until we are 12 feet
"""