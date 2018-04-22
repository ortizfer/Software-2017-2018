"""
    CommandMenu.py is a quick solution to remotely test and control
    the AUV through ROS topics.
"""

import inspect
import rospy
from std_msgs.msg import Int32, Float32, Bool
from rumarino_package.msg import Centroid, ControllerSetup, ForwardsCommand, HorizontalMotors


# ###########-UTILS-########### #
def parse(array):
    atr = []
    for element in array:
        if element == "t":
            atr.append(True)
        elif element == "f":
            atr.append(False)
        else:
            try:
                atr.append(float(element))
            except ValueError:
                atr.append(element)
    return atr

def print_dic(dictionary):
    atr = []
    for key in dictionary:
        atr.append(key)
    return atr
# ###########-Publishers-########### #
print("Creating publishers...")
align_controller_setup = rospy.Publisher("align_controller_setup", ControllerSetup, queue_size=10)
align_current = rospy.Publisher("align_current", Float32, queue_size=10)
align_error = rospy.Publisher("align_error", Float32, queue_size=10)
align_set_point = rospy.Publisher("align_set_point", Float32, queue_size=10)
depth_controller_setup = rospy.Publisher("depth_controller_setup", ControllerSetup, queue_size=10)
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
    "vm": vertical_motors,
    "help": "PRINTS COMMANDS",
    "exit": "CLOSE THE COMMAND MENU",
    "x": "EMERGENCY OFF",
}

# ###########-SCRIPT-########### #
print("Initializing ROS node...")
rospy.init_node("CommandMenu", anonymous=True)
print("Command Menu ready...")

exit_requested = False
while not rospy.is_shutdown() and not exit_requested:
    inp = raw_input("Enter command: ")
    if inp == "x":
        align_controller_setup.publish(False, False, -1, -1)
        depth_controller_setup.publish(False, False, -1, -1)
        vertical_motors(0)
        horizontal_motors(0, 0)
    elif inp == "help":
       dic = print_dic(publisher_dictionary)
       for entry in dic:
           print(entry)
    elif inp == "exit":
        exit_requested = True
    else:
        arguments = parse(inp.split(","))
        try:
            pub = publisher_dictionary[arguments[0]]
            pub.publish(*arguments[1:])
        except KeyError:
            print("Invalid Command: " + arguments[0])

        
"""
VERSION CONTROL:

1. April 21, 2018; 3:11pm; Carlos J. Figueroa
    Initial commit of the CommandMenu.py

"""
