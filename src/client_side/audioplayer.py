from audio import *
from wavefile import *

class AudioPlayer(Audio):
	
    logger = logging.getLogger()
	
    def __init__(self):
        Audio.__init__(self)
        self.logger.debug("Initializing AudioPlayer")
		
    def createAudioPlayerStream(self):
        self.logger.debug("Creating AudioPlayer")
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.Format, channels=self.nb_channel, rate=self.RATE, output=True)
        self.generation = WaveGeneration(self.RATE, 440.0)

    def play(self, data):
        self.stream.write(data)
        self.generation.write(data)
		
    def closeAudioPlayerStream(self):
        try:
            self.logger.debug("Closing audioplayer stream")
            self.stream.stop_stream()
            self.stream.close()
            self.generation.cleanup()
            self.cleanup()
        except AttributeError as e:
            self.logger.warning(e)
