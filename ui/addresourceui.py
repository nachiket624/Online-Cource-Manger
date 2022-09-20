# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addresource.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(989, 575)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(840, 500, 93, 28))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 30, 171, 21))
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(160, 30, 73, 22))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 130, 891, 311))
        self.frame.setAcceptDrops(False)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"submit", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Resouce Tag", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Python", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Html", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"css", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog", u"javascript", None))

    # retranslateUi

