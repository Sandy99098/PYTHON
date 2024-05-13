# Your Python code goes here
# dir, __dict__,help  methods
x=[1,2,3,4]
dir(x)
print(dir(x)) #  return the list of the attributes 

class hey():
     def __init__(self,name,age ):
         self.name=name 
         self.age=age
         self.verison=1
p=hey("sdf",34)
print(p.__dict__)
print(f"dir in class is{dir(p)}")
help(p)
