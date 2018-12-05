import json
from client import *

class SendJson(Client):

    def __init__(self, TCP, host, port, path):
        Client.__init__(self, TCP, host, port)
        self.path = path

    def sendingJson(self):
        self.connect()
        self.sendJsonData(self.getJson())

    def setJson(self, path):
        self.path = path

    def getJson(self):
        return json.load(open(self.path))
