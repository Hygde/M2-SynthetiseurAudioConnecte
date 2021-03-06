from client import Client
from audioplayer import AudioPlayer
from threading import Lock
from filter import Filter
from lowpass import Lowpass
from highpass import Highpass
import numpy as np
import time

class Stream(Client):
	
	def __init__(self, TCP, ip, port):
		Client.__init__(self, TCP, ip, port)
		self.audio = AudioPlayer()
		self.audio.createAudioPlayerStream()
		self.setDaemon(True)#detached thread
		self.lupdate = Lock()
		self.filter = None

	def setCanal(self, n):
		self.logger.debug("Updating the number of channels")
		self.lupdate.acquire()
		self.audio.setNumberOfChannels(n)
		self.audio.closeAudioPlayerStream()
		self.audio.createAudioPlayerStream()
		self.lupdate.release()

	def updateFilter(self, i):
		if(i<1 or i>2):self.filter = None#update this cond
		elif(i == 1):
			self.filter = Highpass(3, 1000, self.audio.getRate(), "highpass")
			#self.filter.designFilter()
		elif(i == 2):
			self.filter = Lowpass(3, 1000, self.audio.getRate(), "lowpass")
			#self.filter.designFilter()
		#todo add crowd filter

	def cleanup(self):
		self.audio.closeAudioPlayerStream()
		self.closeSocket()
		
	def run(self):
		self.logger.debug("Playing stream !")
		while(self.continuer):
			try:
				data = self.sock.recv(self.audio.getBufferSize())
				self.logger.debug(data)
				if(data == b'CLOSE'):self.continuer = False
				else:
					self.lupdate.acquire()
					if(not(self.filter == None)):data = self.filter.applyFilter(data)
					self.audio.play(data)
					self.lupdate.release()
			except Exception as e:
				self.logger.error(e)
				self.continuer = False
