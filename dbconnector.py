#program for the database connectivity to the python for database student
import mysql.connector
import random

cn=mysql.connector.connect(user='root',password='root',database='practice')
cur=cn.cursor()
print('The database connection is successfull:')


print(random.randint(0,9))