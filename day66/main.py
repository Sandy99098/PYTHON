# Your Python code goes here

# instance variables and class variable
class Employee:
    company="Appple"
    number=0
    def __init__(self ,name):
        self.name=name
        self.raiseamt=2
        Employee.number+=1
    def info(self):
        print(f"{self.name}'s raise amount is {self.raiseamt} and  works at{self.company } and total employess are {Employee.number}") 
        # print(f"{self.name} works at {Employee.company} ") 

emp1=Employee("sandy")
emp1.info()
emp2=Employee("Hari")
emp2.raiseamt=4
# Employee.company="Microsoft"
emp2.company="Microsoft"

emp2.info()

