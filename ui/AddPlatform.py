# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddPlatform.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogPlatform(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1054, 183)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color:rgb(62,58,101);\n"
"	font: 87 10pt \"Arial Black\";\n"
"}\n"
"QLabel{\n"
"	font: 63 10pt \"Open Sans Semibold\";\n"
"	color:rgb(239, 239, 239);\n"
"}\n"
"QLineEdit{\n"
"	height:40;\n"
" 	border-bottom: 6px solid rgb(112,195,253);\n"
"	border-radius:20px;\n"
"	font: 63 10pt \"Open Sans Semibold\";\n"
"	color:rgb(255, 255, 255);\n"
"	background-color:rgb(63,55,95);\n"
"	padding-left:20px;\n"
"}\n"
"QPushButton{\n"
"\n"
"	height:40px;\n"
"	font: 63 10pt \"Open Sans Semibold\";\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 												rgba(122, 195, 253, 233), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius:20px;\n"
"\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(20)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.adplt = QLineEdit(Dialog)
        self.adplt.setObjectName(u"adplt")
        font = QFont()
        font.setFamily(u"Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.adplt.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.adplt)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.adpltlink = QLineEdit(Dialog)
        self.adpltlink.setObjectName(u"adpltlink")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.adpltlink)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.addplt_btn = QPushButton(Dialog)
        self.addplt_btn.setObjectName(u"addplt_btn")
        self.addplt_btn.setMinimumSize(QSize(130, 0))

        self.gridLayout.addWidget(self.addplt_btn, 1, 0, 1, 1, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Pltform Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Platform link", None))
        self.addplt_btn.setText(QCoreApplication.translate("Dialog", u"Insert", None))
    # retranslateUi

