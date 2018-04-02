#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

;)
@author: Gabriel Valentin
"""


class Dice:

    def __init__(self):

        self.centroid = (0, 0)
        self.boundingBox = 0
        self.value = 5

    def set_centroid(self, received):
        self.centroid = received

    def set_bounding(self, received):
        self.boundingBox = received

    def set_value(self, received):
        self.value = received

    def get_centroid(self):
        return self.centroid

    def get_bounding(self):
        return self.boundingBox

    def get_value(self):
        return self.value
