# -*- coding: utf-8 -*-
import sys
import socket
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from client.black_design1 import Ui_MainWindow_Main
from client.black_design2 import Ui_MainWindow_List

# for text in element QtWidgets
_translate = QtCore.QCoreApplication.translate
# GLOBAL main ip
IP = []


# def Scan():
#     print('start scan')
#     try:
#         import socket
#         import subprocess
#         # get main shluse
#         process = subprocess.Popen(['ip', 'route', 'show'], stdout=subprocess.PIPE)
#         main_shluze = int(process.communicate()[0].decode('utf-8').split(' ')[2].split('.')[-1])
#         # returns 0 if connection succeeds else raises error
#         for i in range(main_shluze, 2):
#             for j in range(main_shluze + 1, 256):
#                 current_scan = '192.168.' + str(i) + '.' + str(j)
#                 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                 sock.settimeout(0.2)
#                 try:
#                     connect = sock.connect((current_scan, 8000))
#                     IP.append(current_scan)
#                     break
#                 except:
#                     pass
#     except:
#         print('error')


# this anim for button and else element's
def btnClicked(obj):
    obj.setStyleSheet("background: #252525; border-radius: 5%; color: white;")
    QtCore.QTimer.singleShot(100, lambda: obj.setStyleSheet("background: #424242; border-radius: 5%; color: white;"))


class AutoSearchWindow(QtWidgets.QMainWindow):
    # def delAll(self):
    #

    def Search(self):
        try:
            # get main shluse
            process = subprocess.Popen(['ip', 'route', 'show'], stdout=subprocess.PIPE)
            main_shluze = int(process.communicate()[0].decode('utf-8').split(' ')[2].split('.')[-1])
            # returns 0 if connection succeeds else raises error
            for i in range(main_shluze, 2):
                for j in range(main_shluze + 1, 256):
                    current_scan = '192.168.' + str(i) + '.' + str(j)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.2)
                    try:
                        connect = sock.connect((current_scan, 8000))
                        IP.append(current_scan)
                        break
                    except:
                        pass
        except:
            lable = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setPointSize(12)
            lable.setFont(font)
            lable.setStyleSheet("color: white;")
            lable.setAlignment(QtCore.Qt.AlignCenter)
            lable.setText(_translate("MainWindow", "Произошла неизвестная ошибка"))
            self.ui.verticalLayout_2.addWidget(lable)
            print('error')

        if not IP:
            lable = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setPointSize(12)
            lable.setFont(font)
            lable.setStyleSheet("color: white;")
            lable.setAlignment(QtCore.Qt.AlignCenter)
            lable.setText(_translate("MainWindow", "Ничего не найдено"))
            self.ui.verticalLayout_2.addWidget(lable)
        else:
            button = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents)
            button.setMinimumSize(QtCore.QSize(0, 40))
            button.setStyleSheet("background: #424242; border-radius: 5%; color: white;")
            button.setText(_translate("MainWindow", "%s" % IP[0]))
            # button.clicked.connect(self.animButton)
            self.ui.verticalLayout_2.addWidget(button)

    def __init__(self):
        super(AutoSearchWindow, self).__init__()
        self.ui = Ui_MainWindow_List()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: btnClicked(self.ui.pushButton))
        self.ui.pushButton_1.clicked.connect(lambda: btnClicked(self.ui.pushButton_1))
        # start auto search
        self.ui.pushButton_1.clicked.connect(self.Search)


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_MainWindow_Main()
        self.ui.setupUi(self)
        # set anim
        self.ui.pushButton.clicked.connect(lambda: btnClicked(self.ui.pushButton))
        self.ui.pushButton_2.clicked.connect(lambda: btnClicked(self.ui.pushButton_2))
        # set func
        self.ui.pushButton.clicked.connect(self.Push)

    def Push(self):
        print("nice")


app = QtWidgets.QApplication([])
start_window = StartWindow()
auto_search_window = AutoSearchWindow()
widget = QtWidgets.QStackedWidget()
# set window index
widget.addWidget(start_window)  # he have index 0
widget.addWidget(auto_search_window)  # index 1
# set switch
start_window.ui.pushButton.clicked.connect(lambda: widget.setCurrentIndex(1))
auto_search_window.ui.pushButton.clicked.connect(lambda: widget.setCurrentIndex(0))
# start application
widget.show()
sys.exit(app.exec_())

# app = QtWidgets.QApplication(sys.argv)
# application = MyWindow()
# application.show()
# app.exec()
# sys.exit()
