# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName(_fromUtf8("Home"))
        Home.resize(784, 548)
        self.centralwidget = QtGui.QWidget(Home)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 70, 191, 331))
        self.frame.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(114, 135, 135);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 130, 161, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 170, 161, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_5 = QtGui.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 290, 161, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 210, 161, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 250, 161, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 430, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 460, 151, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(180, 430, 211, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 460, 211, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 40, 531, 351))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 460, 131, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 460, 181, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(580, 430, 181, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 430, 131, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 500, 581, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 500, 181, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        Home.setCentralWidget(self.centralwidget)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(_translate("Home", "MainWindow", None))
        self.pushButton.setText(_translate("Home", "Select Satellite Image", None))
        self.pushButton_2.setText(_translate("Home", "Select dataset", None))
        self.pushButton_3.setText(_translate("Home", "Perform CNN", None))
        self.label_4.setText(_translate("Home", "Control Panel", None))
        self.pushButton_5.setText(_translate("Home", "Exit", None))
        self.pushButton_6.setText(_translate("Home", "Preprocess Image", None))
        self.pushButton_7.setText(_translate("Home", "Predict Social Status", None))
        self.pushButton_4.setText(_translate("Home", "Add User", None))
        self.label.setText(_translate("Home", "Image Preview", None))
        self.label_2.setText(_translate("Home", "Agricultural Land %", None))
        self.label_3.setText(_translate("Home", "Roads Sources %", None))
        self.label_6.setText(_translate("Home", "Structures %", None))
        self.label_7.setText(_translate("Home", "Water Resources %", None))
        self.label_9.setText(_translate("Home", "Economic Status Of Area", None))
        self.label_8.setText(_translate("Home", "ADMIN", None))

