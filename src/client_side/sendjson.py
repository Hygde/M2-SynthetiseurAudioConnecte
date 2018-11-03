import os
from client import Client

class SendJson(Client):

    def __init__(self, TCP, host, port, path):
        Client.__init__(self, TCP, host, port)
        self.path = path
        
    def run(self):
        while(self.continuer):
            try:
                data = self.sock.recv(1024)
                self.logger.debug(data)
                if(data == b'EHLO'):
                    self.sendData(bytearray(self.getJson().encode()))
                if(data == b'HELO'):
                    self.continuer = False
            except Exception as e:
            	self.logger.error(e)
            	self.closeSocket()   
            
    def setJson(self, path):
        self.path = path

    def getJson(self):
        f = open("json/manifest.JSON", "r")
        return f.read()
