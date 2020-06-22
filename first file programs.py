#programs for the file handleing first file handling programs
import time


def main():
    f=open('E:\\first_programs','w')#this is the write mode of the file handling
    f.write('hi this is first programs for the file handlings::')
    f.close()
    with open('E:\\first1.txt','w') as file:
        file.writelines('this is the line of code for the file handling and file specification \n and the next line is ::')
        line='this is alternative way of writeing line mode of the file handlings ::\n and in the new line for the file handlings::'
    file.close()
    fi=open('E:\\first1.txt','r')#this command is for the read mode of the file handling
    for ch in range(10):
        res=fi.read(2)
        print(res,end=' ')
        time.sleep(2)
    c=fi.read(5)
    print('The first five characeter of the file is::',c)
    d=fi.read()#this will read till the end of the file if the size is not define the default is -1
    print('this is the full content of the file::',d)


main()
