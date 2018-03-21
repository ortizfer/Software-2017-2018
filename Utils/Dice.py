#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

;)
@author: Gabriel Valentin
"""


class Dice:

    def __init__(self):

        self.centroid = (0,0)
        self.boundingBox = 0
        self.value = 5

    def set_centroid(self, recieved):
        self.centroid = recieved

    def set_bounding(self, recieved):
        self.boundingBox = recieved

    def set_value(self, recieved):
        self.value = recieved

    def get_centroid(self):
        return self.centroid

    def get_bounding(self):
        return self.boundingBox

    def get_value(self):
        return self.value
