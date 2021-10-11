# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uhome.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 520, 211, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(200, 490, 211, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 560, 181, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(600, 490, 181, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 520, 151, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 90, 191, 331))
        self.frame.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(114, 135, 135);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_5 = QtGui.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 210, 161, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 130, 161, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 170, 161, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(600, 520, 181, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 490, 131, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 490, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 30, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 60, 531, 381))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 560, 581, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 520, 131, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_9.setText(_translate("MainWindow", "Economic Status Of Area", None))
        self.label_3.setText(_translate("MainWindow", "Roads Sources %", None))
        self.pushButton.setText(_translate("MainWindow", "Select Satellite Image", None))
        self.label_4.setText(_translate("MainWindow", "User Panel", None))
        self.pushButton_5.setText(_translate("MainWindow", "Exit", None))
        self.pushButton_6.setText(_translate("MainWindow", "Preprocess Image", None))
        self.pushButton_7.setText(_translate("MainWindow", "Predict Social Status", None))
        self.label_7.setText(_translate("MainWindow", "Water Resources %", None))
        self.label_2.setText(_translate("MainWindow", "Agricultural Land %", None))
        self.label.setText(_translate("MainWindow", "Image Preview", None))
        self.label_6.setText(_translate("MainWindow", "Structures %", None))

