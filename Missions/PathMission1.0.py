from Utils import RosCom

"""@authors Karinne and Christian"""
""" 
    Given an angle and the length of the lines *by Vision*, then 
    if the difference between the length of the lines is greater than 1, then 
    check which line is bigger or check the polarity of the difference,
    if polarity positive, turn right(align plus the angle given), 
    if polarity negative, turn left(align - angle given), 
    else if  difference is less than 1 then keep moving forward. 
    
    left: sum the angles, adding the angle with the initial angle will make th sub turn left
    right: subtract the angles, subtracting the angle from the initial angle will make the sub turn right
"""
RosCom.setVisionMission(2)

def found_path_bottom():
    # search for path through bottom camera
    return True


def search_for_path():
    # search for path through front and bottom cameras
    while not found_path_bottom():
        found_path_bottom();
    return True;


def get_angle():
    angle = 0
    # Get the angle given by vision
    return angle

def mission_on(): # Notify when the path mission starts
    return True

search_for_path()

# RosCom.setDepth(1, 13.00) specify and set depth
align = 0  # set angle
path_mission = True


lines_length = []  # Get vision
line_a = lines_length[0]  # leftmost
line_b = lines_length[1]  # rightmost


# while path mission is true
def mission_run():
    while mission_on():
        if line_a - line_b >= 1.00:
            if line_a > line_b:
                align = align + get_angle()
                # RosCom.headingMotors(1, 7, align) # 7 is for eliminating compiler errors, don't know what should go there
                # Tell ros to align sub to the new angle
                RosCom.moveForward(35)
            elif line_b > line_b:
                align = align - get_angle()
                # RosCom.headingMotors(1, 7, align)
                # Tell ros to align sub to the new angle
                RosCom.moveForward(35)
        else:
            # If the difference between lines lengths is less than 1, then continue to move forward
            RosCom.moveForward(25)
    # Method that verifies if mission is still on(running), should return true or false
    mission_run()
