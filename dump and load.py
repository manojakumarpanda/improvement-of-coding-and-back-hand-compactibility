#this programs is for the pickles modules and with the use of the dump and load for starilaztion and destarilazition

from pickle import *
class student:
    schoolname='Naresh informationn technology'
    def __init__(self,names,rono):#,address,branch,semistar):
        self.rollno=rono
        self.name=names
s=student('naresh','12')
f=open('E:\\file.txt','wb')
dump(s,f)
f.close()

file=open('E:\\file.txt','rb')
l=load(file)
print(l)
f.close()
