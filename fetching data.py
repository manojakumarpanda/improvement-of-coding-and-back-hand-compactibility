#programs for fatching the data from databsse with and with out conditions
import mysql.connector

cm=mysql.connector.connect(database='practice',user='root',password='root')
cur=cm.cursor()
cmd=0



cur.execute("select * from user_information")
c=cur.fetchone()
userid,uname,upass,contact=c
print(userid,uname,upass,contact)
