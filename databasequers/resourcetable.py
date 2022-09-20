import mysql.connector
import os
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
conn = mysql.connector.connect(
      host="localhost",
      user=username,
      password=userpass,
      database = "courcemanger"
    )
class Resource():
  def __init__(self):
    pass
  def addResource(self,filepath,resource_tag):
    cur = conn.cursor()
    print(filepath)
    for j,i in filepath:
        print(r"""INSERT INTO resource1 (resource,resource_type, resourcetag, resource_code) VALUES""" +filepath[j]+""", 'jpg', 'person, woman', '3')""")
    cur.close()
    conn.commit()
    conn.close()



res = Resource()
mytuple = ('C:/Users/Nachiket/Downloads/temp.png', 'C:/Users/Nachiket/Downloads/certificate.pdf', 'C:/Users/Nachiket/Downloads/certificate (3).pdf')
res.addResource(mytuple)