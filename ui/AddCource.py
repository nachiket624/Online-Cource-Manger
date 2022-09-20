# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddCource.ui'
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
        Dialog.resize(1062, 623)
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
"	\n"
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
"QPushButton{\n"
"	height:40px;\n"
"	font: 63 10pt \"Open Sans Semibold\";\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(122, 195, 253, 233), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius:20px;\n"
"\n"
"\n"
"}\n"
"QDoubleSpinBox{\n"
"	color:rgb(255, 255, 255);\n"
"	height:40;\n"
"	border-bot"
                        "tom: 6px solid rgb(112,195,253);\n"
"	font: 63 10pt \"Open Sans Semibold\";\n"
"	background-color:rgb(63,55,95);\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"	padding-left:10px;\n"
"}")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(223, 0))

        self.gridLayout_2.addWidget(self.pushButton_6, 2, 0, 1, 1, Qt.AlignHCenter)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.adTechonology = QPushButton(Dialog)
        self.adTechonology.setObjectName(u"adTechonology")

        self.gridLayout.addWidget(self.adTechonology, 3, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.adcplatform = QComboBox(Dialog)
        self.adcplatform.setObjectName(u"adcplatform")

        self.gridLayout.addWidget(self.adcplatform, 1, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout.addWidget(self.doubleSpinBox, 2, 1, 1, 1)

        self.astagsug = QLineEdit(Dialog)
        self.astagsug.setObjectName(u"astagsug")
        self.astagsug.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.astagsug, 7, 1, 1, 1)

        self.adTag = QPushButton(Dialog)
        self.adTag.setObjectName(u"adTag")

        self.gridLayout.addWidget(self.adTag, 7, 2, 1, 1)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(151, 0))

        self.gridLayout.addWidget(self.comboBox, 2, 2, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.adtech_drop = QComboBox(Dialog)
        self.adtech_drop.setObjectName(u"adtech_drop")

        self.gridLayout.addWidget(self.adtech_drop, 3, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_3, 5, 1, 1, 1)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEdit_4, 8, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)

        self.adInstractor = QPushButton(Dialog)
        self.adInstractor.setObjectName(u"adInstractor")

        self.gridLayout.addWidget(self.adInstractor, 5, 2, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.adPlatform = QPushButton(Dialog)
        self.adPlatform.setObjectName(u"adPlatform")

        self.gridLayout.addWidget(self.adPlatform, 1, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_8.setBuddy(self.pushButton)
        self.label_9.setBuddy(self.lineEdit_3)
        self.label.setBuddy(self.lineEdit)
        self.label_4.setBuddy(self.adtech_drop)
        self.label_7.setBuddy(self.lineEdit_4)
        self.label_2.setBuddy(self.adcplatform)
        self.label_5.setBuddy(self.lineEdit_2)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit, self.adcplatform)
        QWidget.setTabOrder(self.adcplatform, self.adPlatform)
        QWidget.setTabOrder(self.adPlatform, self.adtech_drop)
        QWidget.setTabOrder(self.adtech_drop, self.adTechonology)
        QWidget.setTabOrder(self.adTechonology, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.adInstractor)
        QWidget.setTabOrder(self.adInstractor, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.adTag)
        QWidget.setTabOrder(self.adTag, self.lineEdit_4)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Tag", None))
        self.adTechonology.setText(QCoreApplication.translate("Dialog", u"New Technology", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Certificate", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Instructor", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"CourceTitle", None))
        self.adTag.setText(QCoreApplication.translate("Dialog", u"New Tag", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Minutes", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Hours", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Days", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Week", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Month", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Years", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Technology Type", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Dialog", u"this is auto genrate", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Duration", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.adInstractor.setText(QCoreApplication.translate("Dialog", u"New Instructor", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Resource code", None))
        self.adPlatform.setText(QCoreApplication.translate("Dialog", u"New Platform", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Platform", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Cource link", None))
    # retranslateUi

