import logging
import numpy as np
from scipy import signal

class Filter():

    def __init__(self, order, fc, fs, ftype):
        self.logger = logging.getLogger()
        self.forder = order
        self.Wn = float(fc)/fs
        self.btype=ftype
        self.logger.debug("order = %d Wn = %f type = %s", self.forder, self.Wn, self.btype)

    def designFilter(self):
        self.logger.debug("Creating the filter")
        self.b, self.a = signal.butter(self.forder, self.Wn, self.btype)

    def applyFilter(self, data):
        self.logger.debug("Applying the filter")
        return signal.filtfilt(self.b, self.a, data)