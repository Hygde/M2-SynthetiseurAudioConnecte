import sys
import logging
from server import Server

def initLogger():
	logger = logging.getLogger()
	logger.setLevel(logging.ERROR)
	formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s")
	ch = logging.StreamHandler()
	ch.setLevel(logging.ERROR)
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
		#serv.sendJson()
		serv.createMicrophone()
		serv.whileAccept()
	except ValueError as e:
		logger.error(e)
	except OSError as e:
		logger.debug(e)


if __name__ == "__main__":
	main()
