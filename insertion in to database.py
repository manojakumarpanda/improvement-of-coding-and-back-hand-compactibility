#this will insert in to database
import mysql.connector
cn=mysql.connector.connect(user='mkpanda',password='bapupanda1995',database='practice')
cur=cn.cursor()
print('The database connection is successfull:')
cur.execute("insert into student values('7','amruta ','electronics and telecommucication','gopalpur');")
cn.commit()
