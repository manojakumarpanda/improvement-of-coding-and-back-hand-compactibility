#programs to find the number of character and word present in the file
import time

'''
count,word=0,0
with open('E:\\python programs\\length_file.txt','w') as file:
    line=input('Enter some string for the file handling operations::')
    file.write(line)
    file.close()
size=open('E:\\length_file.txt','r')
while True:
    ch=size.read(1)
    if ch!='':
        count+=1
    else:
        break

for ch in range(count):
    cha=size.read(1)
    if cha==' ':
        word+=1

print('the number of the word present in the file is {0} and the number of character{1}'.format(word,count))

'''
def main():
    f=open('E:\\first1.txt','r')
    line1=f.read()

    #line2=f.readline(10)
    print(line1)
    time.sleep(2)
    #print(line2)
    line1=list(line1)
    for i in line1:
        print(i)

main()
