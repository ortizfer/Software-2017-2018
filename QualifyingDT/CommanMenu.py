"""
    CommandMenu.py is a quick solution to remotely test and control
    the AUV through ROS topics.
"""

import rospy
from std_msgs.msg import Int32, Float32, Bool
from rumarino_package.msg import Centroid, ControllerSetup, ForwardsCommand, HorizontalMotors


# ###########-UTILS-########### #
def parse(string):
    arguments = []
    i = 0
    for char in string:
        if char == ',':
            i += 1
        else:
            arguments[i] = arguments[i] + char

    for i in range(0, len(arguments)-1):
        try:
            arguments[i] = int(arguments[i])
        finally:
            arguments[i] = arguments[i]

    return arguments
# ###########-Publishers-########### #
align_controller_setup = rospy.Publisher("align_controller_setup", ControllerSetup)
align_current = rospy.Publisher("align_current", Float32)
align_error = rospy.Publisher("align_error", Float32)
align_set_point = rospy.Publisher("align_set_point", Float32)
depth_controller_setup = rospy.Publisher("depth_controller_setup", Bool)
depth_current = rospy.Publisher("depth_current", Float32)
depth_error = rospy.Publisher("depth_error", Float32)
depth_set_point = rospy.Publisher("depth_set_point", Float32)
forwards_command = rospy.Publisher("forwards_command", ForwardsCommand)
horizontal_motors = rospy.Publisher("horizontal_motors", HorizontalMotors)
vertical_motors = rospy.Publisher("vertical_motors", Int32)

publisher_dictionary = {
    "acs": align_controller_setup,
    "ac": align_current,
    "ae": align_error,
    "asp": align_set_point,
    "dcs": depth_controller_setup,
    "dc": depth_current,
    "dsp": depth_set_point,
    "fc": forwards_command,
    "hm": horizontal_motors,
    "vm": vertical_motors
}

# ###########-SCRIPT-########### #
rospy.init_node("CommandMenu", anonymous=True)
print("Command Menu ready...")

while not rospy.is_shutdown():
    ''''
    print("Available Commands:")
    for command in commands:
        print(command)
    '''
    inp = input("Enter command: ")
    args = parse(inp)
    pub = publisher_dictionary[args[0]]
    pub.Publish(*args[1:])

"""
VERSION CONTROL:

1. April 21, 2018; 3:11pm; Carlos J. Figueroa
    Initial commit of the CommandMenu.py

"""