#program for the user validation if exist in the database or not or login operation

import mysql.connector

cm=mysql.connector.connect(database='practice',user='root',password='root')
cur=cm.cursor()

user=input('Enter the user name for login::')
password=input('Enter the password for the login operations::')
cur.execute("select contact from user_information where  username=%s and password=%s",params=(user,password))
count=cur.rowcount  #this will check the validity of the usename and password and if present the return some vlaue else return 0

if count==0:
    print('The user name and password you have enter{0} and password is not valid for login invalid credentional::')
else:
    #c=cur.fetchone()
    print('Welcome to the website ::')
    print('THe contact number of the persion is ::',cur.fetchone())
