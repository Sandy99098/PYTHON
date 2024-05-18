# Your Python code goes here
#  multiple inheritance 

class Employee:
    def __init__(self,name) -> None:
        self.name=name
class Dancer:
   def __init__(self,dance):
       self.danceType=dance

class DancerEmployee(Employee,Dancer):
    def __init__(self, name,danceType) -> None:
      self.name=name
      self.danceType=danceType
      
    def __str__(self):
        return f'name is {self.name} and dance type is {self.danceType}'
        
       
d=DancerEmployee("Shreya","kathak")
print(d)
print(d.name)
print(d.danceType)


# MRO .  METHOD RESOLUTION ORDER

class Employee:
    def __init__(self,name) -> None:
        self.name=name
    def show(self):
        print(f" name is {self.name}")
class Dancer:
   def __init__(self,dance):
       self.danceType=dance

class DancerEmployee(Dancer,Employee): # if both class have functions of same name then . class which is first inherited is shown first . (mro)
    def __init__(self, name,danceType) -> None:   
      self.name=name
      self.danceType=danceType
      
    def show(self):
      print(f" name is {self.danceType}")
        
    def __str__(self):
        return f'name is {self.name} and dance type is {self.danceType}'
        
       
d=DancerEmployee("Shreya","kathak")
print(d)
print(d.name)
print(d.danceType)
d.show()

