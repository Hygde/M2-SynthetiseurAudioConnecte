import sys
import logging
from server import *

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
	
	assert (len(sys.argv) == 2),"A port is expected"
	print(int("5"))
	try:
		serv = Server(int(sys.argv[1]))
		logger.debug("Creation of the server successed")
		serv.startRecording()
		serv.whileAccept()
	except ValueError:
		logger.error("Incorrect port value !")
	except OSError:
		logger.debug("Port already in use")


if __name__ == "__main__":
	main()
