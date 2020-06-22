#this is another type of program for insertion into the database
import mysql.connector

cn=mysql.connector.connect(database='practice',user='root',password='root')
print('The database connection succesfully::')
cu=cn.cursor()
cmd="insert into employee values(%s,%s,%s,%s)"
data=[(108,'puja sabat','software engineer',25000),(109,'debasish dash','web devloper',20000)]


'''for i in range(len(data)):
    print(data[i])
    cu.execute(cmd,data[i]
    cn.commit()'''
#this is using the for loop and you can do the same in single step only by using the command of executemany
cu.executemany(cmd,data)
cn.commit()
'''
cu.execute(cmd,data)
cn.execute() these statemnts will rais error 'tuple' cannot be converted to a MySQL type'''
print('THe data inserted successfully::')
