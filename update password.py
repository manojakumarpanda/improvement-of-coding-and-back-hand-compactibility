#program for the updation of the password for the user

import mysql.connector

cn=mysql.connector.connect(database='practice',user='root',password='root')
print('the database conectivity sucess::')
cur=cn.cursor()
cmd="update user_information set password=%s where username=%s and password=%s"
user=input('Entre the username for what you want to change the password::')
opassw=input('Enter the old  password ::')
npassw=input('ENter the new password ::')
cur.execute(cmd,params=(npassw,user,opassw))
c=cur.rowcount


if c==0:
    print('The user name or password is invalid please check::')
else:
    print('The password for the username ={} is updated successfully::'.format(user))
    cn.commit()