a=input('enter any complex no ::')
b=input('enter any complex no ::')
if (a[0]!='-') and (a[0]!='+'):
    a='+' + a
if (b[0]!='-') and (b[0]!='+'):
    b='+' + b
x=[[],[]]
j=-1
for g in [a,b]:
    count=0
    j+=1
    for i in g:
        if i=='-' or i=='+':
            if count==1:
                x[j].append(z)
            z=i
            count=1
            continue
        z+=i
    x[j].append(z)
real = (int(x[0][0])+int(x[1][0]))
img =(int(x[0][1][0:-1])+int(x[1][1][0:-1]))
if (str(img)[0]!='-') and (str(img)[0]!='+'):
    img='+' + str(img)

print (real,str(img)+'i')


    
        

