"""


@author: Carlos Morel and Tatiana Rodriguez
"""

CMOREL NEW PATH BEGINNING

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
seePathVision()

"""What Charlie thinks the mission will continue
WAITING ON THE STUPED HOE FROM TATS"""

"""After seeing the path with the bottom camera
at the initial depth"""

RosCom.setDepth(True, 12)  # Go down until we are 12 feet