# Your Python code goes here

#  Operator Overloading Python 
class Vector:
    def __init__(self,i,j,k)  :
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self,x):
        return Vector( {self.i+x.i},{self.j+x.j},{self.k+x.k})   # changing str into vector type 
        
v=Vector(1,3,4)
print(v)
v2=Vector(1,2,8)
print(v2)
print(v+v2)
print(type(v+v2))


#  for multiplication
class Multiplication:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
        
    def info(self):
             self.a=self.num1* self.num2
             return f'{self.a}'
            
    def __mul__(self,other):
        
        self.n=self.num1* self.num2
        print("multiplication of m and m2 is ")
        return (self.n) *(other.num1 * other.num2) 
          
    def __str__(self) -> str:
         return f' Multiplication of {self.num1} and {self.num2} is'
        
m=Multiplication(2,4)
m2=Multiplication(2,8)
print(m,m.info())
print(m2,m2.info())
print(m*m2)




