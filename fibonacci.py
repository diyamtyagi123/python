num = int(input("enter the number .. "))
n1, n2 = 0, 1
count = 0
nth=0
if num == 1:
   print(n1)
else:
   while nth < num:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
