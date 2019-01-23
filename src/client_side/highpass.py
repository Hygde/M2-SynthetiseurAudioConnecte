import matplotlib.pyplot as plt
import numpy as np
from filter import *
import wave
import sys
import math
import contextlib

from scipy.signal import firwin, firwin2, lfilter, freqz

class Highpass(Filter):
	
    logger = logging.getLogger()
	
    def __init__(self, order, fc, fs, ftype):
        Audio.__init__(self)
        self.logger.debug("Initializing Highpass filter")
        self.cutOffFrequency = 100.0
        self.filtered = None

    def interpret_wav(self, raw_bytes, n_frames, n_channels, sample_width, interleaved = True):
        if sample_width == 1:
    	    dtype = np.uint8 # unsigned char
        elif sample_width == 2:
            dtype = np.int8 # signed 2-byte short
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats.")
        channels = np.fromstring(raw_bytes, dtype=dtype)
        if interleaved:
            # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
            channels.shape = (n_frames, n_channels)
            channels = channels.T
        else:
            # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
            channels.shape = (n_channels, n_frames)

        return channels

    def applyFilter(self, data):
        super(Highpass, self).applyFilter(data)

        channels = self.interpret_wav(data, self.bsize, self.nb_channel, pyaudio.get_sample_size(self.Format), True)
        freqRatio = (self.cutOffFrequency/self.RATE)
        a = [1]
        b = firwin(129, freqRatio, pass_zero=False)
        filtered = lfilter(b, a, channels)
        output = filtered.astype(np.float32).tostring()

        return output
