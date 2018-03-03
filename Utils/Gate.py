# !/usr/bin/env python2
#  -*- coding: utf-8 -*-
"""


@author: Fernando Guzman and Angel Burgos
"""


class Gate:
    def __init__(self):
        self.center_leftx = 0   # point to the center between the red strips
        self.center_lefty = 0

        self.center_rightx = 0  # point to the center between the black strips
        self.center_righty = 0

        self.centerx = 0    # point to the center
        self.centery = 0

        self.distance = 0   # distance to gate

    def setter_center_leftx(self, x):
        self.center_leftx = x

    def setter_center_lefty(self, y):
        self.center_lefty = y

    def setter_center_rightx(self, x):
        self.center_rightx = x

    def setter_center_righty(self, y):
        self.center_righty = y

    def setter_centerx(self, x):
        self.centerx = x

    def setter_centery(self, y):
        self.centery = y

    def setter_distance(self, d):
        self.distance = d

    def getter_center_leftx(self):
        return self.center_leftx

    def getter_center_lefty(self):
        return self.center_lefty

    def getter_center_rightx(self):
        return self.center_rightx

    def getter_center_righty(self):
        return self.center_righty

    def getter_centerx(self):
        return self.centerx

    def getter_centery(self):
        return self.centery

    def getter_distance(self):
        return self.distance
