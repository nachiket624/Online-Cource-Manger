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


class TableTag():
    def InsertNewTag(tag, tagdis):
        cur = conn.cursor()
        cur.execute("INSERT INTO tags (maintag,tag_discription) VALUES ('" + str(tag) + "', '" + str(tagdis) + "')")
        cur.close()
        conn.commit()
        conn.close()

    def TableTagAutoComplite(self):
        cur = conn.cursor()
        autocomplatetext = []
        cur.execute("select maintag from tags")
        for i in cur:
            autocomplatetext.append(i)
        autocomplatetext = filterlistoftupel(autocomplatetext)
        print(autocomplatetext)
        return autocomplatetext

    def Update(tag, tagdis):
        pass

    def tagsuggestion(self):
        cur = conn.cursor()
        cur.execute("""SELECT maintag from tags""")
        tagsug = cur.fetchall()
        tags = filterlistoftupel(tagsug)
        return  tags
