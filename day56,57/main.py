#   reason of using oop 
#  classes and  objects  in python ;
#  examples

# class Person:
#       Name=" Sandeep"
#       Occupation ="Developer"
#       Income=9998

# a=Person()
# print(a.Name,a.Income,a.Occupation)

class Person:
      Name=" Sandeep"
      Occupation ="Developer"
      Income=9998
      def info(self): # self is 
          print(f" {self.Name} is a {self.Occupation}")

a=Person()
b=Person()
a.Occupation="doing well and i am doing well and "
a.info()
b.Name="Harry "
b.Occupation=" Developer  "
b.Income= 90339
b.info()



# example 2
class Hello:
    name="Sandy "
    def info(self):
        print(f" Hello {self.name}")
       
m=Hello()
m.info()

m.name="saan"
m.info()
