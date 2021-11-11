a=int(input('enter the no. ::'))
for i in range (1,a):
    prime=('yes')
    for n in range (2,i):
        if(i%n==0):
            prime=('no')
            break
    if (prime=='yes'):
        print(i)
    
