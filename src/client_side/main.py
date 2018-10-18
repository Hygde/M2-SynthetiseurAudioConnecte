import logging

import sys
import logging

from time import sleep
from client import Client
from sendjson import SendJson
from PyQt5 import QtWidgets
from mainwindow import MainWindow

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
		client_list.append(SendJson(True, "37.59.57.203",55555,"manifest.JSON"))
		client_list[-1].connect()
		client_list[-1].start()
		#do some other task
		app = QtWidgets.QApplication(sys.argv)
		window = MainWindow()
		client_list[-1].join()
		#todo get hosts from client_list and sends it to window object
	except ValueError as e:
		logger.error(e)
	except OSError as e:
		logger.debug(e)
	finally:
		window.setHosts([("127.0.0.1", 2000)])
		window.connectToStreams()
		sys.exit(app.exec_())

if __name__ == "__main__":
	main()
