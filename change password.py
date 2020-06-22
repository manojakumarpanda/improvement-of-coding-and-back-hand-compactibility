#program to updating password of the user
import mysql.connector

cn=mysql.connector.connect(database='practice',user='root',password='root')
cur=cn.cursor()
print('The connection established and the cursore is created::')
old=input('Enter the old password::')
user=input('Enter the user name of ::')
new=input('Enter the new password ::')


cur.execute("update user_information set password=%s where username=%s and password=%s",params=(new,user,old))
c=cur.rowcount
if c==0:
    print('The user name or password is not valid::')
else:
    print('The password is updated successfully ::')
    cn.commit()
