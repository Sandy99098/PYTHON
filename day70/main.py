# Your Python code goes here
class Employee:
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id
        
    @classmethod
    def fromstr(cls,string):
        cls.string=(string.split("-")[0],int(string.split("-")[1]),int(string.split("-")[2]))
        print(f"{cls.string}")
        # print(type(int(string.split("-")[1])))
e=Employee("Sandy",122234,9)
print(e.name)
print(e.salary)
print(e.id)
string="Sandy-3249-09"
e=Employee.fromstr(string)




