from Utils import Movement
"""


@author: Carlos Morel and Tatiana Rodriguez
"""
#Code
# Definitions
#Definitions from Vision
def frontCamFoundPath(x):
    global foundPath
    # VISION
    foundPath =

def bottomCamFoundPath(y):
    global foundPathBottom
    #VISION
    return foundPathBottom

def searchForPath(x): #Search for the path
    global foundPath
    count = 0 #When count is equal to 6 the submarine will be in the initial position
    while not x and count < 6:
        Movement.rotate(60)
        frontCamFoundPath(x)
        count += 1
    foundPath = x

def searchForPathBottom(y): #Find path with the bottom camera
    global foundPathBottom
    count = 0
    while not y and count < 6:
        Movement.rotate(60)
        bottomCamFoundPath(foundPathBottom)
        count += 1
    return foundPathBottom

foundPath = False #Initial value that will make the submarine look for the path
foundPathBottom = False

Movement.depth(3.9624) #Submerge so we are able to see the path with the frontal camera

if not foundPath: #if I dont see the path with the frontal camera look right
    global foundPath
    Movement.rotate() #Do not know what function use in this part
    searchForPath(foundPath)


Cameras.onDownCamera    #Command to turn on the down camera



while (not foundPathBottom):
    global foundPathBottom
    Movement.foward() #By how many meters should the submarine move foward
    searchForPathBottom(foundPathBottom)

