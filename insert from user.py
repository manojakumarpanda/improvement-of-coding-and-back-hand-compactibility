#program to insert the data from the users or the runtime
import mysql.connector

cn=mysql.connector.connect(database='practice',user='root',password='root')
cur=cn.cursor()
command="insert into employee values(%s,%s,%s,%s)"#this will get the value inserted from the keyboard


n=int(input('Enter the number of employee data you want to insert::'))
for i in range(n):
    empid=input('Eneter the employee id ::')
    empnames=input("Enter the name of the employee::")
    empdesign=input('Enter the designation of the employee::')
    empsalary=float(input('Enter the salary of the employee::'))
    cur.execute(command,params=(empid,empnames,empdesign,empsalary))
    cn.commit()
print('The data is inserted in to the database successfully::')

data=cur.fetchall()
for ch in data:
    print('the data inside the database::',ch)



