# Your Python code goes here
#  Inheritance in Python 
class Employee:
    def __init__(self,name,occupation):
        self.n=name 
        self.o = occupation
    def info(self):
        print(f"Employee name is {self.n} and occupation is {self.o}")
        
        
# inheritating programmer from employee class 
class Programming(Employee):
    def showLanguages(self):
        print(f" The Default language is Python ")
    
a=Employee("san","Designer")
a.info()

a=Employee("sandy","Artist")
a.info()
a1=Programming("saan","Programmer")
a1.showLanguages()


    