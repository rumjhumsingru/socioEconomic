from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QFileDialog
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time 
import login
import home
import add
import err_add
import uhome
import error_log
import err_img
import MySQLdb
import numpy as np
import cv2
import os


fname=""

class ExampleApp(QtGui.QMainWindow, login.Ui_UserLogin):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.log)
        self.pushButton_2.clicked.connect(self.can)
        
    def log(self):
        i=0
        db = MySQLdb.connect("localhost","root","root","socio")
        cursor = db.cursor()
        a=self.lineEdit.text()
        b=self.lineEdit_2.text()
        sql = "SELECT * FROM users WHERE username='%s' and password='%s'" % (a,b)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                i=i+1
        except Exception as e:
           print e
        
        if i>0:
            if a=="admin":
                print "admin login success"
                self.hide()
                self.home=home()
                self.home.show()
            else:
                print "user login success"
                self.hide()
                self.uhome=uhome()
                self.uhome.show()
            
        else:
            print "login failed"
            self.errlog=errlog()
            self.errlog.show()
                    
        db.close()
        
    def can(self):
        sys.exit()
        
   
class addNew(QtGui.QMainWindow, add.Ui_AdNewUser):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save1)
        self.pushButton_3.clicked.connect(self.can2)

    def can2(self):
        self.hide()
        #sys.exit()
        
    def save1(self):
        db1 = MySQLdb.connect("localhost","root","root","socio")
        cursor1 = db1.cursor()
        name=self.lineEdit.text()
        email=self.lineEdit_2.text()
        contact=self.lineEdit_3.text()
        uname=self.lineEdit_4.text()
        pwd=self.lineEdit_5.text()
        sql = "INSERT INTO users(name, email, contact, username, password) VALUES ('%s', '%s', '%s', '%s', '%s' )" % (name,email,contact,uname,pwd)
        try:
                cursor1.execute(sql)
                self.hide()
                db1.commit()
        except Exception as e:
                print e
                db1.rollback()
                self.erradd=erradd()
                self.erradd.show()
            

        db1.close()
        

class home(QtGui.QMainWindow, home.Ui_Home):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.addNew1)
        self.pushButton.clicked.connect(self.selimg)
        self.pushButton_2.clicked.connect(self.seldir)
        self.pushButton_5.clicked.connect(self.ex)
        self.pushButton_6.clicked.connect(self.preproc)

    def addNew1(self):
        self.addNew=addNew()
        self.addNew.show()

    def selimg(self):
        global fname
        self.QFileDialog = QtGui.QFileDialog(self)
        #self.QFileDialog.show()
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\',"Image files (*.jpg *.png)")
        print fname
        label = QLabel(self.label_5)
        pixmap = QPixmap(fname)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(),pixmap.height())
        label.show()

    
    def seldir(self):
        self.QFileDialog = QtGui.QFileDialog(self)
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        print folder
        

    def preproc(self):
        global fname
        if fname=="":
            self.errimg=errimg()
            self.errimg.show()
        else:
            filename = fname
            print "file for processing",filename
            image =cv2.imread(str(filename))
            #print type(image)
            cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 27, 40)
            cv2.imshow("4 - Canny Edges", edged)

   
            
    def ex(self):
        sys.exit()
        
class uhome(QtGui.QMainWindow, uhome.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.uselimg)
        self.pushButton_5.clicked.connect(self.uex)
        self.pushButton_6.clicked.connect(self.upreproc)
  

    def uselimg(self):
        global fname
        self.QFileDialog = QtGui.QFileDialog(self)
        #self.QFileDialog.show()
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\',"Image files (*.jpg *.png)")
        print fname
        label = QLabel(self.label_5)
        pixmap = QPixmap(fname)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(),pixmap.height())
        label.show()

        

    def upreproc(self):
        global fname
        if fname=="":
            self.errimg=errimg()
            self.errimg.show()
        else:
            filename = fname
            print "file for processing",filename
            image =cv2.imread(str(filename))
            #print type(image)
            cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 270, 400)
            cv2.imshow("4 - Canny Edges", edged)

   
            
    def uex(self):
        sys.exit()
        
class errlog(QtGui.QMainWindow, error_log.Ui_Error):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok1)
    def ok1(self):
        self.hide()

class errimg(QtGui.QMainWindow, err_img.Ui_Error):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok1)
    def ok1(self):
        self.hide()

class erradd(QtGui.QMainWindow, err_add.Ui_Error):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok1)
    def ok1(self):
        self.hide()


def main():
    app = QtGui.QApplication(sys.argv)  
    form = ExampleApp()                 
    form.show()                         
    app.exec_()                         


if __name__ == '__main__':              
    main()                             
