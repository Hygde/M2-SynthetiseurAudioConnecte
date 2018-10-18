from audio import *

class AudioPlayer(Audio):
	
	logger = logging.getLogger()
	
	def __init__(self):
		Audio.__init__(self)
		self.logger.debug("Initializing AudioPlayer")
		
	def createAudioPlayerStream(self):
		self.logger.debug("Creating AudioPlayer")
		self.stream = self.audio.open(format=self.Format, channels=self.nb_channel, rate=self.RATE, output=True)
		
	def play(self, data):
		self.stream.write(data)
		
	def closeAudioPlayerStream(self):
		self.logger.debug("Closing audioplayer stream")
		self.stream.stop_stream()
		self.stream.close()
		self.cleanup()
