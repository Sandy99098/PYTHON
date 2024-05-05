#local and global variable 
x=2;
print(x)
a= 5; 
print(f"it is local variable  a {a}") 


def hey():
    print("HEllo ")
    global a # it helps to prevent the error 
    
    a=4 #local variable  
    print(f"it is local variable  a {a}")

hey()
print(f"it is global  variable  a but got override by using global keyword in the function  {a}") 

# print(a) #cannot print the  a because it is not globa; variable

