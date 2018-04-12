#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

;)
@author: Gabriel Valentin
"""


class Dice:

    def __init__(self):

        self.centx = 0
        self.centy = 0
        self.boundingBox = 0 #needs update
        self.value = 0

    def set_centx(self, received):
        self.centx = received

    def set_centy(self, received):
        self.centy = received

    def set_bounding(self, received):
        self.boundingBox = received

    def set_value(self, received):
        self.value = received

    def get_centx(self):
        return self.centx

    def get_centy(self):
        return self.centy

    def get_bounding(self):
        return self.boundingBox

    def get_value(self):
        return self.value
