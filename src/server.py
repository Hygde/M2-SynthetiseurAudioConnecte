import socket
import logging
import threading

from audio import *
from sendjson import *
from manageclient import *
from managemicrophone import *

class Server:
	
    logger = logging.getLogger()
	
    def __init__(self, port):
        self.logger.debug("Initializing server")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("", port))
        self.socket.listen()
        self.lock_client = Lock()
        self.list_client = []
		
    def getClients(self):
        self.logger.debug("The server is getting the list of clients")
        return self.list_client

    def sendJson(self):
        self.logger.debug("The server is sending a json file to the clients")
        print("gggg", socket.gethostname())
        self.json_data = SendJson(socket.gethostname(), 2000, "json/manifest.JSON")
        self.json_data.sendingJson()
		
    def startRecording(self):
        self.logger.debug("The server is starting the microphone thread")
        self.manage_mic = ManageMicrophone(self.lock_client, self.list_client)
        self.manage_mic.start()
		
    def whileAccept(self):
        self.logger.debug("The server is accepting client")
        continuer = True
        while(continuer):
            try:
                print(len(self.list_client))
                conn, addr = self.socket.accept()
                self.lock_client.acquire(True)
                self.list_client.append(ManageClient(conn, addr, self.lock_client, self.list_client))
                self.list_client[-1].start()
                self.lock_client.release()
            except:
                self.logger.debug("The server stop to accept client")
                continuer = False
        self.cleanup()
				
    def cleanup(self):
	    self.logger.debug("The server is starting to clean up")
	    for i in range(len(self.list_client)):
	        self.list_client[i].stop()
	    self.socket.shutdown(socket.SHUT_RDWR)
	    self.socket.close()
	    self.manage_mic.stop()
	    self.manage_mic.join()
