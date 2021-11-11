myfile = open(r'C:\Users\Niraj\Documents\python.txt','r')
str=''
while str:
    str = myfile.readline()
    print(str,end='')
myfile.close()

