import numpy as np
import wave
from audio import *

class WaveGeneration(Audio):
    """docstring for WaveGeneration"""
    def __init__(self, rate, freq):
        super(WaveGeneration, self).__init__()
        Audio.__init__(self)
        self.wav_file = wave.open('sound.wav', 'wb')
        self.wav_file.setnchannels(self.getNumberOfChannels())
        self.wav_file.setsampwidth(pyaudio.get_sample_size(self.getFormat()))
        self.wav_file.setframerate(self.getRate())

    def write(self, data):
        self.wav_file.writeframes(data)

    def cleanup(self):
        self.wav_file.close()