import logging
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from stream import Stream
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
	'''To modify the ui:
		1.	open & modify & save the ui file with qt-creator
		2.	puic5 file_name.ui -o output_name.py
		3.	import the output class
	'''
    
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.logger = logging.getLogger()
		self.strl = []
		self.connectSlots()
		self.show()

	def connectSlots(self):
		self.ui.RadioMono.clicked.connect(self.onMonoSelected)
		self.ui.RadioStereo.clicked.connect(self.onStereoSelected)
		self.ui.RadioNormal.clicked.connect(self.onNormalSelected)
		self.ui.RadioAigue.clicked.connect(self.onAigueSelected)
		self.ui.RadioGrave.clicked.connect(self.onGraveSelected)
		self.ui.RadioFoule.clicked.connect(self.onFouleSelected)
     
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

	def updateStream(self,n):
		for i in range(len(self.strl)):
			self.strl[i].updateFilter(n)

	#user's event

	@pyqtSlot()
	def onMonoSelected(self):
		self.logger.debug("The output is now Mono")
		#self.updateStream(1)
		pass

	@pyqtSlot()
	def onStereoSelected(self):
		self.logger.debug("The output is now Stereo")
		#self.updateStream(2)
		pass

	@pyqtSlot()
	def onNormalSelected(self):
		self.logger.debug("The filter is now: normal")
		self.updateStream(0)
		pass

	@pyqtSlot()
	def onAigueSelected(self):
		self.logger.debug("The filter is now: aigue")
		self.updateStream(1)
		pass

	@pyqtSlot()
	def onGraveSelected(self):
		self.logger.debug("The filter is now: grave")
		self.updateStream(2)
		pass

	@pyqtSlot()
	def onFouleSelected(self):
		self.logger.debug("The filter is now: foule")
		pass
	
	def closeEvent(self, event):
		self.logger.error("application est quitée")
		for s in self.strl:
			s.cleanup()