# matchcase statements in python
a=input("enter the value of a :");
a=int(a)
# a is the value for match 
#if the first case is matche ,it ignores the other
match a:
    case 0:
        print(" this is case 0");
    case 2:
        print(" This is case 2");
    case 5:
        print(" this is case 5 ");
    
    case _ if(a!=100) :
        print(a," is not 100")
    
    case _ :
        print("this is default case and value of a is ",a)

