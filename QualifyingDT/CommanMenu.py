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
            arguments[i] = float(arguments[i])
        except ValueError:
            arguments[i] = arguments[i]

    return arguments
# ###########-Publishers-########### #
print("Creating publishers...")
align_controller_setup = rospy.Publisher("align_controller_setup", ControllerSetup, queue_size=10)
align_current = rospy.Publisher("align_current", Float32, queue_size=10)
align_error = rospy.Publisher("align_error", Float32, queue_size=10)
align_set_point = rospy.Publisher("align_set_point", Float32, queue_size=10)
depth_controller_setup = rospy.Publisher("depth_controller_setup", Bool, queue_size=10)
depth_current = rospy.Publisher("depth_current", Float32, queue_size=10)
depth_error = rospy.Publisher("depth_error", Float32, queue_size=10)
depth_set_point = rospy.Publisher("depth_set_point", Float32, queue_size=10)
forwards_command = rospy.Publisher("forwards_command", ForwardsCommand, queue_size=10)
horizontal_motors = rospy.Publisher("horizontal_motors", HorizontalMotors, queue_size=10)
vertical_motors = rospy.Publisher("vertical_motors", Int32, queue_size=10)

print("Creating dictionary...")
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
print("Initializing ROS node...")
rospy.init_node("CommandMenu", anonymous=True)
print("Command Menu ready...")

while not rospy.is_shutdown():
    ''''
    print("Available Commands:")
    for command in commands:
        print(command)
    '''
    inp = input("Enter command: ")
    arguments = parse(inp)
    pub = publisher_dictionary[arguments[0]]
    pub.Publish(*arguments[1:])

"""
VERSION CONTROL:

1. April 21, 2018; 3:11pm; Carlos J. Figueroa
    Initial commit of the CommandMenu.py

"""