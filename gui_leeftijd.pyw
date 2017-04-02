''' 
    Berekent leeftijd van een persoon in jaren, maanden en dagen. 
    Hangt af van PyQT5
'''

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QSystemTrayIcon
from MainWindow import Ui_MainWindow
from Classes import CalcTime

''' To make the icon work in the taskbar in Win7+, ctype is needed'''
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class runApplication(Ui_MainWindow):
    def __init__(self):
        self.run()
        self.setdefaults()
        self.Quit()
    def run(self):
        self.app=QApplication(sys.argv)
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.buttonactions()
        self.window.show()
        self.Quit()
    def setdefaults(self):
        self.ui.Resultaat=""
        _translate = QtCore.QCoreApplication.translate
        self.lblResultaat.setText(_translate("MainWindow", self.ui.Resultaat))
    def update(self):
        Calc=CalcTime(self.ui.Geboortedatum.text().replace("/",""))
        self.ui.Resultaat=Calc.printresult()
        _translate = QtCore.QCoreApplication.translate
        self.ui.lblResultaat.setText(_translate("MainWindow", self.ui.Resultaat))
    def buttonactions(self):
        self.ui.pushButtonBereken.clicked.connect(self.update)
    def Quit(self):
        sys.exit(self.app.exec_())
        
if __name__=="__main__":
    runApplication()

