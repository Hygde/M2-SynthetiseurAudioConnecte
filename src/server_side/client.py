import logging
import socket
import time

from threading import Thread

class Client(Thread):

	def __init__(self, TCP, host, port):
		Thread.__init__(self)
		self.logger = logging.getLogger()
		self.logger.debug("Creation of a client")
		self.host = host
		self.port = port
		self.isTCP = TCP
		self.continuer = True

	def connect(self):
		try:
			if(self.isTCP):
				self.logger.debug("Creating TCP socket")
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP
			else:
				self.logger.debug("Creating an UDP sokcet")
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#udp
				self.sock.bind((self.host, self.port))
			self.sock.connect((self.host, self.port))
			self.logger.debug("connected to %s (%s) with %s" % (self.host, self.port, self.sock.getpeername()))
		except Exception as e:
			self.logger.error(e)

	def sendData(self, data):
		try:
			self.logger.debug("sending data to the server")
			self.logger.debug(data)
			if(self.isTCP):self.sock.send(data)
			else:self.sock.sendto(data, self.host)
		except Exception as e:
			self.logger.error("sending fail with error code : %s",e)
			
	def recvUDP_TCP(self):
		data = bytearray()
		data = self.sock.recv(1024)
		return data
			
	def run(self):#reception of data
		while(self.continuer):
			try:
				data = self.recvUDP_TCP()
				if(data == b'CLOSE'):self.continuer = False
				else:
					self.logger.debug(data)	
			except Exception as e:
				self.logger.error(e)
				self.closeSocket()

	def closeSocket(self):
		self.logger.debug("Closing the socket")
		self.continuer = False
		self.sock.close()
		self.logger.debug("Socket closed")
