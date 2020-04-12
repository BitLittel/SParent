# -*- coding: utf-8 -*-
import sys, time, zipfile, urllib.request, os, getpass
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

mother_path = ['']


class Ui_MainWindow_Start(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 450)
        MainWindow.setMinimumSize(QtCore.QSize(700, 450))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background: #323232;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Hairline")
        font.setPointSize(72)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: #10ff30;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: #434343; border-radius: 10%; color: white;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SParent Install"))
        self.label.setText(_translate("MainWindow", "SParent"))
        self.label_2.setText(_translate("MainWindow", "Это программа установки \"Sparent v0.1\". Для продожения установки нажмите кнопку \"Далее\". В отличии от других программ установки тут не будет вкладки с политиками и правами, да и кто их нахуй читает. Так что если хочешь установить таталитарный кантроль над компом ребёнка то просто продолжи уже и перестать эту чушь читать. "))
        self.pushButton.setText(_translate("MainWindow", "Далее"))


class Ui_MainWindow_File(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 450)
        MainWindow.setMinimumSize(QtCore.QSize(700, 450))
        MainWindow.setStyleSheet("background: #323232;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Hairline")
        font.setPointSize(72)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: #10ff30; margin: 50%;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setObjectName("treeView")
        self.gridLayout_2.addWidget(self.treeView, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setStyleSheet("background: #434343; border-radius: 10%; color: white;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SParent"))
        self.label_2.setText(_translate("MainWindow", "Выбери деррикторию установки: "))
        self.pushButton.setText(_translate("MainWindow", "Установить"))


class Ui_MainWindow_Load(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 450)
        MainWindow.setMinimumSize(QtCore.QSize(700, 450))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background: #323232;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Hairline")
        font.setPointSize(72)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #10ff30;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setText("А пока идёт процесс установки, щас поясню что делает установка. Скачиваеться пакет "
                             "программы который будет запускать в автономном режиме при запуске компьютера. Это "
                             "программа создаёт сервер и с помощью приложения мы подключаемся и нахуй гасим комп. "
                             "Всё. А чё ты хотел, я тебе всё расскажу, иди лесом!")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("color: white;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionadd = QtWidgets.QAction(MainWindow)
        self.actionadd.setObjectName("actionadd")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SParent"))
        self.label_3.setText(_translate("MainWindow", "Идёт установка..."))
        self.actionadd.setText(_translate("MainWindow", "add"))


class Ui_MainWindow_Finish(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 450)
        MainWindow.setMinimumSize(QtCore.QSize(700, 450))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background: #323232;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Hairline")
        font.setPointSize(72)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #10ff30;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setStyleSheet("background: #434343; border-radius: 10%; color: white;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SParent"))
        self.label_2.setText(_translate("MainWindow", "Ну всё. Установка закончена. Не забудь перезагрузить компьютер. Теперь просто нажми кнопку \"Закрыть\" или нажми крестик. И да, если заметил орфографические ошибки, то знай что мне искренне... похуй.  "))
        self.pushButton.setText(_translate("MainWindow", "Закрыть"))


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_MainWindow_Start()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.touch_button)

    def touch_button(self):
        self.ui.pushButton.setStyleSheet("border-radius: 10%; background: #303030; color: white;")
        self.ui.pushButton.repaint()
        time.sleep(.08)


class ChooseDirectory(QtWidgets.QMainWindow):
    def __init__(self):
        super(ChooseDirectory, self).__init__()
        self.ui = Ui_MainWindow_File()
        self.ui.setupUi(self)
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.homePath()))
        self.model.setReadOnly(True)
        self.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.hideColumn(1)
        self.ui.treeView.hideColumn(2)
        self.ui.treeView.hideColumn(3)
        self.ui.treeView.setExpandsOnDoubleClick(False)
        self.ui.treeView.setHeaderHidden(False)
        self.ui.treeView.clicked.connect(self.open_dir)
        self.ui.pushButton.clicked.connect(self.touch_button)
        # self.ui.pushButton.clicked.connect(self.load_file_in_the_path)

    def touch_button(self):
        self.ui.pushButton.setStyleSheet("border-radius: 10%; background: #303030; color: white;")
        self.ui.pushButton.repaint()
        time.sleep(.08)

    def open_dir(self):
        index = self.ui.treeView.currentIndex()
        dir_path = self.model.filePath(index)
        mother_path[0] = dir_path


class LoadTread(QThread):

    progress_value = pyqtSignal(int)

    def run(self):

        # download zip main server
        url = urllib.request.urlopen("https://github.com/VladPyJs/SParent/raw/master/SParent.zip")
        file_size = int(url.info()['Content-Length'])
        full_path = mother_path[0] + '/' + 'SParent.zip'
        f = open(full_path, 'wb')
        file_size_dl = 0
        block_sz = 1024  # 8192
        while True:
            buffer = url.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            value = int(file_size_dl * 100 / file_size)
            self.progress_value.emit(value)
            load_file.ui.progressBar.repaint()
        f.close()
        # end download #

        # un_zip #
        with zipfile.ZipFile(full_path) as zip_ref:
            zip_ref.extractall(mother_path[0]+'/SParent')
        os.remove(full_path)
        # end un_zip #

        # create auto_run file #
        auto_file = open('C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\'
                         'Programs\\Startup\\auto_run.vbs' % (getpass.getuser()), 'w')
        auto_file.write('Dim WinScriptHost\n'
                        'Set WinScriptHost = CreateObject("WScript.Shell")\n'
                        'WinScriptHost.Run Chr(34) & "%s" & Chr(34), 0\n'
                        'Set WinScriptHost = Nothing' % (mother_path[0]+'\\SParent\\SParent.exe'))
        auto_file.close()
        # end create #


class LoadFile(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoadFile, self).__init__()
        self.ui = Ui_MainWindow_Load()
        self.ui.setupUi(self)
        self.thread = LoadTread()

    def setProgressBar(self, val):
        self.ui.progressBar.setValue(val)

    def startProgressBar(self):
        self.thread.progress_value.connect(self.setProgressBar)
        self.thread.run()
        widget.setCurrentIndex(3)


class Finish(QtWidgets.QMainWindow):
    def __init__(self):
        super(Finish, self).__init__()
        self.ui = Ui_MainWindow_Finish()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.closeAPP)

    def closeAPP(self):
        sys.exit(app.exec_())


app = QtWidgets.QApplication([])

widget = QtWidgets.QStackedWidget()

start_window = StartWindow()
choose_directory = ChooseDirectory()
load_file = LoadFile()
finish = Finish()

widget.addWidget(start_window)
widget.addWidget(choose_directory)
widget.addWidget(load_file)
widget.addWidget(finish)

start_window.ui.pushButton.clicked.connect(lambda: widget.setCurrentIndex(1))
choose_directory.ui.pushButton.clicked.connect(lambda: (widget.setCurrentIndex(2),
                                                        load_file.ui.progressBar.repaint(),
                                                        load_file.startProgressBar()))

widget.show()
sys.exit(app.exec_())
