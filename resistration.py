#program for the user resistration

import mysql.connector

cm=mysql.connector.connect(database='practice',user='root',password='root')
cur=cm.cursor()
print('the connection succes')

username=input('Enter the user name ::')
password=input('Enter the password::')
userid=int(input('Enter the userid for the user::'))
mobileno=input('Enter the mobile number to the user')
cur.execute("insert into user_information values(%s,%s,%s,%s)",params=(userid,username,password,mobileno))
cm.commit()

