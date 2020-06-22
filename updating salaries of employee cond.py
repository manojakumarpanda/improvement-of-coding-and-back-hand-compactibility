#program for the updating the salary of the employee with some conditions

import mysql.connector

cm=mysql.connector.connect(database='practice',user='root',password='root')
print('The database connectivity is success:')
cur=cm.cursor()
cur.execute("update employee set empsal=empsal+(empsal*0.1) where empsal<=18000")
cm.commit()

#fetching all the data from the database and printing in to the console

while True:
    data=cur.fetchone()
    if data==None:
        break
    empno,empname,empdesi,empsal=data
    print('all data are fetch ed', empno, empname, empsal, empdesi)
'''for ch in data:
    print('*'*10,'the data are as fallow','*'*10)
    print(ch)'''


