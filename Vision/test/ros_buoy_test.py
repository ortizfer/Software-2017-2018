#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 07:45:58 2018

@author: eric
"""

import cv2
import numpy as np
import time
import rospy
from std_msgs.msg import Float64

# Bounding Parameters
bounding_box_percent = 0.2
fovh = 80 # Field of View Horizontal
fovv = 64 # Field of View Vertical
# ROS NODE INIT
pub = rospy.Publisher("visionAngleChatter", Float64, queue_size=5)
rospy.init_node("visionTest", anonymous=True)

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('/home/nvidia/ros/visionTest3.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened() and not rospy.is_shutdown()):
  # Capture frame-by-frame
    ret, img = cap.read()
    cv2.waitKey(1)
    img_height, img_width, _ = img.shape
    error_pixels = (1-bounding_box_percent)/2*img_width

    bounding_box_width = img_width*bounding_box_percent
    im_line_1 = int((img_width-bounding_box_width)/2)
    im_line_2 = int((img_width+bounding_box_width)/2)
    cv2.namedWindow("ROS_VISION_TEST", cv2.WINDOW_NORMAL)

    if ret:
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#BGR to HSV-Space conversion
        
        #Path color parameters (yellow-green) 
        #lower_color = np.array([0,30,30], dtype = 'uint8')
        #upper_color = np.array([70,180,255], dtype = 'uint8')
        
        #Thresholding parameters (Red) 
        lower_color = np.array([160,40,170], dtype = 'uint8')
        upper_color = np.array([190,255,255], dtype = 'uint8')
                 
        #Image Segmentation
        # Construct a mask for the desired color
        mask = cv2.inRange(hsv, lower_color, upper_color)
        
        #Morphological Functions
        # Perform a series of dilations and erosions to remove any small
        # blobs left in the mask
        kernel = np.ones((9,9),np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        #Find Contours
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
               
        # only proceed if at least one contour was found
        if len(contours) > 0:
            # find the largest contour in the mask, then use it to compute the minimum 
            # enclosing circle and centroid
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
               
            # Only proceed if the radius meets a minimum size. Change/Correct this value for your obect's size
            if radius > 0.5:
                # Draw the circle based on the centroid on the image
                cv2.circle(img, (int(x), int(y)), int(radius),(0,255,255), 2)
                cv2.circle(img, (int(x), int(y)), int(5),(0,255,255), 2)
               
            #Position alligment
            # The center is defined by two imaginary lines within the pixel coordinates of 160 and 480 (x-axis).
            # The user if notified if the object's center is out range, either too left or too right.
            # im_line_1 = 160
            # im_line_2 = 480
            #Draw imaginary line
            cv2.line(img, (im_line_1,0), (im_line_1, img_height), (0,255,255), 1, cv2.LINE_AA)
            cv2.line(img, (im_line_2,0), (im_line_2, img_height), (0,255,255), 1, cv2.LINE_AA)
        

            # Imaginary Line Comparison
            if x < im_line_1 :
                cv2.putText(img,'Position: Left', (500, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.55,(0,255,255),2,cv2.LINE_AA)
                #print("Move Right")
                pixels = (x-im_line_1)
                if(pixels > 0):
                    pixels = pixels*-1
            elif x > im_line_2 :
                cv2.putText(img,'Position: Right', (500, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.55,(0,255,255),2,cv2.LINE_AA)
                #print("Move Left")
                pixels = (x-im_line_2)
                if(pixels < 0):
                    pixels = pixels*-1
            elif x > im_line_1 and x < im_line_2:
                cv2.putText(img,'Position: Centered', (460, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.55,(0,255,255),2,cv2.LINE_AA)
                #print("Nigga you good")
                pixels = 0
            fov_error_ratio = pixels/error_pixels
            fov_error_angle = fov_error_ratio*fovh
            message = fov_error_angle
            print("error: {}".format(message))
            pub.publish(message) # Publishes the distance in pixels through ROS
        else:
            print("Nothing detected")
        cv2.imshow("ROS_VISION_TEST", img)

# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
print("FINISHED")
