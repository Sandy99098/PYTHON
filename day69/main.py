# Your Python code goes here
#Class methods in python 
class Employee:
    company ="Apple"
    name="Hari"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
        
    @classmethod #by using this class variable is changed
    def changeCompany(cls,newCompany):
        cls.company=newCompany
a=Employee()
# print( a.name)
a.show()
a.changeCompany("Tesla")
a.show()
print(Employee.company)  # it will show the default value of company and donot change the value of the company . so we use classmethod decorator to change the class variable


 
