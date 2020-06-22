#program for creating the csv file in the command of python
#from csv import *
import csv


'''fi=open('E://employee.csv','w')
w=csv.write(fi)
w.writerow(['employee name','emp id','designation','empsal','emp dob'])
fi.writerow(['padma charan panda',1113,'head teacher i/c',68000,'20.06.1963'])
fi.close()
'''


file=open('E://employee.csv','w+')
w=file.dictwriter(file,filename=['employee name','emp id','designation','empsal','emp dob'])
w.writedeader()
w.writerow({'employee name':'padma charan panda','emp id':1113,'designation':'head teacher i/c','empsal':68000,'emp dob':'20.06.1963'})
file.close()



