#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Gabs & Sachy & Chris
"""
from Utils.Dice import Dice

from Utils import RosCom

camCenterX = 640/2
camCenterY = 480/2

visionlist = [1,2,3,4,5,6]

Dice1 = Dice()
Dice2 = Dice()

center_x = visionlist.Dice.centroide[4]

def align():  # movement values need to be adjusted (authors: Angel B. y Fernando G.)
    current_depth = RosCom.getDepth()
    set_center()
    if center_x < camCenterX and center_y < camCenterY:
        RosCom.Left(1)
        RosCom.setDepth(current_depth - 1)
    elif center_x < camCenterX and center_y > camCenterY:
        RosCom.Left(1)
        RosCom.setDepth(current_depth + 1)
    elif center_x > camCenterX and center_y > camCenterY:
        RosCom.Right(1)
        RosCom.setDepth(current_depth + 1)
    elif center_x > camCenterX and center_y < camCenterY:
        RosCom.Right(1)
        RosCom.setDepth(current_depth - 1)
    elif center_x == camCenterX and center_y < camCenterY:
        RosCom.setDepth(current_depth - 1)
    elif center_x == camCenterX and center_y > camCenterY:
        RosCom.setDepth(current_depth + 1)
    elif center_x < camCenterX and center_y == camCenterY:
        RosCom.Left(1)
    elif center_x > camCenterX and center_y == camCenterY:
        RosCom.Right(1)
# return true if found 3 dice, false if found less than 3
def check_3():
    counter = 0
    for x in range(0, 5):
        if visionlist[x] != None:
            counter+=1
    if counter >= 3:
        return True
    else:
        return False


def start(visionlist):
    for Dice in visionlist:
        if x. == 5:
            for Dice y in visionlist:
                if y.number == 6:

                    centerofdice5 = visionlist.Dice.centroide{4}
                    leftmovement5 = 320 - centerofdice5{0}
                    rightmovement5 = centerofdice5{0} - 320
                    updepth5 = 240 - centerofdice5{1}
                    downdepth5 = centerofdice5{1} - 240

                    if centerofdice5{0} > 320 and centerofdice5{1} > 240:
                        RosCom.left(leftmovement5)
                        RosCom.depth(downdepth5)
                        RosCom.forward()
                        RosCom.backward()
                        RosCom.depth(downdepth5)
                        RosCom.right(leftmovement5)
                    elif centerofdice5 < 320:
                        RosCom.right(rightmovement5)
                        RosCom.forward()
                        RosCom.backward()
                        RosCom.left(rightmovement5)
                    else:
                        RosCom.forward()


                elif y.number == 2:
                    missionlogic

        elif x.number == 6:
            for Dice y in visionlist:
                if y.number == 1:
                    missionlogic

        elif x.number == 3:
            for Dice y in visionlist:
                if y.number == 4
                    missionlogic
