#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

sup
@author: Gabriel, Fernando G. & Angel

Here we are gonna start defining variables and imports
"""
from Utils.Dice import Dice
from time import *
from Utils import RosCom

"""Tells VISION with mission we are"""
Roscom.setVisionMission(3)

camCenterX = 640/2
camCenterY = 480/2

visionlist = [1,2,3,4,5,6]

Dice1 = Dice()
Dice2 = Dice()

def run_Dice():
    counter = 0
    while check_pair() == 0:
        forward_sleep(30,1)
        counter +=1
        if counter==5:
            print("mission failed we'll get em next time")
            break
    while check_bigdice(Dice1):#break while when dice is biggerthan boundingbox
        if check_binding_box(Dice1):
            forward_sleep(40,2)
        else:
            align()
        update_dice(Dice1)
    forward_sleep(40,3)
    backward_sleep(40,6) #retrace steps
    update_dice(Dice2)
    while check_bigdice(Dice2):#break while when dice is biggerthan boundingbox
        if check_binding_box(Dice2):
            forward_sleep(40,2)
        else:
            align()
        update_dice(Dice2)
    forward_sleep(40,3)
    #sets finised state, end



""""This is the self-alignment program"""
def align(Dice):  # movement values need to be adjusted
    current_depth = RosCom.getDepth()
    update_dice(Dice)
    if Dice.get_centx() < camCenterX and Dice.get_centy() < camCenterY:
        left_sleep(40,1)
        RosCom.setDepth(current_depth - 1)
    elif Dice.get_centx() < camCenterX and Dice.get_centy() > camCenterY:
        left_sleep(40,1)
        RosCom.setDepth(current_depth + 1)
    elif Dice.get_centx() > camCenterX and Dice.get_centy() > camCenterY:
        right_sleep(40,1)
        RosCom.setDepth(current_depth + 1)
    elif Dice.get_centx() > camCenterX and Dice.get_centy() < camCenterY:
        right_sleep(40,1)
        RosCom.setDepth(current_depth - 1)
    elif Dice.get_centx() == camCenterX and Dice.get_centy() < camCenterY:
        RosCom.setDepth(current_depth - 1)
    elif Dice.get_centx() == camCenterX and Dice.get_centy() > camCenterY:
        RosCom.setDepth(current_depth + 1)
    elif Dice.get_centx() < camCenterX and Dice.get_centy() == camCenterY:
        left_sleep(40,1)
    elif Dice.get_centx() > camCenterX and Dice.get_centy() == camCenterY:
        right_sleep(40,1)

""""Here we are gonna check all patterns possible for 7 and 11, if such pattern exists then we go with that one"""
def check_pair():
    if visionlist[4] is not None and visionlist[5] is not None:
        Dice1.set_centx(visionlist[4].getcentx()) #upadte for vision
        Dice1.set_centy(visionlist[4].getcenty())  # upadte for vision
        Dice1.set_value(5)
        Dice1.set_boundingbox(visionlist[4].getbounding) #needs update
        Dice2.set_centx(visionlist[5].getcentx())  # upadte for vision
        Dice2.set_centy(visionlist[5].getcenty())  # upadte for vision
        Dice2.set_value(6)
        Dice2.set_boundingbox(visionlist[5].getbounding)  # needs update
        return 11
    elif visionlist[5] is not None and visionlist[0]is not None:
        Dice1.set_centx(visionlist[0].getcentx())  # upadte for vision
        Dice1.set_centy(visionlist[0].getcenty())  # upadte for vision
        Dice1.set_value(1)
        Dice1.set_boundingbox(visionlist[0].getbounding)  # needs update
        Dice2.set_centx(visionlist[5].getcentx())  # upadte for vision
        Dice2.set_centy(visionlist[5].getcenty())  # upadte for vision
        Dice2.set_value(6)
        Dice2.set_boundingbox(visionlist[5].getbounding)  # needs update
        return 7
    elif visionlist[4] is not  None and visionlist[1] is not None:
        Dice1.set_centx(visionlist[4].getcentx())  # upadte for vision
        Dice1.set_centy(visionlist[4].getcenty())  # upadte for vision
        Dice1.set_value(5)
        Dice1.set_boundingbox(visionlist[4].getbounding)  # needs update
        Dice2.set_centx(visionlist[1].getcentx())  # upadte for vision
        Dice2.set_centy(visionlist[1].getcenty())  # upadte for vision
        Dice2.set_value(2)
        Dice2.set_boundingbox(visionlist[1].getbounding)  # needs update
        return 7
    elif visionlist[2] is not None and visionlist[3] is not None:
        Dice1.set_centx(visionlist[2].getcentx())  # upadte for vision
        Dice1.set_centy(visionlist[2].getcenty())  # upadte for vision
        Dice1.set_value(3)
        Dice1.set_boundingbox(visionlist[2].getbounding)  # needs update
        Dice2.set_centx(visionlist[3].getcentx())  # upadte for vision
        Dice2.set_centy(visionlist[3].getcenty())  # upadte for vision
        Dice2.set_value(4)
        Dice2.set_boundingbox(visionlist[3].getbounding)  # needs update
        return 7
    else:
        return 0


def check_bigdice(Dice):  # checks 4 out of bound dice

    return True

def forward_sleep(intensity, timer):
    RosCom.moveForward(intensity)
    time.sleep(timer)
    RosCom.moveForward(0)

def backward_sleep(intensity, timer):
    RosCom.moveBackward(intensity)
    time.sleep(timer)
    RosCom.moveBackward(0)

def left_sleep(intensity, timer):
    RosCom.headingMotors(1, 0,90)#rotate 90 counterclockwise
    RosCom.moveForward(intensity)
    time.sleep(timer)
    RosCom.moveForward(0)
    RosCom.headingMotors(1, 0, -90)  # rotate 90 clockwise

def right_sleep(intensity, timer):
    RosCom.headingMotors(1, 0, -90)  # rotate 90 clockwise
    RosCom.moveForward(intensity)
    time.sleep(timer)
    RosCom.moveForward(0)
    RosCom.headingMotors(1, 0, 90)  # rotate 90 counterclockwise

def update_dice(Dice): #update for vision
    Dice.set_centx(visionlist[Dice.get_value-1].getcentx)
    Dice.set_centy(visionlist[Dice.get_value - 1].getcenty)
    Dice.set_boundingbox(visionlist[Dice.get_value - 1].getbounding)

def check_binding_box(Dice):
    update_dice(Dice)
    if (camCenterX-50) < Dice.get_centx() < (camCenterX+50) and (camCenterY-50) < Dice.get_centx() < (camCenterY+50):
        return True
    return False
