import pyaudio
from audio import Audio

#class Microphone
class Microphone(Audio):
	
	#constructor
	def  __init__(self):
		Audio.__init__(self)
		self.logger.debug("Initializing Microphone")
		
	#/* Implementation */
	
	def createMicroStream(self):
		self.audio = pyaudio.PyAudio()
		self.stream = self.audio.open(format=self.Format,channels=self.nb_channel,rate=self.RATE,input=True,frames_per_buffer=1)
		self.logger.debug("stream opened")
		
	def getDataFromBuffer(self):
		self.logger.debug("Microphone is getting a frame")
		return self.stream.read(self.bsize)
		
	def closeMicroStream(self):
		self.logger.debug("closing micro and stream")
		self.stream.stop_stream()
		self.stream.close()
		self.cleanup()
