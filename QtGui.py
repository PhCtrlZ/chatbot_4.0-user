# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 651)
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setToolTipDuration(-5)
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setIndent(-10)
        self.label_7.setObjectName("label_7")
        self.time = QtWidgets.QTextEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(280, 70, 251, 51))
        self.time.setFrameShape(QtWidgets.QFrame.Box)
        self.time.setObjectName("time")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 90, 121, 31))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(280, 190, 251, 61))
        self.text.setObjectName("text")
        self.id = QtWidgets.QTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(280, 130, 251, 51))
        self.id.setObjectName("id")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 200, 121, 41))
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 150, 121, 31))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setObjectName("label_5")
        self.english = QtWidgets.QPushButton(self.centralwidget)
        self.english.setGeometry(QtCore.QRect(110, 370, 75, 31))
        self.english.setStyleSheet("selection-color: rgb(85, 255, 0);")
        self.english.setObjectName("english")
        self.vietnam = QtWidgets.QPushButton(self.centralwidget)
        self.vietnam.setGeometry(QtCore.QRect(220, 370, 75, 31))
        self.vietnam.setObjectName("vietnam")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(340, 370, 75, 31))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(460, 370, 75, 31))
        self.stop.setObjectName("stop")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 440, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 280, 121, 51))
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setObjectName("label_6")
        self.profile = QtWidgets.QTextEdit(self.centralwidget)
        self.profile.setGeometry(QtCore.QRect(280, 270, 371, 81))
        self.profile.setObjectName("profile")
        self.cookie = QtWidgets.QPushButton(self.centralwidget)
        self.cookie.setGeometry(QtCore.QRect(570, 370, 81, 31))
        self.cookie.setObjectName("cookie")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "     Auto messenger timer"))
        self.label_3.setText(_translate("MainWindow", "      Set timer"))
        self.label_4.setText(_translate("MainWindow", "    Message text"))
        self.label_5.setText(_translate("MainWindow", "     ID facebook"))
        self.english.setText(_translate("MainWindow", "English"))
        self.vietnam.setText(_translate("MainWindow", "VietNam"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "2022©-Nguyễn Hoàng Phúc"))
        self.label_6.setText(_translate("MainWindow", "    Table profile"))
        self.cookie.setText(_translate("MainWindow", "Get cookie"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())