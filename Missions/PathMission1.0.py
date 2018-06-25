from Utils import RosCom
import numpy as np
import rospy
from Utils.Path import *


"""@authors Karinne and Christian"""
""" 
    1st style: 
        Using the intercepts of the path lines with the edges of the camera box. With this
        intercepts we can check if the sub is aligned or not and if it is not aligned using 
        the numpy libray we can align it
"""


v_max = 60  # x coordinates of the max vertical bounding box
v_min = 40  # x coordinates of the min vertical bounding box
h_min = 45  # y coordinate for the min horizontal bounding box
h_max = 55  # y coordinate for the max horizontal bounding box
# x and y coordinate set for top and bottom intercepts
top_x = 0
top_y = 0
bottom_x = 0
bottom_y = 0


def mission_on():
    # it should return true while the camera does not detect any intercepts in the top edge or
    # while the centroid in the path end is not inside the center boundary box
    return


def check_align(bottom_x, bottom_y, top_x, top_y):
    if bottom_x != top_x:
        # calculate angle using tangent
        coordinates = [bottom_x-top_x, bottom_y-top_y]
        angle = calc_phi(coordinates)
        if bottom_x > top_x:
            return [-angle, bottom_x, top_x]
        else:
            return [np.abs(angle), bottom_x, top_x]
    return 0  # angle for sub to align, 0 if there is no need for alignment


def run():
    while mission_on():
        if bottom_x < v_min and top_x > v_max:
            check_align(bottom_x, bottom_y, top_x, top_y)
            # move forward
        elif bottom_x > v_max and top_x < v_min:
            check_align(bottom_x, bottom_y, top_x, top_y)
            # move forward
        elif bottom_x < v_min or top_x < v_min:
            check_align(bottom_x, bottom_y, top_x, top_y)
            # move forward
        elif bottom_x > v_max or top_x > v_max:
            check_align(bottom_x, bottom_y, top_x, top_y)
            # move forward
        elif bottom_x < v_min and top_x < v_min:
            x = v_min + ((v_max - v_min) / 2)
            check_align(bottom_x, bottom_y, x, top_y)
            # move forward
        elif bottom_x > v_max and top_x > v_max:
            x = v_min + ((v_max - v_min) / 2)
            check_align(x, bottom_y, top_x, top_y)
            # move forward


def calc_phi(v):
    if v[0] > 0:
        return np.arctan(v[1] / v[0])
    else:
        if v[1] > 0:
            if v[0] < 0:
                return np.pi + np.arctan(v[1] / v[0])
            else:
                return np.pi
        elif v[1] < 0:
            if v[0] < 0:
                return -np.pi + np.arctan(v[1] / v[0])
            else:
                return -np.pi
        else:
            return 0.0


#  OLD ALGORITHM USING LINES LENGTH
# # RosCom.setDepth(1, 13.00) specify and set depth
# align = 0  # set angle
# path_mission = True
#
#
# lines_length = []  # Get vision
# line_a = lines_length[0]  # leftmost
# line_b = lines_length[1]  # rightmost
#
# # There is a difference of 0.89 ft between the depth path and the depth of the sub, the
# #  will be 0.89 ft above the path. This should the optimal depth fo the sub to gather
# #  the data necessary for this mission
#
#
# # while path mission is true
# # def run():
# #     while True:
# #         # updateLines()
# #         if line_a - line_b >= 1.00:
# #             if line_a > line_b:
# #                 align = align + get_angle()
# #                 # RosCom.headingMotors(1, 7, align) # 7 is for eliminating
# #                 # compiler errors, don't know what should go there
# #                 # Tell ros to align sub to the new angle
# #                 RosCom.moveForward(35)
# #             elif line_b > line_b:
# #                 align = align - get_angle()
# #                 # RosCom.headingMotors(1, 7, align)
# #                 # Tell ros to align sub to the new angle
# #                 RosCom.moveForward(35)
# #         else:
# #             # If the difference between lines lengths is less than 1, then continue to move forward
# #             RosCom.moveForward(25)
