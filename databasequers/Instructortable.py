from PySide2.QtWidgets import QMessageBox
from PySide2 import QtWidgets
import mysql.connector
import os
from ui.AddInstractor import Ui_DialogInstructor
from filters.listtuple import filterlistoftupel

username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
conn = mysql.connector.connect(
    host="localhost",
    user=username,
    password=userpass,
    database="courcemanger"
)


class TableInstructor(QtWidgets.QDialog,Ui_DialogInstructor):
    def __init__(self):
        adinstruactortech = self.adinstruactortech
        self.dropdown()

    def CheckExist(instructora_name):
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM instractor WHERE instractor_name = '" + instructora_name + "'")
        number = cur.fetchone()
        if number[0] >= 1:
            return 0;
        else:
            return 1;


    def InsertNewInstructor(instrator_name, techology, linkdin, social1, social2):
        cur = conn.cursor()
        number_cource = 1
        instratorlist = (instrator_name, str(number_cource), techology, linkdin, social1, social2)
        cur.execute(
            """INSERT INTO instractor (instractor_name, number_of_cource, techonology, linkdin, social1, social2) VALUES (%s,%s,%s,%s,%s,%s)""",
            instratorlist)
        cur.close()
        conn.commit()
        conn.close()

    def Update(tag, tagdis):
        pass

    def UpdataCourceCount(self):
        pass

    def dropdown(self):
        self.adinstruactortech.clear()
        cur = conn.cursor()
        cur.execute("SELECT type_of_technology FROM technology")
        item = cur.fetchall()
        convertlist = filterlistoftupel(item)
        self.adinstruactortech.addItems(convertlist)

