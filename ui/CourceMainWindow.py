import sys
from playsound import playsound
from PySide2 import QtWidgets
from PySide2.QtWidgets import QCompleter
from PySide2.QtWidgets import QMessageBox
from uimainwidnow import Ui_MainWindow
from AddCource import Ui_Dialog
from AddPlatform import Ui_DialogPlatform
from AddInstractor import Ui_DialogInstructor
from AddTag import Ui_DialogTag
from AddTechnology import Ui_DialogTechonology
from databasequers.tagtable import TableTag
from databasequers.Instructortable import TableInstructor
from databasequers.platformtable import TablePlatform
from databasequers.technologytable import TableTechnology
from databasequers.databasecheck.textsuggestion import SuggestionEngine
import os

username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
inputdata = []


def warringsound():
    playsound(r'C:\Users\Nachiket\Documents\Nachiket\My Project\cource\sound\beep.mp3')


def suggestionwidgets(inputlist=[]):
    return inputlist


class NewTechonology(QtWidgets.QDialog, Ui_DialogTechonology):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("New Technology")
        self.inserttech_btn.clicked.connect(self.AddNewTech)
    def AddNewTech(self):
        techtype = self.adtechtype.text()
        assotag = self.adassotag.text()
        if len(techtype) and len(assotag) > 2:
            returnval = TableTechnology.checkexist(techtype)
            if returnval == 1:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Value Error")
                dlg.setText("Technology is already exist ")
                dlg.exec_()
            else:
                TableTechnology.InsertNewTechnology(techtype,assotag)
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Value Error")
            dlg.setText("Place Enter Both Information")
            dlg.exec_()


class NewTag(QtWidgets.QDialog, Ui_DialogTag):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("New Tag")
        self.adtagsubmit_btn.clicked.connect(self.CreateNewTag)
        # suggestiondata = suggestionwidgets()
        # inputdata1 = ['c++', 'ddddsd', 'ddddsdddd', 'erf', 'f', 'javascript']
        # completer = QCompleter(inputdata1)
        # completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        # self.adtag.setCompleter(completer)

    def CreateNewTag(self):
        """This function create new tag """

        tag = self.adtag.text()
        tagdis = self.adtagdis.text()
        if len(tag) and len(tagdis) < 2:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("I have a question!")
            dlg.setText("Sir! Please Enter Valid Input")
            dlg.exec_()
        else:
            TableTag.InsertNewTag(tag, tagdis)


class NewInstructor(QtWidgets.QDialog, Ui_DialogInstructor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("New Instructor")
        self.inInstructor.clicked.connect(self.AddNewInstractor)
        TableInstructor.dropdown(self)
    def AddNewInstractor(self):
        instractorname = self.adinstractorname.text()
        instractortec = self.adinstruactortech.currentText()
        instruactorlinkdin = self.adinstruactorlinkdin.text()
        instractorsoc1 = self.adinstruactorsoc1.text()
        instruactorsco2 = self.adinstruactorsoc2.text()
        returnvalue = TableInstructor.CheckExist(instractorname)
        if returnvalue == 0:
            try:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("I have a question!")
                dlg.setText("The Instractor\n Already Exist...")
                warringsound()
                button = dlg.exec_()
            except Exception as e:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Sound Erro")
                dlg.setText("System is not able to play sound")
                button = dlg.exec_()
        else:
            if len(instractorname) and len(instractortec) and len(instruactorlinkdin) and len(instractorsoc1) and len(
                    instruactorsco2) >= 1:
                """Here the insertion function call"""
                try:
                    TableInstructor.InsertNewInstructor(instractorname, instractortec, instruactorlinkdin,
                                                        instractorsoc1, instruactorsco2)
                except Exception as e:
                    print(e)
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Alert!")
                    dlg.setText("Insertion Operation Failed...")
                    button = dlg.exec_()
            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Value Error")
                dlg.setText("Please enter all entry filed..")
                button = dlg.exec_()


class NewPlatform(QtWidgets.QDialog, Ui_DialogPlatform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("New Platform")
        self.addplt_btn.clicked.connect(self.AddNewPlatform)
    def AddNewPlatform(self):
        platform = self.adplt.text()
        platform_link = self.adpltlink.text()
        returnval = TablePlatform.CheckExist(platform,platform_link)
        if returnval == 1:
            # record already exist
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Value Error")
            dlg.setText("Platform Name or Platform like already Exist ")
            dlg.exec_()
        else:
            # insert new record
            TablePlatform.InsertNewPlatform(platform,platform_link)
            print("record Inserted")
            self.adplt.clear()
            self.adpltlink.clear()
            # update suggestion list




class AnotherWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.w1 = NewPlatform()
        self.w2 = NewTechonology()
        self.w3 = NewTag()
        self.w4 = NewInstructor()
        self.setupUi(self)
        self.setWindowTitle("Cource")
        tagsuggestion = TableTag.tagsuggestion(None);
        completer = QCompleter(tagsuggestion)
        self.astagsug.setCompleter(completer)
        dropdownlist = TablePlatform.suggestionplatform(None)
        self.adcplatform.addItems(dropdownlist)
        tehdropdown=TableTechnology.TechDropDown()
        self.adtech_drop.addItems(tehdropdown)
        self.adPlatform.clicked.connect(self.showAddNewPlatform)
        self.adTechonology.clicked.connect(self.showAddNewTechonology)
        self.adTag.clicked.connect(self.showAddNewTag)
        self.adInstractor.clicked.connect(self.showAddNewInstructor)

    #     Here all update count function call

    def showAddNewPlatform(self, checked):

        self.w1.show()

    def showAddNewTechonology(self):
        self.w2.show()

    def showAddNewTag(self):
        self.w3.show()

    def showAddNewInstructor(self):
        self.w4.show()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.w = AnotherWindow()
        self.setupUi(self)
        self.add_cource.clicked.connect(self.showAddcource)

    def showAddcource(self, checked):
        self.w.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

# TODO: InsertNewPlatform function code
# TODO: in addcource change tag dropdown to line edit
# TODO: create technology database query script
# TODO: add drop down suggestion to technology to courceadd
# TODO: Create fucntionality for addnew techonology