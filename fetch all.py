#programs for fetching all the element from the database
import mysql.connector

cm=mysql.connector.connect(database='practice',user='root',password='root')
cur=cm.cursor()
print('THe connection established and the cursor created ::')

cur.execute("select * from student")
data=cur.fetchall()


for row in data:
    print('the first set of data is :',row)
    print('*'*30)

