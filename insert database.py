#insert data ino a database

import mysql.connector

cn=mysql.connector.connect(database='practice',user='root',password='root')
cur=cn.cursor()
cmd="insert into student values('8','naina patro','electronics and telecommunication','berhampur');"
cur.execute(cmd)
print('The data inserted successfully ::')
cn.commit()
cur.execute('select * from student;')

