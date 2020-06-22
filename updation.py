#program for the updation of the salary

import mysql.connector
cm=mysql.connector.connect(database='practice',user='root',password='root')
cr=cm.cursor()
cmd="update employee set empsal=empsal+3000 where empsal>='40000'"
cr.execute(cmd)
cm.commit()
