import cv2
import numpy as np
import rospy
from rumarino_package.msg import Centroid

pub = rospy.Publisher("Orange_Pole_Centroid", Centroid, queue=10)
rospy.init_node("Orange_Pole_Detector", anonymous=True)


def obj_detect(contour):
    """
    This function will determine wheter or not an object is detected.
    The approach consists on determining if one contour is detected. If the condition is met,
    assign a value (a different value for each condition). This value is returned and used to determine
    if the algorithm should continue or not.
    """
    # only proceed if at least one contour is found
    if len(contour) > 0:
        area = 1
    else:
        area = 0
    return area


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream or file")

# Loop through video feed
while not rospy.is_shutdown() and cap.isOpened():
    # Read image
    ret, img = cv2.read()
    # img = cv2.resize(img,(640,480)) #Resize image to 640x480 if neccesary
    bilfilter = cv2.bilateralFilter(img, 5, 300, 300)  # Noise reduction using a bilateral filter.

    hsv = cv2.cvtColor(bilfilter,cv2.COLOR_BGR2HSV)  # BGR to HSV Conversion

    # HSV threshold values
    lower_color = np.array([9,26,15], dtype='uint8')
    upper_color = np.array([74,190,193], dtype='uint8')

    mask = cv2.inRange(hsv, lower_color, upper_color)  # image segmentation

    # Morphological Function
    kernel = np.ones((5, 5), np.uint8)  # Rectangular kernel
    close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Finding Countours
    _, contours,_ = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Determine if an oject is detected
    A = obj_detect(contours)

    if A == 1:
        cnt = max(contours, key=cv2.contourArea) # filter contours by area. Find biggest area.

        # Create bounding box around object
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int64(box)

        # Center coordinates of the object
        c_x = int((box[3][0]+box[1][0])/2)
        c_y = int((box[1][1]+box[3][1])/2)
        pub.publish(c_x, c_y)
        cv2.waitKey(30)

    elif A == 0:
        pub.publish(-1, -1)
        print("No Object Detected")
