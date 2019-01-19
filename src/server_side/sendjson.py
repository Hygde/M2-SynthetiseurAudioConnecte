import json
import socket
from client import Client

class SendJson(Client):

    def __init__(self, TCP, host, port, path):
        Client.__init__(self, TCP, host, port)
        self.path = path

    def sendData(self,data):
        self.logger.debug("sending data to the server")
        self.logger.debug(data)
        if(self.isTCP):self.sock.send(data)
        else:self.sock.sendto(data, self.host)

    def sendingJson(self):
        self.connect()
        self.sendData(self.getJson())

    def setJson(self, path):
        self.path = path

    def getJson(self):
        data = json.load(open(self.path))
        data["services"][0]["ip_local"] = socket.gethostbyname(socket.gethostname())
        return json.dumps(data).encode()
