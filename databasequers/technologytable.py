import mysql.connector
import os
from filters.listtuple import filterlistoftupel
from databasequers.databasecheck.textsuggestion import SuggestionEngine

username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
conn = mysql.connector.connect(
    host="localhost",
    user=username,
    password=userpass,
    database="courcemanger"
)

class TableTechnology():
    def checkexist(technoloy):
        check = [technoloy]
        cur = conn.cursor()
        cur.execute("""select count(*) from technology where type_of_technology = %s """, check)
        number = cur.fetchone()
        print(type(number), number)
        if number[0] >= 1:
            return 1
        else:
            return 0

    def InsertNewTechnology(technoloy,assoTag):
        insertdata = [technoloy,assoTag]
        cur = conn.cursor()
        print("""INSERT INTO technology (type_of_technology, associate_tag) VLAUES (%s,%s)""",insertdata)

        cur.execute("""INSERT INTO technology (type_of_technology, associate_tag) Values (%s,%s)""",insertdata)
        cur.close()
        conn.commit()
        conn.close()
    def TechDropDown():
        cur = conn.cursor()
        cur.execute("""SELECT type_of_technology FROM technology""")
        techsug_list = cur.fetchall()
        techsug = filterlistoftupel(techsug_list)
        return techsug

