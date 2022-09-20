# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddInstractor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogInstructor(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1048, 381)
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
"QComboBox{\n"
"	height:40;\n"
"	border-bottom: 6px solid rgb(112,195,253);\n"
"	border-radius:20px;\n"
"	font: 63 10pt \"Open Sans Semibold\";\n"
"	color:rgb(255, 255, 255);\n"
"	background-color:rgb(63,55,95);\n"
"	padding-left:20px;\n"
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

        self.adinstractorname = QLineEdit(Dialog)
        self.adinstractorname.setObjectName(u"adinstractorname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.adinstractorname)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.adinstruactortech = QComboBox(Dialog)
        self.adinstruactortech.addItem("")
        self.adinstruactortech.addItem("")
        self.adinstruactortech.addItem("")
        self.adinstruactortech.addItem("")
        self.adinstruactortech.addItem("")
        self.adinstruactortech.addItem("")
        self.adinstruactortech.setObjectName(u"adinstruactortech")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.adinstruactortech)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.adinstruactorlinkdin = QLineEdit(Dialog)
        self.adinstruactorlinkdin.setObjectName(u"adinstruactorlinkdin")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.adinstruactorlinkdin)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.adinstruactorsoc1 = QLineEdit(Dialog)
        self.adinstruactorsoc1.setObjectName(u"adinstruactorsoc1")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.adinstruactorsoc1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.adinstruactorsoc2 = QLineEdit(Dialog)
        self.adinstruactorsoc2.setObjectName(u"adinstruactorsoc2")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.adinstruactorsoc2)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.inInstructor = QPushButton(Dialog)
        self.inInstructor.setObjectName(u"inInstructor")
        self.inInstructor.setMinimumSize(QSize(130, 0))

        self.gridLayout.addWidget(self.inInstructor, 1, 0, 1, 1, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Instractor Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Techonology", None))
        self.adinstruactortech.setItemText(0, QCoreApplication.translate("Dialog", u"Python1", None))
        self.adinstruactortech.setItemText(1, QCoreApplication.translate("Dialog", u"Python", None))
        self.adinstruactortech.setItemText(2, QCoreApplication.translate("Dialog", u"C++", None))
        self.adinstruactortech.setItemText(3, QCoreApplication.translate("Dialog", u"Java", None))
        self.adinstruactortech.setItemText(4, QCoreApplication.translate("Dialog", u"Web Dev", None))
        self.adinstruactortech.setItemText(5, QCoreApplication.translate("Dialog", u"Math3", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"Linkdin", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Social 1", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Social 2", None))
        self.inInstructor.setText(QCoreApplication.translate("Dialog", u"Insert", None))
    # retranslateUi

