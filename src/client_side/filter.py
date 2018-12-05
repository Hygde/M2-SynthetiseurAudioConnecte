import logging
import numpy as np
from audio import *

class Filter(Audio):

    def __init__(self, order, fc, fs, ftype):
        Audio.__init__(self)
        self.forder = order
        self.freqCoupure = float(fc)/fs
        self.logger.debug("order = %d Wn = %f type = %s", self.forder, self.Wn, self.btype)

    #def designFilter(self):
    #    self.logger.debug("Creating the filter")

    def applyFilter(self, data):
        self.logger.debug("Applying the filter")
