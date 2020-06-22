#progrma for the vlaidatio of the user details:
import mysql.connector

con=mysql.connector.connect(database='practice',user='root',password='root')
cur=con.cursor()
print('The usr name and the password is valid and the database connection is established::')
user=input('Enter the user name for login operation ::')
cur.execute("select * from user_information where username=%s",params=(user,))
r=cur.rowcount  #this statemnt will check if there is the usrname is exist or not


if r!=0: #this will check for the validation of the user name
    print('The username is matched succesfully now enter the vlaid password::')
    password=input('Enter the password for the user name{}::'.format(user))
    cur.execute("select * from user_information where username=%s and password=%s",params=(user,password))
    result=cur.rowcout  #this will check for the validation for the username and password

    if result!=0:
        print('The user login is success "Welcome to the website"')
        con.commit()
    else:
        print('The password you have entered is wrong please enter a valid password::')
else:
    print('The user name of the user is not valid enter the corect username::')

print('the execution is success ::')