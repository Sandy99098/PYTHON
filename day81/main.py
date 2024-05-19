# Your Python code goes here
#  hybrid inheritance and hireracial inheriaance

class Animal:
    def __init__(self ,atype) -> None:
        self.atype=atype
    def __str__(self):
        return f" This is a {self.atype} animal "
    
class AnimalType (Animal):
    def __init__(self, atype, lAtype) -> None:
        super().__init__(atype)  
        self.lAtype=lAtype
    def __str__(self):
        return f'This is {self.atype} animal which is a {self.lAtype} animal type'
        
class Dog (AnimalType , Animal):
    def __init__(self,atype,lAtype ,aName) -> None:
        super().__init__( lAtype,atype)
        self.aName=aName
        
    def __str__(self):
        return f'This is animal which is a {self.lAtype} animal type And it is a {self.aName} and is a {self.atype}'
a=Animal("terrestrial")
print (a)

l=AnimalType("mammal","terrestrial")   
print (l)
       
d=Dog("Terrestrial","mammal","Golden Retiver")
print (d)