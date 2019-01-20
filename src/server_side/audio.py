import pyaudio
import logging

class Audio:

	def __init__(self):
		self.logger = logging.getLogger()
		self.logger.debug("Initializing Audio")
		self.bsize = 2816#45056
		self.Format = pyaudio.paInt16
		self.nb_channel = 1
		self.RATE = 45056
		self.audio = None
		print(pyaudio.paInt16)

	def cleanup(self):
		self.logger.debug("Cleanup Audio")
		self.audio.terminate()

	#/* Setters */
		
	def setBufferSize(self, val):
		self.logger.debug(val) 
		self.bsize = val
		
	def setNumberOfChannels(self, val):
		self.logger.debug(val)
		self.nb_channel = val
		
	def setRate(self, val):
		self.logger.debug(val)
		self.RATE = val
		
	def setFormat(self, val):
		self.logger.debug(val)
		self.Format = val
		
	#/* Getters */

	def getBufferSize(self):
		self.logger.debug(self.bsize)
		return self.bsize
		
	def getNumberOfChannels(self):
		self.logger.debug(self.nb_channel)
		return self.nb_channel
		
	def getRate(self):
		self.logger.debug(self.RATE)
		return self.RATE
		
	def getFormat(self):
		self.logger.debug(self.Format)
		return self.Format
