# -*- coding: utf-8 -*-
import sys
import socket
import re
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("SParent")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(QtGui.QFont("URW Gothic L", 40, italic=True, weight=50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 60))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label.setText("SParent")
        self.pushButton.setText("Автопоиск")
        self.pushButton_2.setText("Вручную")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class Ui_MainWindow_List(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("SParent")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(QtGui.QFont('Noto Sans', 12))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 149, 318, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setAcceptDrops(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_1.setFont(QtGui.QFont('Noto Sans', 12))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label_1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 60))
        self.verticalLayout.addWidget(self.pushButton_1)
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setText('Нажмите кнопку "Поиск"')
        self.pushButton_1.setText("Поиск")
        self.pushButton.setText("Назад")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class Ui_MainWindow_HandSetting(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle("SParent")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText("")
        self.verticalLayout.addWidget(self.label_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(QtGui.QFont('Noto Sans', 14))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_3.setFont(QtGui.QFont('Noto Sans', 12))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(QtGui.QFont('Noto Sans', 11))
        self.label_2.setStyleSheet("color: #248f24")
        self.label_2.setText("")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 60))
        self.verticalLayout.addWidget(self.pushButton_1)
        self.label.setText("Ручная настройка")
        self.label_3.setText("Введите IP компьютера: ")
        self.pushButton.setText("Подключиться")
        self.pushButton_1.setText("Назад")
        MainWindow.setCentralWidget(self.centralwidget)


# GLOBAL main ip
IP = []


class Ui_MainWindow_ShutDown(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle("SParent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(QtGui.QFont('Noto Sans', 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(QtGui.QFont('Noto Sans', 14))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.label)
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalLayout.addWidget(self.timeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.setText("Выключение")
        self.label.setText("Таймер:")
        self.timeEdit.setDisplayFormat("HH:mm")
        self.pushButton.setText("Выключить")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class ShutDownWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ShutDownWindow, self).__init__()
        self.ui = Ui_MainWindow_ShutDown()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.GetBackMutherFucker)

    def GetBackMutherFucker(self):
        time_h, time_m, time_s = self.ui.timeEdit.time().hour(), self.ui.timeEdit.time().minute(), \
                                 self.ui.timeEdit.time().second()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP[0], 8000))
            mes = "GET /shutdown/%s HTTP/1.1\r\nHost: http://%s:8000\r\n\r\n" % ((time_h*60+time_m)*60+time_s, IP[0])
            s.sendall(mes.encode())
        except:
            print('Error')
        print('Bang %s' % IP[0])


class AutoSearchWindow(QtWidgets.QMainWindow):
    def Back_To_Main(self):
        self.ui.label.setText('Нажмите кнопку "Поиск"')
        if len(self.ui.scrollAreaWidgetContents.children()) == 3:
            self.ui.scrollAreaWidgetContents.children()[2].deleteLater()

    def Search(self):
        del IP[:]
        if len(self.ui.scrollAreaWidgetContents.children()) == 3:
            self.ui.scrollAreaWidgetContents.children()[2].deleteLater()
        self.ui.label_1.setText("")
        self.ui.label.setText("Ведёться поиск компьютера...")
        self.ui.label.repaint()
        self.ui.label_1.repaint()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ipc = s.getsockname()[0].split('.')
            s.close()
            time.sleep(5)
            for i in range(int(ipc[2]), int(ipc[2])+1):
                for j in range(2, 256):
                    current_scan = ipc[0]+'.'+ipc[1]+'.'+str(i)+'.'+str(j)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.10)
                    try:
                        connect = sock.connect((current_scan, 8000))
                        IP.append(current_scan)
                        break
                    except:
                        pass
            if not IP:
                self.ui.label_1.setText("Ничего не найдено")
            else:
                button = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents)
                button.setMinimumSize(QtCore.QSize(0, 40))
                # host_name = socket.gethostbyaddr(IP[0]) # get user_name pc come back soon
                host_name = ['PC']
                button.setText("%s/%s" % (host_name[0], IP[0]))
                button.clicked.connect(lambda: (widget.setCurrentIndex(3),
                                                self.ui.scrollAreaWidgetContents.children()[2].deleteLater()))
                self.ui.verticalLayout_2.addWidget(button)
        except:
            self.ui.label_1.setText("Произошла неизвестная ошибка")
        self.ui.label.setText('Нажмите кнопку "Поиск"')

    def __init__(self):
        super(AutoSearchWindow, self).__init__()
        self.ui = Ui_MainWindow_List()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.Search)
        self.ui.pushButton.clicked.connect(self.Back_To_Main)
        if len(self.ui.scrollAreaWidgetContents.children()) == 3:
            self.ui.scrollAreaWidgetContents.children()[2].deleteLater()


class HandSetting(QtWidgets.QMainWindow):
    def __init__(self):
        super(HandSetting, self).__init__()
        self.ui = Ui_MainWindow_HandSetting()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Connect)

    def Connect(self):
        del IP[:]
        current_hand = self.ui.lineEdit.text()
        if re.search(r'^([0-9]){1,3}\.([0-9]){1,3}\.([0-9]){1,3}\.([0-9]){1,3}$', current_hand) is None:
            self.ui.label_2.setStyleSheet('color: #ff0000')
            self.ui.label_2.setText('IP введён не верно')
        else:
            try:
                sock_hand = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock_hand.settimeout(0.10)
                connect = sock_hand.connect((current_hand, 8000))
                IP.append(current_hand)
                self.ui.label_2.setStyleSheet('color: #248f24')
                self.ui.label_2.setText('Есть контакт!')
                self.ui.label_2.repaint()
                time.sleep(3)
                widget.setCurrentIndex(3)
            except:
                self.ui.label_2.setStyleSheet('color: #ff0000')
                self.ui.label_2.setText('Нет контакта!')


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_MainWindow_Main()
        self.ui.setupUi(self)


# initialisations
app = QtWidgets.QApplication([])
start_window = StartWindow()
auto_search_window = AutoSearchWindow()
hand_setting = HandSetting()
shutdown_window = ShutDownWindow()
widget = QtWidgets.QStackedWidget()
# set window index
widget.addWidget(start_window)  # he have index 0
widget.addWidget(auto_search_window)  # index 1
widget.addWidget(hand_setting)  # index 2
widget.addWidget(shutdown_window)  # index 3
# set switch
start_window.ui.pushButton.clicked.connect(lambda: widget.setCurrentIndex(1))
start_window.ui.pushButton_2.clicked.connect(lambda: widget.setCurrentIndex(2))
auto_search_window.ui.pushButton.clicked.connect(lambda: widget.setCurrentIndex(0))
hand_setting.ui.pushButton_1.clicked.connect(lambda: widget.setCurrentIndex(0))
# start application
widget.show()
sys.exit(app.exec_())
