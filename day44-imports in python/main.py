# how import works in python
import math
floor=math.floor(1.23)
print(floor)
from math import sqrt,pi
# from math import  # however it is not recommended 
r=5
print(f" area of circle is {pi*((r)**2)}")


import math as m
print(f"square root of 4 is {m.sqrt(4)}")

# dir function . print all the functions  that are in math

import math
print (dir (math))


# importin module 
from sandeep import welcome,sandeep
# from sandeep *
welcome()
print(sandeep)

#example
import math as mt
a=int(input("Enter the radius"))
print("Area of circle is ",mt.pi*a**2)
