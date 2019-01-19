import ast
import json
import socket
from client import Client

class SendJson(Client):

    def __init__(self, TCP, host, port, path):
        Client.__init__(self, TCP, host, port)
        self.path = path

    def _parse(self, data):
        ip, port = None, None
        for d in data:
            print(d)
            if "label" in d and "MicServer" in d["label"]: 
                ip = d["services"][0]["ip_local"]
                port = d["services"][0]["port"]
        return (ip, port)


    def sendData(self,data):
        self.logger.debug("sending data to the server")
        self.logger.debug(data)
        if(self.isTCP):self.sock.send(data)
        else:self.sock.sendto(data, self.host)

    def sendingJson(self):
        self.connect()
        self.logger.debug(self.recvUDP_TCP())
        self.sendData(self.getJson())
        self.logger.debug(self.recvUDP_TCP())

    def getIpOfServer(self):
        self.sendData("man".encode())
        to_parse = ast.literal_eval(str(self.recvUDP_TCP(), "utf-8"))
        return self._parse(to_parse)

    def setJson(self, path):
        self.path = path

    def getJson(self):
        data = json.load(open(self.path))
        return json.dumps(data).encode()
