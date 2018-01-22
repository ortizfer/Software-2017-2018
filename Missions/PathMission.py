from Utils import Movement
"""


@author: Carlos Morel and Tatiana Rodriguez
"""
#Code


foundPath = False #Initial value that will make the submarine look for the path
foundPathBottom = False

Movement.depth(3.9624) #Submerge so we are able to see the path with the frontal camera

while (not foundPath):
    global foundPath
    Movement. () #Do not know what function use in this part
    searchForPath(foundPath)

#ALGO CON ALINIARME CON EL CENTRO DE LO QUE VEO DEL PATH

Cameras.onDownCamera    #Command to turn on the down camera



while (not foundPathBottom):
    global foundPathBottom
    Movement.foward() #By how many meters should the submarine move foward
    searchForPathBottom(foundPathBottom)

#Debo ALINEARME una vez encuentre el path con la camara de abajo

#Codear la parte de ir moviendote y aliniandote dentro del path y terminar la mision

 #Definitions
 #DUDA CON findPath Y frontCamFoundPath
def searchForPath(x): #Search for the path
    global foundPath
    count = 0 #When count is equal to 6 the submarine will be in the initial position
    while (not x and count < 6):
        Movement.rotate(60)
        frontCamFoundPath(x)
        count = count + 1
    foundPath = x

def searchForPathBottom(y): #Find path with the bottom camera
    global foundPathBottom
    count = 0
    while (not y and count < 6):
        Movement.rotate(60)
        bottomCamFoundPath(foundPathBottom)
        count1 = count1 + 1
    return foundPathBottom

#Definitions from Vision
def frontCamFoundPath(x):
    global foundPath
    # VISION
    foundPath =

def bottomCamFoundPath(foundPathBottom):
    global foundPathBottom
    #VISION
    return foundPathBottom
