#exception handling
   #example 1 
try:
    num=int(input("Enter the number "))
    for i in range(11):
        print(f"{num}*{i}={num*i}")

except ValueError:
    print("Enter integer only!!")


#example 1 

try:
    num=int(input(" Enter the number\n"))
    for i in range(11):
        a=[1,2]
        print(a[num])
except ValueError :
   print("Enter integer values only")
except IndexError:
    print("Index error ")

print("Some lines of code")

   #example 3
try:
    n=int(input("Enter the divident number"))
    d=int(input("Enter the divisior"))
    print(f"{n}/{d}={n/d}")
    
except ZeroDivisionError:
    print(f"Zero division occur divisor != 0")
