#  map ,filter and reduce in pythons 
# use in advance data manapulation 
def cube (x):
    return x*x*x 
print(cube(2))
l=[1,2,3,4,5]

# for computinfg cube of the list
# newl=[]
# for item in l:
#     newl.append(cube (item ))
# print(newl)

newl=list(map(cube,l))
print(newl)

# filer (it a can also take lambda as an arguments)
print("filter example : ");
def filter_function(a):
    return a>4 #retun only true and is passsed to the list

list2= list(filter(filter_function,l))

print(list2)

# reduce .also a higher order function
print ("reduce Example")
from functools import reduce
list=[1,3,4,5,4]
#  first ma 1+3= 4 +4= 8+5= 13 +4 = 17 hunxa
def sum(x,y):
    return x+y
sum = reduce( sum, list )
print (sum )
