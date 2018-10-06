import pyaudio
import logging

class Audio:

	def __init__(self):
		self.logger = logging.getLogger()
		self.logger.debug("Initializing Audio")
		self.audio = pyaudio.PyAudio()
		self.bsize = 1024
		self.Format = pyaudio.paInt16
		self.nb_channel = 1
		self.RATE = 45056
		print(pyaudio.paInt16)
		
	def cleanup(self):
		self.logger.debug("Cleanup Audio")
		self.audio.terminate()

	#/* Setters */
		
	def setBufferSize(self, val):
		self.logger.debug("Microphone buffer size :", val) 
		self.bsize = val
		
	def setNumberOfChannels(self, val):
		self.logger.debug("Microphone number of channels = ", val)
		self.nb_channel = val
		
	def setRate(self, val):
		self.logger.debug("Microphone rate : ", val)
		self.RATE = val
		
	def setFormat(self, val):
		self.logger.debug("Microphone format = ", val)
		self.Format = val
		
	#/* Getters */

	def getBufferSize(self):
		self.logger.debug("Microphone buffer size = ", self.bsize)
		return self.bsize
		
	def getNumberOfChannels(self):
		self.logger.debug("Microphone number of channels = ", self.nb_channel)
		return self.nb_channels
		
	def getRate(self):
		self.logger.debug("Microphone rate = ", self.rate)
		return self.rate
		
	def getFormat(self):
		self.logger.debug("Microphone format = ", self.Format)
		return self.Format
