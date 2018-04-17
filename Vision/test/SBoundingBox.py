import rospy
from std_msgs import Int32

rospy.init_node("SingleBoundingBox", anonymous = True)

boundingBoxPerc = 0.30
centroidX = rospy.wait_for_message("leCentre", Int32).data
imageSize = rospy.wait_for_message("imageSize", Int32).data
fovh = 80
errorPixels = (1-boundingBoxPerc)/imageSize
leftBound = imageSize * errorPixels

pub = rospy.Publisher("horizontal_controller", Int32)

while(not rospy.is_shutdown()):
    if centroidX < leftBound:
        pixels = (centroidX - leftBound)
        if (pixels > 0):
            pixels = pixels * -1
    elif centroidX > leftBound:
        pixels = 0

    fovErrorRatio = pixels / errorPixels
    fovErrorAngle = fovErrorRatio * fovh
    message = fovErrorAngle
    print("error: {}".format(message))
    pub.publish(message)  # Publishes the distance in pixels through ROS