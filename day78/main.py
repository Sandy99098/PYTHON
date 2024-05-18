#  single inheritance 

class Animal:
    def __init__(self,name,color):
        self.name=name 
        self.color=color
        
    def make_sound(self):
        print(f'sound made by an animal ')        
    
class Cat(Animal):
    def ___init__(self,name,breed):
        Animal. __init__(self,name,species="Cat")
        self.breed=breed
        print(f"cat's breed{self.breed}")
                     
        
        
    def make_sound(self):
        print(f' Meow! ')        
    
        
        
a=Animal("Cat","black")
c=Cat("cat","cat's breed")
a.make_sound()

c.make_sound()
