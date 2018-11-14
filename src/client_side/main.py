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
	pregister = None
	window = None
	try:
		logger.debug("Creation of the client successed")
		#pregister = SendJson(True, "37.59.57.203",55555,"manifest.JSON")
		#pregister.connect()
		#pregister.start()
		#do some other task
		app = QtWidgets.QApplication(sys.argv)
		window = MainWindow()
		#pregister.join()
		#todo get hosts from client_list and sends it to window object
	except ValueError as e:
		logger.error(e)
	except OSError as e:
		logger.error(e)
	finally:
		window.setHosts([("127.0.0.1", 2000)])
		window.connectToStreams()
		sys.exit(app.exec_())

if __name__ == "__main__":
	main()
