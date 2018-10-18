import logging
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from stream import Stream

class MainWindow(QtWidgets.QMainWindow):
    
	def __init__(self):
		super(MainWindow, self).__init__()
		uic.loadUi('ui/ui_mainwindow.ui', self)
		self.logger = logging.getLogger()
		self.strl = []
		self.show()
     
	def setHosts(self, hosts):
		self.logger.debug(hosts)
		self.hosts = hosts.copy()
	
	def connectToStreams(self):
		self.logger.debug("It starts to connect to the streams")
		try:
			for i in range(len(self.hosts)):
				self.logger.debug(self.hosts[i])
				self.strl.append(Stream(True, self.hosts[i][0], self.hosts[i][1]))
				self.strl[-1].connect()
				self.strl[-1].start()
		except Exception as e:
			self.logger.error(e)
