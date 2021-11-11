l=[]
while 1:
    
    print('1=add element')
    print('2=remove element')
    print('3=show element')
    choice = input("Enter choice(1/2/3):")
    if choice=='1':
        a=input('enter the number::')
        l.append(a)
    elif choice=='2':
        l.pop()
    elif choice=='3':
        for i in l :
            print (i) 





