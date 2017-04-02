# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 106)
        MainWindow.setMinimumSize(QtCore.QSize(350, 106))
        MainWindow.setMaximumSize(QtCore.QSize(350, 106))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblGeboortedatum = QtWidgets.QLabel(self.centralwidget)
        self.lblGeboortedatum.setGeometry(QtCore.QRect(12, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblGeboortedatum.setFont(font)
        self.lblGeboortedatum.setObjectName("lblGeboortedatum")
        self.Geboortedatum = QtWidgets.QDateEdit(self.centralwidget)
        self.Geboortedatum.setGeometry(QtCore.QRect(10, 30, 95, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Geboortedatum.setFont(font)
        self.Geboortedatum.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 11, 21), QtCore.QTime(0, 0, 0)))
        self.Geboortedatum.setObjectName("Geboortedatum")
        self.pushButtonBereken = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBereken.setGeometry(QtCore.QRect(10, 60, 93, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonBereken.setFont(font)
        self.pushButtonBereken.setObjectName("pushButtonBereken")
        self.lblResultaat = QtWidgets.QLabel(self.centralwidget)
        self.lblResultaat.setGeometry(QtCore.QRect(132, 10, 189, 67))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblResultaat.setFont(font)
        self.lblResultaat.setText("")
        self.lblResultaat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblResultaat.setObjectName("lblResultaat")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bereken leeftijd"))
        self.lblGeboortedatum.setText(_translate("MainWindow", "Geboortedatum:"))
        self.pushButtonBereken.setText(_translate("MainWindow", "Bereken leeftijd"))

