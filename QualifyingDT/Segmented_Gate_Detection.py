#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:11:53 2018


@author: Emmanuel A. Mendez Alicea
         emmanuel.mendez3@upr.edu

         This code will process a segmented gate
"""


import cv2
import numpy as np
import glob
import rospy
from rumarino_package.msg import Centroid

pub = rospy.Publisher("Gate_Centroid", Centroid)

#Global Parameters
#Functions
def img_pre_proc(img):
    """ Pre-process image
    """
    #img = cv2.resize(img,(640,480)) #Resize image to 640x480
    #img = cv2.GaussianBlur(img, (11, 11), 0) #Gaussian Filter
    img_proc = img
    return img_proc

def find_contours(segmented):
    """Find Contours
    """
    _,contours,_ = cv2.findContours(segmented,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    return contours

def color_seg(img,color):
    """ This function does color filtering depending on the threshold parameters
    """
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#BGR to HSV conversion

    if color == 1:
        #Path color parameters (Red)
        lower_color = np.array([65,55,110], dtype = 'uint8')
        upper_color = np.array([77,235,175], dtype = 'uint8')

    elif color == 2:
        #Path color parameters (Orange)
        lower_color = np.array([30,65,110], dtype = 'uint8')
        upper_color = np.array([70,235,175], dtype = 'uint8')

    # Construct a mask for the desired color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    #Morphological Functions
    # Perform a series of dilations and erosions to remove any small
    # blobs left in the mask
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return mask

def img_crop(img):
    """
    Crop image vertically by half
    """

    left_roi=img[0:480, 0:320] #Numpy slicing. Cut detected object
    right_roi = img[0:480, 320:640]

    return left_roi, right_roi

def obj_detect(contours):
    """
    This function will determine wheter or not an object is detected.
    The approach consists on determining if one contour is detected. If the condition is met,
    assign a value (a different value for each condition). This value is returned and used to determine
    if the algorithm should continue or not. Errors will be obatined if an image with no orange object is
    input in the algorithm. To avoid this errors we do this approach.

    """
    global area
    # only proceed if at least one contour was found
    # This is just for testing.
    if len(contours) > 0:
        area = 1
    else:
        area = 0
    return area

def img_drawing(img, cnt_l, cnt_r):
    """
    This function draw a bounding box in the detected gate.
    """

    #Draw rectangle around detected object
    cnt_right = max(cnt_r, key=cv2.contourArea)
    cnt_left = max(cnt_l, key=cv2.contourArea)
    x1,y1,w1,h1 = cv2.boundingRect(cnt_left)
    x2,y2,w2,h2 = cv2.boundingRect(cnt_right)

#    cv2.rectangle(img,(x1,y1-50),(x2+w2+320,y2+h2+50),(255,0,0),2)

    a = int(x2+w2+320) #320 is the cut value
    b = int(y2+h2+50) #50 is value due to the back section of the gate
    c = int(y1-50)

    #draw bounding box
    cv2.rectangle(img,(x1,y1-50),(a,b),(0,0,0),2)
#    cv2.rectangle(img,(a,c),(x2+w2+320,b),(0,0,255),2)

    #Text
#    cv2.putText(img,'Red', (a+50, y2+100), cv2.FONT_HERSHEY_SIMPLEX, 0.65,(0,0,255),1,cv2.LINE_AA)
#    cv2.putText(img,'Black', (x1+50, y1+140), cv2.FONT_HERSHEY_SIMPLEX, 0.65,(0,0,0),1,cv2.LINE_AA)
#
#    #Center Points
    x_center = int((x1 + a) / 2)
    y_center = int((y1-50+b) / 2)
    cv2.circle(img, (x_center, y_center), 7, (255, 255, 255), -1) #draw center point
    pub.publish(x_center, y_center) #publishes the centroid


    return img


'---------------------------------------- Main ------------------------------------'

#This is a list that contains the path for each image as a string value
filenames = [img for img in glob.glob("/home/emmanuel/Downloads/segmented_gate/*.jpg")] #change path if necessary
filenames.sort() # Sort images

#cap = cv2.VideoCapture(0)
# Access and loop through each image to be analyzed
for n in filenames:
#while(True):
#    _, img = cap.read()
    img = cv2.imread(n) #read image
#    img = cv2.resize(img,(640,480)) #Resize image to 640x480
    height, width = img.shape[:2]
    #Separate desired object from the background using color filtering
    segmented_orange = color_seg(img,1) #Look for anything orange (biggest area in object)

    #Find contours
    contours = find_contours(segmented_orange) #Find Contours

    #Determine if an oject is detected
    A = obj_detect(contours)

    if A == 1:

        #Numpy slicing. Cut image in half vertically
        left_roi=img[0:height, 0:320]
        right_roi = img[0:480, 320:640]

        segmented_left = color_seg(left_roi,1)
        segmented_right = color_seg(right_roi,2)

        contours_left = find_contours(segmented_left)
        contours_right = find_contours(segmented_right)

        draw_img = img_drawing(img,contours_left,contours_right)

        cv2.imshow("frame",draw_img)
        cv2.waitKey(0)


    elif A == 0:
        print("No Object Detected")
