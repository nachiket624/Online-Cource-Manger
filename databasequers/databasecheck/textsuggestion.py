import mysql.connector
from filters.listtuple import filterlistoftupel
class SuggestionEngine():
    def __init__(self):
        pass
    def SugDbCourceManger(databasename,user,password,column_name,dbtable,incolume,remethod,reword):
        conn = mysql.connector.connect(
            host="localhost",
            user=user,
            password=password,
            database=databasename
        )
        cur = conn.cursor()
        cur.execute("select "+ column_name +" from "+  dbtable +" where "+ incolume+ " regexp '"+remethod+reword+"' ")
        data = []
        curdata = cur.fetchmany(6)
        for i in curdata:
            data.append(i)
        data = filterlistoftupel(data)
        return data
