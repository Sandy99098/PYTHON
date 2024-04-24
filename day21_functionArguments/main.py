# ?function arguments 
def average(a,b):
    print("The average is ",(a+b)/2)

average(5,20);

def average(a=5,b=19):
    print("The average is ",(a+b)/2)

# average(5,20); #it will iverride the valu that is given iside the paramaters of the function
def name(fname, mname="bahadur",lname=""): #lname default paramater navayer empty rakhna parxa
    print("Hello!",fname,mname,lname);

name("Hari","Thapa");
name("Shyam","Parsad","Adhikari");

#variable length  arguments

def names(*name):
    print("hello",name[0],name[1],name[2]);
names("ram","shyam","hari");

#example passing arguments as tuple

def average(*numbers):

    print(type(numbers))
    sum=0;#defining sum by 0
    for i in numbers:
        sum= sum+i
    print("Average is",sum/len(numbers) )

average(1,2,3,4)

#example passing arguments as dictionary

def names(**name):
    # print(type(name))
    print("hello",name["fname"],name["mname"],name["lname"])

# names("ram","bahadur","thapa") #itshouldnot be done
names(fname="shyam",mname=" prasad",lname="adhikari")

#return 
def average(*numbers):

    print(type(numbers))
    sum=0;#defining sum by 0
    for i in numbers:
        sum= sum+i
    return sum/len(numbers) 

a=average(1,2,3,4)
print(a)