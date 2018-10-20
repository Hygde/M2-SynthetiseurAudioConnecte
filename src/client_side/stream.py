from client import Client
from audioplayer import AudioPlayer
from threading import Lock

class Stream(Client):
	
	def __init__(self, TCP, ip, port):
		Client.__init__(self, TCP, ip, port)
		self.audio = AudioPlayer()
		self.audio.createAudioPlayerStream()
		self.setDaemon(True)#detached thread
		self.lupdate = Lock()

	def setCanal(self, n):
		self.logger.debug("Updating the number of channels")
		self.lupdate.acquire()
		self.audio.setNumberOfChannels(n)
		self.audio.closeAudioPlayerStream()
		self.audio.createAudioPlayerStream()
		self.lupdate.release()

		
	def run(self):
		self.logger.debug("Playing stream !")
		while(self.continuer):
			try:
				self.lupdate.acquire()
				self.audio.play(self.sock.recv(self.audio.getBufferSize()))
				self.lupdate.release()
			except Exception as e:
				self.logger.error(e)
				self.audio.closeAudioPlayerStream()
				self.closeSocket()
