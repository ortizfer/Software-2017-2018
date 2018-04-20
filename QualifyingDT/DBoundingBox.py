"""
    Part of the Duct Tape series, this codes purpose is to direct the AUV
    around a static pole using two bounding boxes  during  the qualifying
    round. It assumes the camera will be facing the right.
"""


import rospy
from std_msgs import Int32, Float32
from rumarino_package.msg import ForwardsCommand, Centroid

rospy.init_node("DoubleBoundingBox", anonymous=True)

angle = -5.0
boundingBoxPerc = 0.20
imageSize = rospy.wait_for_message("imageSize", Int32, ).data
boundingBoxSize = imageSize*boundingBoxPerc
rightBound = imageSize-boundingBoxSize
leftBound = imageSize-2*boundingBoxPerc
rot = rospy.Publisher("align_set_point", Float32, timeout=5)
mov = rospy.Publisher("forwards_command", ForwardsCommand, timeout=5)

current_heading = rospy.wait_for_message("align_current", Float32).data
target_heading = (current_heading+180)%360


while not rospy.is_shutdown() and current_heading != target_heading:
    current_heading = rospy.wait_for_message("align_current", Float32, timeout=5)
    centroid = rospy.wait_for_message("Centroid_Pole_Side", Centroid, timeout=5)
    if centroid is not None:
        x = centroid.x
        if x > rightBound:  # Stop forward movement and Rotate to the right
            mov.Publish(0, True)
            rot.Publish(angle)
        elif leftBound < x < rightBound:  # Move forward, rotate less degrees
            mov.Publish(20, True)
            rot.Publish(angle/2.0)
        elif x < leftBound:  # Move forward
            mov.Publish(20, True)

    else:
        print("OBJECT NOT DETECTED: Start panicking...")

mov.Publish(0, True)  # Stop movement before ending, mission

"""
VERSION CONTROL:

    1. April 20, 2018; 2:34am; Carlos J. Figueroa
        Initial commit of DBoundingBox.py
"""