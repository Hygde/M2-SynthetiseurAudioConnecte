# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(247, 155)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RadioNormal = QtWidgets.QRadioButton(self.centralwidget)
        self.RadioNormal.setChecked(True)
        self.RadioNormal.setObjectName("RadioNormal")
        self.verticalLayout.addWidget(self.RadioNormal)
        self.RadioAigue = QtWidgets.QRadioButton(self.centralwidget)
        self.RadioAigue.setObjectName("RadioAigue")
        self.verticalLayout.addWidget(self.RadioAigue)
        self.RadioGrave = QtWidgets.QRadioButton(self.centralwidget)
        self.RadioGrave.setObjectName("RadioGrave")
        self.verticalLayout.addWidget(self.RadioGrave)
        self.RadioFoule = QtWidgets.QRadioButton(self.centralwidget)
        self.RadioFoule.setObjectName("RadioFoule")
        self.verticalLayout.addWidget(self.RadioFoule)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 247, 22))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        self.menuFichier.triggered['QAction*'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RadioNormal.setText(_translate("MainWindow", "Normal"))
        self.RadioAigue.setText(_translate("MainWindow", "Aiguë"))
        self.RadioGrave.setText(_translate("MainWindow", "Grave"))
        self.RadioFoule.setText(_translate("MainWindow", "Foule"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+F4"))

