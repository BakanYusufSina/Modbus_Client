# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\TR-DM-004\Documents\Programing\Python\Modbus_Client\modbus.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setGeometry(QtCore.QRect(400, 70, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnConnect.setFont(font)
        self.btnConnect.setObjectName("btnConnect")
        self.comRead = QtWidgets.QComboBox(self.centralwidget)
        self.comRead.setGeometry(QtCore.QRect(110, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comRead.setFont(font)
        self.comRead.setObjectName("comRead")
        self.btnRead = QtWidgets.QPushButton(self.centralwidget)
        self.btnRead.setGeometry(QtCore.QRect(330, 140, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnRead.setFont(font)
        self.btnRead.setObjectName("btnRead")
        self.btnWrite = QtWidgets.QPushButton(self.centralwidget)
        self.btnWrite.setGeometry(QtCore.QRect(330, 210, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btnWrite.setFont(font)
        self.btnWrite.setObjectName("btnWrite")
        self.comWrite = QtWidgets.QComboBox(self.centralwidget)
        self.comWrite.setGeometry(QtCore.QRect(110, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comWrite.setFont(font)
        self.comWrite.setObjectName("comWrite")
        self.txtIpv1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIpv1.setGeometry(QtCore.QRect(20, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtIpv1.setFont(font)
        self.txtIpv1.setObjectName("txtIpv1")
        self.txtIpv2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIpv2.setGeometry(QtCore.QRect(90, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtIpv2.setFont(font)
        self.txtIpv2.setObjectName("txtIpv2")
        self.txtIpv3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIpv3.setGeometry(QtCore.QRect(160, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtIpv3.setFont(font)
        self.txtIpv3.setObjectName("txtIpv3")
        self.txtIpv4 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIpv4.setGeometry(QtCore.QRect(230, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtIpv4.setFont(font)
        self.txtIpv4.setObjectName("txtIpv4")
        self.txtRead = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRead.setGeometry(QtCore.QRect(220, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtRead.setFont(font)
        self.txtRead.setObjectName("txtRead")
        self.txtWrite = QtWidgets.QLineEdit(self.centralwidget)
        self.txtWrite.setGeometry(QtCore.QRect(220, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtWrite.setFont(font)
        self.txtWrite.setObjectName("txtWrite")
        self.txtPort = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPort.setGeometry(QtCore.QRect(310, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPort.setFont(font)
        self.txtPort.setObjectName("txtPort")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnConnected = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnected.setGeometry(QtCore.QRect(440, 0, 51, 31))
        self.btnConnected.setText("")
        self.btnConnected.setObjectName("btnConnected")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ip Adresi"))
        self.btnConnect.setText(_translate("MainWindow", "Bağlan"))
        self.btnRead.setText(_translate("MainWindow", "Veri Oku"))
        self.btnWrite.setText(_translate("MainWindow", "Veri Yaz"))
        self.txtIpv1.setText(_translate("MainWindow", "0"))
        self.txtIpv2.setText(_translate("MainWindow", "0"))
        self.txtIpv3.setText(_translate("MainWindow", "0"))
        self.txtIpv4.setText(_translate("MainWindow", "0"))
        self.txtPort.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Port"))
