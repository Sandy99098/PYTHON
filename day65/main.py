# Your Python code goes here
# Static Method  it doesnot instance nor class ( self os instance)

class Math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num+=n
    @staticmethod
    def add(a,b):
        print(a+b)
        return a+b
    
a=Math(9)
print(a)
a.addtonum(4)
print(a.num)

a.add(1,2)
Math.add(1,2) # can be also called by class name

