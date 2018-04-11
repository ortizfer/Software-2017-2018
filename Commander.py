#!/usr/bin/env python

"""
    The file Commander.py  is intended to run as the ROS master node.
    It fetches the time  from the ROS  Topic  time_inquiry.  Based on
    The pre-established ranges, the Commander execute  a fixed set of
    missions. The less time the Commander is given, the less missions
    it will run.
"""


import rospy
from std_msgs.msg import String

# ##########-Utils-##########


# get_missions accepts an integer, representing remaining mission time, and returns truth values
# corresponding to the missions that can be executed.
def get_missions(remaining_time):
    x = remaining_time
    if 15*60 >= x > 8*60:
        return [True, True, True, True]  # Corresponds to: Gate, Path, Dice, Path
    elif 8*60 >= x > 3*60:
        return [True, False, True, False]  # Corresponds to: Gate, Dice
    elif 3*60 >= x > 0:
        return [True, False, False, False]  # Corresponds to: Gate
    else:
        return [False, False, False, False]  # Corresponds to: NO MISSIONS


# ##########-Script-##########
print('Starting Commander')
rospy.init_node('commander', anonymous=True)  # Initialize ROS Node
print('Waiting for time...')
message = rospy.wait_for_message('time_response', String)  # Gets remaining time from Adaptive_Timer
missions = get_missions(int(message.data))  # Gets an array of missions to run


if missions[0]:  # Gate
    print("Starting Gate Mission...")
    # run Gate Mission
if missions[1]:  # Path
    print("Starting Path Mission...")
    # run Path Mission
if missions[2]:  # Dice
    print("Starting Dice Mission...")
    # run Dice Mission
if missions[3]:  # Path
    print("Starting path Mission...")
    # run Path Mission

print("Mission Array completed.")
