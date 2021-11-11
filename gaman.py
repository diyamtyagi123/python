def cal(x,y,sign):
    if sign =='1':  print (str(x)+'+'+str(y)+' = '+str(x+y))
    elif sign =='2':  print (str(x)+'-'+str(y)+' = '+str(x-y))
    elif sign =='3':  print (str(x)+'*'+str(y)+' = '+str(x*y))
    elif sign =='4':  print (str(x)+'/'+str(y)+' = '+str(x/y))
while 1:
    print('Choose Calculation \n 1.Add \n 2.Subtract \n 3.multiply \n 4.Divide')
    sign , x, y =input('Enter Calculation:') , input('Enter first No:') , input('Enter sec. No:')
    cal(int(x) , int(y) , sign)
