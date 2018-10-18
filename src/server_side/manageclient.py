import socket
import logging
import time
from threading import Thread
from threading import Lock

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
		self.data = bytearray()
		self.read = True
		self.lock_read = Lock()
		
	def setData(self, data):
		self.logger.debug("set data")
		if(self.lock_read.acquire(False)):
			self.data = data
			self.read = False
			self.lock_read.release()
			self.logger.debug("setting data completed")
		
	def stop(self):
		self.logger.debug("Stoping the client %s thread",self.addr)
		try:
			self.logger.debug("CLOSE")
			self.sock.sendall(b"CLOSE")
		finally:
			self.continuer = False
		
	def run(self):
		self.logger.debug("Starting client %s thread", self.addr)
		self.continuer = True
		while(self.continuer):
			try:
				if(self.read == False):
					self.sock.sendall(self.data)
					self.read = True
				else:time.sleep(0.01)
			except Exception as e:
				self.logger.debug(e)
				self.logger.debug("Connection closed !")
				self.continuer = False
		self.cleanup()
		
	def cleanup(self):
		self.logger.debug("Client %s waiting for lock", self.addr)
		self.lock.acquire(True)
		self.sock.close()
		self.lclients.remove(self)
		print(len(self.lclients))
		self.lock.release()
		self.logger.debug("Client %s cleanup completed!", self.addr)
