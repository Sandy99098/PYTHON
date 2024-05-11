# Your Python code goes here

# instance variables and class variable
class Employee:
    company="Appple"
    number=0
    def __init__(self ,name):
        self.name=name
        Employee.number+=1
    def info(self):
        print(f"{self.name} works at{self.company } and total employess are {Employee.number}") 
        # print(f"{self.name} works at {Employee.company} ") 

emp1=Employee("sandy")
emp1.info()
emp2=Employee("Hari")
# Employee.company="Microsoft"
emp2.company="Microsoft"

emp2.info()

