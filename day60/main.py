# Your Python code goes here
#  Getters and setters in python
# # Getters
print("Getters")
class Operation():
    def __init__(self,value):
        self.val=value
    def show(self):
     print(f" The value is {self.val} ")
     
    @property
    def mul_values(self):
        return 3*self.val # it is getter 
        
o=Operation(19)
o.show()
print(o.mul_values)



# #setters

class Operation():
    def __init__(self,value):
        self.val=value
    def show(self):
     print(f" The value is {self.val} ")
     
    @property
    def mul_values(self): # it works as a getter by using property . used for encapsulation
        return 3*self.val # 
        
    @mul_values.setter
    def mul_values(self,new_val): # setters
        self.val= new_val/10;
        
o=Operation(10)
print(o.mul_values)
o.mul_values=90 # setters 
o.show()

# example
class Demo:
    def __init__(self,value):
        self.v=value
    def info(self):
        print(f"The value is {self.v} ")
        
    @property
    def new_value(self):
        return 5+self.v
    
d=Demo(9)

d.info()

print(d.new_value )

# for setters
class Demo:
    def __init__(self,value):
        self.v=value
    def info(self):
        print(f"The value is {self.v} ")
        
    @property
    def new_value(self):
        return self.v*3
    
    @new_value.setter
    def new_value(self,val):
        self.v=9+val
    
d=Demo(9)

d.info()

d = Demo(5)
print("from getter ",d.new_value)  # Output: 15
d.info()
d.new_value= 9
d.info()

