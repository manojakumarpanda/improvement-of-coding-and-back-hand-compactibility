#programs for deleting a row from the database
import mysql.connector

cn=mysql.connector.connect(database='practice',password='bapupanda1995',user='mkpanda')
cur=cn.cursor()
print('The connection establilshed and cursor is created::')



#rolno=int(input('Enter the rollno of the student you want to delete from::'))

bra=input('enter:')
data=cur.execute("select name,address from student where branch=%s",params=(bra,))
da=cur.fetchall()
print(data)
c=cur.rowcount
if c==0:
    print('the roll number you have entered is not exist in the school::')
else:
    print('the student details is deleted from the selceted rollno::')
    cn.commit()

