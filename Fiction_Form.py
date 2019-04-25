# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fiction_Form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 570)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 170, 255);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_fpath = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_fpath.setGeometry(QtCore.QRect(180, 130, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_fpath.setFont(font)
        self.txt_fpath.setObjectName("txt_fpath")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 310, 121, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lbl_Error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Error.setGeometry(QtCore.QRect(10, 480, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_Error.setFont(font)
        self.lbl_Error.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 0, 0);")
        self.lbl_Error.setText("")
        self.lbl_Error.setObjectName("lbl_Error")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 480, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbl_new_path = QtWidgets.QLabel(self.centralwidget)
        self.lbl_new_path.setGeometry(QtCore.QRect(180, 210, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_new_path.setFont(font)
        self.lbl_new_path.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 0, 0);")
        self.lbl_new_path.setText("")
        self.lbl_new_path.setScaledContents(False)
        self.lbl_new_path.setObjectName("lbl_new_path")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.pushButton_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fiction_Sort"))
        self.label.setText(_translate("MainWindow", "小说排序重组"))
        self.label_2.setText(_translate("MainWindow", "小说路径："))
        self.pushButton.setText(_translate("MainWindow", "重组"))
        self.label_4.setText(_translate("MainWindow", "tips:小说章节顺序错乱或者章节有重复，可以进行重组（txt格式）"))
        self.label_3.setText(_translate("MainWindow", "重组后路径："))

