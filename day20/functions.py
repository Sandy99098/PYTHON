#functions
# a=5;
# b=10;
# gmean=(a*b)/(a+b)

#function

def calculateGmean(a,b):
    gmean=(a*b)/(a+b)
    print("geometric mean is ",gmean)
    return gmean ;
calculateGmean(8,9)
print("geometric mean2 is",calculateGmean(7,6) )    

#to calculate the area 
a=int(input("enter the lenght a: "));
b=int(input("enter the breadth b: "));
def area(a,b):
    area=a*b ;
    print("the area is :",area)
    return area;
area(a,b)

#to find the greatest or smallest number 
a=int(input("enter the value of a :"));
b=int(input("enter the value of b"));
def compare(a,b):
    if(a>b):
        print("First Numberis greater than b :");
    else:
        print("Second Numberis greater ")
compare(a,b)

c=int(5)
m=int(10)
compare(c,m)

#writing function later 
def isLesser(a,b):
    pass 

