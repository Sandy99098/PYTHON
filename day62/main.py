# Your Python code goes here

#ACess specifers  or modifiers in Python

class hey:
    def __init__(self):
        self.name="naam mero "
        
a=hey()
print(a.name)

# Private 

class hey:
    def __init__(self):
        self.__name="naam mero "
        
a=hey()
#  it can be access indirectly .by name mangling 
# print(a.___name) #we cannot access because name act as a private  


# Name MANGLING  cannot be accessed directly 
#  using (_CLASSNAME__(value tha you wanna acess) )
# , accessing private  class
class hey:
    def __init__(self):
        self.__name="naam mero "
        
a=hey()
#  it can be access indirectly .by name mangling 
print(a._hey__name) #we cannot access because name act as a private  



# protected   single underscore is just a convention which denote it is protected
class prot:
    def __init__(self):
        self._name="Protected "
        
b=prot()
print(b._name)
