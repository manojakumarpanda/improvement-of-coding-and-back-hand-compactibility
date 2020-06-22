#programs for the deletion operation by using list and tuple concept
import mysql.connector

cm=mysql.connector.connect(database='practice',user='root',password='root')
cur=cm.cursor()
print('The curser and connection established succesfully::')

lis=list()
cmd="delete from student where rollno=%s"
rollno=int(input('Enter the rollno of the student:: '))
lis.append(rollno)
t=tuple(lis)
cur.execute(cmd,params=t)
c=cur.rowcount
if c==0:
    print('Ingalid rollno you have inserted :: please inserted vaid rollno::')
else:
    print('THe student detaile is deleted successfully')
    cm.commit()