# -*- coding: utf-8 -*-
import sys
import subprocess
from os import path, getcwd
from PyQt5 import QtCore, QtGui, QtWidgets
from client.design import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    #
    # def unfade(self):
    #     self.ui.pushButton.setStyleSheet("border-radius: 70%; background: #404040; margin: 10px; color: white;")
    #
    def btnClicked(self):
        print(path.abspath(getcwd()))
        subprocess.Popen([sys.executable, "server.py"])
        print("lol")
        # subprocess.run('python3 //home//gaylord//PycharmProjects//Sparent0.0.1//server.py')
        # self.ui.pushButton.setStyleSheet("border-radius: 70%; background: #252525; margin: 10px; color: white;")
        # QtCore.QTimer.singleShot(100, self.unfade)


app = QtWidgets.QApplication(sys.argv)
application = MyWindow()
application.show()
app.exec()
sys.exit()
