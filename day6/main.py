# //learning about variables and datatypes
# datatypes  describes the kind of value a variable possesses and the kinds of mathematical, relational, or logical operations that can be performed on it without leading to an error.
# Variables are used to store and modify data during program execution.

hello="i am fine ";
print("hi how are you  \n ");
print(hello);
a=1;
b=4.5;
c=complex(2,1);
d=None;
e=True;3 

print(a+b,c,d);
m=a+b+c; #we cannot add none value
print (m);
print("the data type of a is ",type(a),)
print("the data type of b is ",type(b),)
print("the data type of c is ",type(c),)
print("the data type of hello is ",type(hello),)
print("the data type of e is ",type(e),)

# list 
# list is the collection of the different datatypes 
# mutable and immutable 
list=[1,2,3,[-4,-5],["hello","hi"]]
print(list);
tuple2=(( "parrot ","pigeon"),("lion", "girrafe"))
print(tuple2); #we cannot change the tuple 
#  map datatype i.e dictionary  also a mapped data 

dict1={"name":"sandeep","age":20,"canvote":True};
print(dict1); 