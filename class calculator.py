class weld :
    def adding (self):
        return str(self.a)+str(self.b)
    def mult (self):
        return str(self.a)*self.b


class calculator(weld):

    def __init__(self):
        self.a=int(input('enter a number ::'))
        self.b=int(input('enter a number ::'))
 
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

c1=calculator()

print ('addition =', c1.add())
print ('subtraction =',c1.sub())
print ('multiplication =',c1.mul())
print ('division =',c1.div())
print (c1.adding())
print (c1.mult())
