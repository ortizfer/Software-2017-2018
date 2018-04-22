import rospy
from std_msgs import Int32, Float32
from rumarino_package.msg import ForwardsCommand, Centroid

# Initializes the node
rospy.init_node("SingleBoundingBox", anonymous = True)

# Limits the bounding box to a 30% to the right
# Hard-coded value subjected to further modification
boundingBoxPerc = 0.30

# Information to be received from vision
imageSize = rospy.wait_for_message("imageSize", Int32).data

# Miscellaneous parameters
fovh = 80
errorPixels = (1-boundingBoxPerc)/imageSize
leftBound = imageSize * errorPixels

# Defines the respective publishers
alignPub = rospy.Publisher("align_set_point", Float32, timeout=5)
forwardPub = rospy.Publisher("forwards_command", ForwardsCommand, timeout=5)

while(not rospy.is_shutdown()):

    # Waits for centroid to be received
    centroid = rospy.wait_for_message("centroid_topic", Centroid, timeout=5)

    # Fixates the x coordinate of the coordinate being received
    x = centroid.x

    if centroid < leftBound: # Object is to the left of the bounding box
        pixels = (centroid - leftBound)
        if (pixels > 0):
            pixels = pixels * -1

        forwardPub.publish(20, True) # Moves and tries to align
        alignPub.publish(5, True)    # within the boundary

    elif centroid > leftBound: # Object is within the bounds
        pixels = 0
        forwardPub.publish(20, True)

    # Error calculations
    # fovErrorRatio = pixels / errorPixels
    # fovErrorAngle = fovErrorRatio * fovh
    # message = fovErrorAngle
    # print("error: {}".format(message))
    # pub.publish(message)  # Publishes the distance in pixels through ROS

