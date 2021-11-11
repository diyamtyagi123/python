# Python code to demonstrate the working of 
# log(a,Base) 

import math 

# Printing the log base e of any number
n=int(input('enter the value::'))
print ("Natural logarithm of n is : ", end="") 
print (math.log(n)) 

# Printing the log base 10 of n
print ("Logarithm base 10 of n is : ", end="") 
print (math.log(n,10)) 
