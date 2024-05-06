#lambda functions in puython 

# def double(x):
#     return x*2
# print(double(5))

def apl(fx,value):
    return 5+fx(value)

# used to make the mini function 
double = lambda x:x*2 
cube = lambda x:x*x*x
avg= lambda x,y,z : (x+y+z)/3
print(double(5))
print(cube(6))
print(avg(11,23,43))
print(apl(double , 3)) #passsin functions as an arguments
print(apl(lambda x: x*22 , 3)) #passsin functions as an arguments
