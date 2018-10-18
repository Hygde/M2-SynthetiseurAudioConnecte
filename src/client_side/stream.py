from client import Client
from audioplayer import AudioPlayer

class Stream(Client):
	
	def __init__(self, TCP, ip, port):
		Client.__init__(self, TCP, ip, port)
		self.audio = AudioPlayer()
		self.setDaemon(True)#detached thread
		
	def run(self):
		self.logger.debug("Playing stream !")
		while(self.continuer):
			try:
				self.audio.play(self.sock.recv(1024))
			except Exception as e:
				self.logger.error(e)
				self.closeSocket()
