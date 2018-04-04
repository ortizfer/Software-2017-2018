from Utils import RosCom

"""@authors Karinne and Christian"""
""" 
    Given an angle and the length of the lines *by Vision*, then 
    if the difference between the length of the lines is bigger than ~1, then 
    check which line is bigger or check the polarity of the difference,
    if polarity positive, turn right(align plus the angle given), 
    if polarity negative, turn left(align - angle given), 
    else if  difference is less than 1 then keep moving forward. 
    
    left: sum the angles, adding the angle with the initial angle will make th sub turn left
    right: subtract the angles, subtracting the angle from the initial angle will make the sub turn right
"""


def found_path_front():
    # search for path through front camera, Vision
    return True


def found_path_bottom():
    # search for path through bottom camera
    return True


def search_for_path():
    # search for path through front and bottom cameras
    if found_path_front():
        while not found_path_bottom():
            RosCom.moveForward()
    else:
        RosCom.moveForward()


search_for_path()

# RosCom.setDepth(1, 13.00) specify and set depth
path_angle = 0 # angle given by Vision
align = 0 # set angle
path_mission = True


lines_length = []  # Get vision
lines_a = lines_length[0]  # leftmost
lines_b = lines_length[1]  # rightmost


# while path mission is true
while path_mission:
    if float(lines_a) - float(lines_b) >= 1.00:

        if float(lines_a) > float(lines_b):
            align = align + path_angle
            RosCom.headingMotors(1, 7, align) # 7 is for eliminating compiler errors
            RosCom.moveForward(35)

        elif float(lines_b) > float(lines_a):
            align = align - path_angle
            RosCom.moveForward(35)
    else:
        RosCom.moveForward(25)