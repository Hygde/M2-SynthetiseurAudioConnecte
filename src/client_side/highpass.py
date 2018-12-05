import matplotlib.pyplot as plt
import numpy as np
from filter import *
import wave
import sys
import math
import contextlib

class Highpass(Filter):
	
    logger = logging.getLogger()
	
    def __init__(self, order, fc, fs, ftype):
        Audio.__init__(self)
        self.logger.debug("Initializing Highpass filter")
        self.cutOffFrequency = 100.0
        self.filtered = None

    # from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean
    def running_mean(self, x, windowSize):
        cumsum = np.cumsum(np.insert(x, 0, 0)) 
        return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize

    # from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
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

        #sampleRate = self.RATE
        #nChannels = self.nb_channel
        #nFrames = self.bsize
        #ampWidth = pyaudio.get_sample_size(self.Format)

    	# Extract Raw Audio from multi-channel Wav File
    	#signal = spf.readframes(nFrames*nChannels)
    	#spf.close()
        channels = self.interpret_wav(data, self.bsize, self.nb_channel, pyaudio.get_sample_size(self.Format), True)

    	# get window size
    	# from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter
        freqRatio = (self.cutOffFrequency/self.RATE)
        N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)

        # Use moviung average (only on first channel)
        print(self.running_mean(channels[0], N).astype(channels.dtype))
        return (self.running_mean(channels[0], N).astype(channels.dtype))

