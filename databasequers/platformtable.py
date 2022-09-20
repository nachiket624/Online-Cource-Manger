from PySide2 import QtWidgets
import mysql.connector
import os
from filters.listtuple import filterlistoftupel
# from ui.CourceMainWindow import NewPlatform
# from ui.AddPlatform import Ui_DialogPlatform
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
conn = mysql.connector.connect(
    host="localhost",
    user=username,
    password=userpass,
    database="courcemanger"
)
platformsuggesstion = []
class TablePlatform():
    def __init__(self):
        pass
    def CheckExist(platform,platform_link):
        """ This function check the existing value if value
         is exist than dialog appear of not then value
        insert to database  """
        check = [platform,platform_link]
        cur = conn.cursor()
        cur.execute("""select count(*) from  platform where platform_name = %s or platform_link = %s""",check)
        number = cur.fetchone()
        print(type(number),number)
        if number[0] >= 1:
            return 1
        else:
            return 0

    def InsertNewPlatform(platform,platform_link):
        """This function Insert new platform details"""
        cur = conn.cursor()
        number_of_cource = 1
        insertdata = [platform,number_of_cource,platform_link]
        cur.execute("""Insert into platform (platform_name, number_of_cource, platform_link) values(%s,%s,%s)""",insertdata)
        cur.close()
        conn.commit()
        conn.close()
    def updatecount(self,platformid):
        """This function increment the count of number of course if the
        course is already exist """
        pass
    def suggestionplatform(self):
        cur = conn.cursor()
        cur.execute("""select platform_name from platform""")
        platform_list = cur.fetchall()
        platform_listsug = filterlistoftupel(platform_list)
        return platform_listsug

