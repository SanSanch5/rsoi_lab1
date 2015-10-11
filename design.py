# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ppAuthForm(object):
    def setupUi(self, ppAuthForm):
        ppAuthForm.setObjectName("ppAuthForm")
        ppAuthForm.resize(592, 146)
        self.authClick = QtWidgets.QPushButton(ppAuthForm)
        self.authClick.setGeometry(QtCore.QRect(20, 60, 161, 23))
        self.authClick.setObjectName("authClick")
        self.splitter = QtWidgets.QSplitter(ppAuthForm)
        self.splitter.setGeometry(QtCore.QRect(20, 88, 531, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.funcCloseClick = QtWidgets.QPushButton(self.splitter)
        self.funcCloseClick.setObjectName("funcCloseClick")
        self.lblAnsClose = QtWidgets.QLabel(self.splitter)
        self.lblAnsClose.setObjectName("lblAnsClose")
        self.splitter_2 = QtWidgets.QSplitter(ppAuthForm)
        self.splitter_2.setGeometry(QtCore.QRect(20, 30, 531, 27))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.funcOpenClick = QtWidgets.QPushButton(self.splitter_2)
        self.funcOpenClick.setObjectName("funcOpenClick")
        self.lblAnsOpen = QtWidgets.QLabel(self.splitter_2)
        self.lblAnsOpen.setObjectName("lblAnsOpen")

        self.retranslateUi(ppAuthForm)
        QtCore.QMetaObject.connectSlotsByName(ppAuthForm)

    def retranslateUi(self, ppAuthForm):
        _translate = QtCore.QCoreApplication.translate
        ppAuthForm.setWindowTitle(_translate("ppAuthForm", "Pay Pal Auth"))
        self.authClick.setText(_translate("ppAuthForm", "Авторизоваться"))
        self.funcCloseClick.setText(_translate("ppAuthForm", "Выполнить закрытую функцию"))
        self.lblAnsClose.setText(_translate("ppAuthForm", "TextLabel"))
        self.funcOpenClick.setText(_translate("ppAuthForm", "Выполнить открытую функцию"))
        self.lblAnsOpen.setText(_translate("ppAuthForm", "TextLabel"))

