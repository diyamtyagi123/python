#program to calculate the value of ( 1^2 + 2^2 + 3^2 + ---------- n^2 )
# user gives the input 
n=int(input('enter the last value of the series :: '))
# using the formula of sum of series
val= (n*(n+1)*(2*n+1))
print ('The sum of series is  -  ',val/6)
