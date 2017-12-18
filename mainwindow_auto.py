# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.button1 = QtWidgets.QPushButton(self.centralWidget)
        self.button1.setGeometry(QtCore.QRect(50, 110, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setStyleSheet("alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralWidget)
        self.button2.setGeometry(QtCore.QRect(280, 110, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setStyleSheet("alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.button2.setObjectName("button2")
        self.label_status_lbl = QtWidgets.QLabel(self.centralWidget)
        self.label_status_lbl.setGeometry(QtCore.QRect(60, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_status_lbl.setFont(font)
        self.label_status_lbl.setObjectName("label_status_lbl")
        self.status_label = QtWidgets.QLabel(self.centralWidget)
        self.status_label.setGeometry(QtCore.QRect(180, 20, 131, 31))
        self.status_label.setObjectName("status_label")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home Alarm"))
        self.button1.setText(_translate("MainWindow", "Armed Away"))
        self.button2.setText(_translate("MainWindow", "Armed Home"))
        self.label_status_lbl.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600;\">Alarm Status:   </span></p></body></html>"))
        self.status_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))

