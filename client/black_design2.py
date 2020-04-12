from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_List(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 427)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../project_pyqt_test/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: #303030;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setStyleSheet("border: 1px solid #606060; border-radius: 5px;")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 132, 320, 52))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setAcceptDrops(False)
        self.scrollAreaWidgetContents.setStyleSheet("border: hidden;")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.pushButton_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.pushButton_1.setMinimumSize(QtCore.QSize(0, 40))
        # self.pushButton_1.setStyleSheet("background: #424242; border-radius: 5%; color: white;")
        # self.pushButton_1.setObjectName("pushButton_1")
        # self.verticalLayout_2.addWidget(self.pushButton_1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("background: #424242; border-radius: 5%; color: white;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_1.setStyleSheet("background: #424242; border-radius: 5%; color: white;")
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)

        self.verticalLayout.addWidget(self.pushButton)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SParent"))
        self.label.setText(_translate("MainWindow", 'Нажмите на "Поиск"'))
        # self.label.setText(_translate("MainWindow", "Ведёться поиск компьютера внутри сети \n"
        #                                             "Это может занят от 2-х до 3-х минут"))
        self.pushButton_1.setText(_translate("MainWindow", "Поиск"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))
