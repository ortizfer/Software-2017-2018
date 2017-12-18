"""
Movement API file, All Movement functions of the AUV are available here.
Use the function to call the specified movement on the AUV.

Author: Fernando Ortiz

"""


#Function the moves the AUV forward

def forward(d):
    print("Moving forward "+d+" distance")


#Function that moves the AUV backwards

def backward(d):
    print("Moving backward "+d+" distance")


#Function that moves up or down the AUV

def depth(h):
    print("Moving to "+h+" depth")


#Function that moves the AUV left

def left(d):
    print("Moving left "+d+" distance")


#Function the moves the AUV right

def right(d):
    print("Moving right "+d+" distance")


#Function that rotates the AUV

def rotate(x):
    print("Rotating "+x+" angle")

#Function that stops the system if needed

def strop():
    print("Stopping")

"""

Dec. 18 10:06AM FOrtiz
Added the stop function 

Dec. 17 8:18PM FOrtiz
Creation of the movement API for the code development.


"""