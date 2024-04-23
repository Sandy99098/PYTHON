#if else,elif  statement 
age=int(input("enter your age \n"));
print(" \nyour age is : ",age );
#voting system 
if(age>=18 and age<=100):
    print("you can vote ")
elif(age<18):
     print("you cannot vote" );
else:
    print("enter the valid date")
# to check wether the number is positive or not 
num=int(input("enter a number"));
print("tne number is ",num);
if(num<0):
    print("The given number is negative ");
elif(num==0):
    print("The number is zero ");
else:
    print("THe number is positive ");

# nested if 

num=int(input("enter a number"));
print("tne number is ",num);
if(num<0):
    print("The given number is negative ");
elif(num>0):
    if(num<=10):
        print(" the number lies between 1- 10 ");
    elif (num>10 and num<=20):
        print(" The number lies between 10 - 20 ");
    else:
        print("The number is greater than 20 ")
else:
    print("The number is zero ");

