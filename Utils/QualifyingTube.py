#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author:
"""



class QTube:

    tubeDiameter = 0.0762
    allowableTubeApproach = 1

    def __init__(self):
        tubeApproach = 5
        xTubeDist = -3

    def settubeApproach(self,recieved):
        self.tubeApproach = recieved

    def gettubeApproach(self):
        return self.tubeApproach