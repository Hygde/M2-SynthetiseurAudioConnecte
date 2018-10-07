import socket
import time

class Client():

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = True

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.host, self.port)  
        sock.connect(server_address)  
        print("connecting to %s (%s) with %s" % (self.host, self.port, server_address))

    def sendJsonData(data):
        print("grec")
        while connected:
            try:
                print("Connection on {}".format(port))
                sock.send(data)
                connected = False
            except Exception as e:
                print(e)
                connected = False

        print("Close")
        sock.close()

    #def sendOtherData(data):
        #TODO
