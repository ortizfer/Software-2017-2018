"""
    Part of the Duct Tape series, this codes purpose is to direct the AUV
    around a static pole using two bounding boxes  during  the qualifying
    round. It assumes the camera will be facing the right.
"""



import rospy
from std_msgs.msg import Int32, Float32
from rumarino_package.msg import ForwardsCommand, Centroid
import time
rospy.init_node("DoubleBoundingBox", anonymous=True)
centroid_topic = "Centroid_Test"

angle = 8.0
fwd = -15
boundingBoxPerc = 0.20
imageSize = 640 #rospy.wait_for_message("imageSize", Int32, ).data
boundingBoxSize = imageSize*boundingBoxPerc
rightBound = (imageSize + boundingBoxSize)/2
leftBound = (imageSize - boundingBoxSize)/2
rot = rospy.Publisher("align_set_point", Float32, queue_size = 10)
mov = rospy.Publisher("forwards_command", ForwardsCommand, queue_size = 10)

current_heading = rospy.wait_for_message("align_current", Float32).data
target_heading = (current_heading+180)%360

print("INITIALIZED")
while not rospy.is_shutdown() and current_heading != target_heading:
    current_heading = rospy.wait_for_message("align_current", Float32, timeout=5)
    centroid = rospy.wait_for_message(centroid_topic, Centroid, timeout=5)
    if centroid is not None:
        x = centroid.x
        if x > rightBound:  # Stop forward movement and Rotate to the right
            mov.publish(0, True)
            rot.publish(angle)
            print('Stop Forwards, rotate to the right')
        elif leftBound < x < rightBound:  # Move forward, rotate less degrees
            mov.publish(fwd, True)
            rot.publish(angle/2.0)
            print('Move Forwards, rotate less degrees')
        elif x < leftBound:  # Move forward
            mov.publish(fwd, True)
            print('move forwards')
        time.sleep(0.30)
    else:
        print("OBJECT NOT DETECTED: Start panicking...")

mov.Publish(0, True)  # Stop movement before ending, mission

"""
VERSION CONTROL:

    1. April 20, 2018; 2:34am; Carlos J. Figueroa
        Initial commit of DBoundingBox.py
"""
