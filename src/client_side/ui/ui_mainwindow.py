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
        MainWindow.resize(315, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RadioMono = QtWidgets.QRadioButton(self.horizontalWidget)
        self.RadioMono.setChecked(True)
        self.RadioMono.setObjectName("RadioMono")
        self.horizontalLayout_2.addWidget(self.RadioMono)
        self.RadioStereo = QtWidgets.QRadioButton(self.horizontalWidget)
        self.RadioStereo.setObjectName("RadioStereo")
        self.horizontalLayout_2.addWidget(self.RadioStereo)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.RadioNormal = QtWidgets.QRadioButton(self.verticalWidget)
        self.RadioNormal.setChecked(True)
        self.RadioNormal.setObjectName("RadioNormal")
        self.verticalLayout_5.addWidget(self.RadioNormal)
        self.RadioAigue = QtWidgets.QRadioButton(self.verticalWidget)
        self.RadioAigue.setObjectName("RadioAigue")
        self.verticalLayout_5.addWidget(self.RadioAigue)
        self.RadioGrave = QtWidgets.QRadioButton(self.verticalWidget)
        self.RadioGrave.setObjectName("RadioGrave")
        self.verticalLayout_5.addWidget(self.RadioGrave)
        self.RadioFoule = QtWidgets.QRadioButton(self.verticalWidget)
        self.RadioFoule.setObjectName("RadioFoule")
        self.verticalLayout_5.addWidget(self.RadioFoule)
        self.verticalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 315, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionMono = QtWidgets.QAction(MainWindow)
        self.actionMono.setObjectName("actionMono")
        self.actionStereo = QtWidgets.QAction(MainWindow)
        self.actionStereo.setObjectName("actionStereo")
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sortie Audio :"))
        self.RadioMono.setText(_translate("MainWindow", "Mono"))
        self.RadioStereo.setText(_translate("MainWindow", "Stereo"))
        self.label_2.setText(_translate("MainWindow", "Filtres Audio :"))
        self.RadioNormal.setText(_translate("MainWindow", "Normal"))
        self.RadioAigue.setText(_translate("MainWindow", "Aiguë"))
        self.RadioGrave.setText(_translate("MainWindow", "Grave"))
        self.RadioFoule.setText(_translate("MainWindow", "Foule"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionMono.setText(_translate("MainWindow", "Mono"))
        self.actionStereo.setText(_translate("MainWindow", "Stereo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

