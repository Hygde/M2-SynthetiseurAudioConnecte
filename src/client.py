import socket
import time

class Client():

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = True
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.host, self.port)  
        self.sock.connect(server_address)  
        print("connecting to %s (%s) with %s" % (self.host, self.port, server_address))

    def sendJsonData(self, data):
        print("grec")
        while self.connected:
            try:
                print("Connection on {}".format(port))
                self.sock.send(data)
                self.connected = False
            except Exception as e:
                print(e)
                self.connected = False

        print("Close")
        self.sock.close()

    #def sendData(data):
    #    while continuer:
    #        try:
	#		    #player.play(sock.recv(2048))
	#	        data = sock.recv(4096)
	#	        if(data == b'CLOSE'):
	#		        continuer = False
	#	        else:
	#		        player.play(data)		
	#        except Exception as e:
	#	        print(e)
	#	        continuer = False

    #    sock.close()
    #    player.closeAudioPlayerStream()
