while 1:
    a=input('enter any three digit no. ::')
    SUM=0
    for i in range (len(a)):
        y=(int(a[i])**3)
        SUM+=int(y)

    print (SUM)
    if (SUM==int(a)):
        print ('Yes,the number is armstrong')
    else:
        print ('No,the  number is not armstrong')
    
