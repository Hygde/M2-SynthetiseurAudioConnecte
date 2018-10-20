import socket
import logging
import time
from threading import Thread
from threading import Lock
from microphone import Microphone

class ManageClient(Thread):
	
	logger = logging.getLogger()
	
	def __init__(self, conn, addr, lock_list, list_client):
		Thread.__init__(self)
		self.setDaemon(True)
		print(self.isDaemon())
		self.logger.debug("Initializing the client manager")
		self.sock = conn
		self.addr = addr
		self.lock = lock_list
		self.lclients = list_client
		
	def setData(self, data):
		self.logger.debug("set data")
		if(self.lock_read.acquire(False)):
			self.data = data
			self.read = False
			self.lock_read.release()
			self.logger.debug("setting data completed")

	def setMicrophone(self, mic):
		self.logger.debug("Setting the microphone")
		self.micro = mic
		
	def stop(self):
		self.logger.debug("Stoping the client %s thread",self.addr)
		try:
			self.logger.debug("CLOSE")
			self.sock.sendall(b"CLOSE")
		except Exception as e:
			self.logger.debug(e)
		finally:
			self.continuer = False
		
	def run(self):
		self.logger.debug("Starting client %s thread", self.addr)
		self.continuer = True
		while(self.continuer):
			try:
				self.sock.sendall(self.micro.getDataFromBuffer())
			except Exception as e:
				self.logger.error(e)
				self.continuer = False
		self.cleanup()
		
	def cleanup(self):
		self.logger.debug("Client %s waiting for lock", self.addr)
		self.stop()
		self.lock.acquire(True)
		self.lclients.remove(self)
		print(len(self.lclients))
		self.lock.release()
		self.logger.debug("Client %s cleanup completed!", self.addr)
