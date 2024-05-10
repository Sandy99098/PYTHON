#Constructor in python
# class person:
    
#     name="Sandeep"
#     occ="Designer"
        
#     def info(self):
#         print(f" I am {self.name} and my job is {self.occ}")

# a=person()
# a.info()

# Example of constructor 
class person:
    #  # Default constructor
    # def __init__(self,n="hari",o="Coder"):
    #     self.name=n
    #     self.occ=o
    #     print("I am a Designer")
    
    #Paramaterized constructor
    def __init__(self,n,o): 
       self.name=n
       self.occ=o
   
        
    def info(self):
        print(f" I am {self.name} and my I am  {self.occ}")
# p = person()
# p.info()
a=person("Sandeep","Developer") # constructor ma 3 ta pass vaaxa 1ta a obj and other are paranaters
a.info()
# print(p)