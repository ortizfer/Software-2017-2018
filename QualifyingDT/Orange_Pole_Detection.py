import cv2
import numpy as np
import glob


def obj_detect(contours):
    """
    This function will determine wheter or not an object is detected.
    The approach consists on determining if one contour is detected. If the condition is met,
    assign a value (a different value for each condition). This value is returned and used to determine
    if the algorithm should continue or not.
    """
    # only proceed if at least one contour is found
    if len(contours) > 0:
        area = 1
    else:
        area = 0
    return area

#This is a list that contains the path for each image as a string value. Alternative of reading video.
filenames = [img for img in glob.glob("/home/emmanuel/Downloads/markerfotos/*.jpg")] #change path to folder containing images.
filenames.sort() # Sort images in ascending order

#Loop through each image
for n in filenames:
    #Read image
    img = cv2.imread(n)
    #img = cv2.resize(img,(640,480)) #Resize image to 640x480 if neccesary
    bilfilter = cv2.bilateralFilter(img, 5, 300, 300)  # Noise reduction using a bilateral filter.

    hsv = cv2.cvtColor(bilfilter,cv2.COLOR_BGR2HSV) #BGR to HSV Conversion

    #HSV threshold values
    lower_color = np.array([9,26,15], dtype = 'uint8')
    upper_color = np.array([74,190,193], dtype = 'uint8')

    mask = cv2.inRange(hsv, lower_color, upper_color) #image segmentation

    #Morphological Function
    kernel = np.ones((5, 5), np.uint8)  #Rectangular kernel
    close=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  #Closing is reverse of Opening, Dilation followed by Erosion.

    #Finding Countours
    _, contours,_ = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Determine if an oject is detected
    A = obj_detect(contours)

    if A == 1:
        cnt = max(contours, key=cv2.contourArea) #filter contours by area. Find biggest area.

        #Create bounding box around object
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int64(box)
        cv2.drawContours(img, [box], 0, (0, 0, 255), 2) #draw box in the image

        #Center coordinates of the object
        c_x=int((box[3][0]+box[1][0])/2)
        c_y=int((box[1][1]+box[3][1])/2)

        cv2.circle(img, (c_x,c_y), 7, (255, 255, 255), -1) #draw center point
        cv2.imshow("frame",img)
        cv2.waitKey(30)

    elif A == 0:
         print("No Object Detected")