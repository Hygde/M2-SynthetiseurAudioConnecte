import logging
import time
from threading import Thread

from microphone import *

class ManageMicrophone(Thread):
	
	logger = logging.getLogger()

	def __init__(self, lock_clients, list_client):
		Thread.__init__(self)
		self.logger.debug("Initializing microphone thread")
		self.lock = lock_clients
		self.lclients = list_client
		self.mic = Microphone()
		self.mic.createMicroStream()
		
	def stop(self):
		self.logger.debug("Stop recording")
		self.continuer = False
		
	def run(self):
		self.logger.debug("Starting microphone")
		self.continuer = True
		buff = bytearray()
		while(self.continuer):
			if(len(self.lclients) != 0):
				buff =  self.mic.getDataFromBuffer()
				self.lock.acquire(True)
				for i in range(len(self.lclients)):
					self.lclients[i].setData(buff)						
				self.lock.release()
			time.sleep(0.02)
		self.cleanup()
		
	def cleanup(self):
		self.logger.debug("Stoping microphone thread")
		self.mic.closeMicroStream()	
