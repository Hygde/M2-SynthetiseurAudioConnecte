import logging
import socket
import time

class Client():

	def __init__(self, TCP, host, port):
		self.logger = logging.getLogger()
		self.logger.debug("Creation of a client")
		self.host = host
		self.port = port
		self.isTCP = TCP

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
			self.logger.debug("connecting to %s (%s) with %s" % (self.host, self.port, self.sock.getpeername()))
		except Exception as e:
			self.logger.debug(e)

	def sendData(self, data):
		try:
			self.logger.debug("sending data to the server")
			if(self.isTCP):self.sock.sendAll(data)
			else:self.sock.sendTo(data, (self.host, self))
		except Exception as e:
			self.logger.debug("sending fail",e)

	def closeSocket(self):
		self.logger.debug("Closing the socket")
		self.sock.close()
