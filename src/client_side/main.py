import logging

import sys
import logging

from client import *

def initLogger():
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s")
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	ch.setFormatter(formatter)
	logger.addHandler(ch)
	return logger		
	

def main():
	logger = initLogger()
	logger.info("starting program")
	client_list = []
	try:
		logger.debug("Creation of the client successed")
		client_list.append(Client(True, "127.0.0.1",2000))
		client_list[-1].connect()
	except ValueError as e:
		logger.error(e)
	except OSError as e:
		logger.debug(e)
	finally:
		logger.debug("closing the sockets")
		for i in range(len(client_list)):client_list[i].closeSocket()

if __name__ == "__main__":
	main()
