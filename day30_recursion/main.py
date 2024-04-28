#recursion in python
#factorial
def fac(a):
    if a==0 or a==1:
        return 1;
    else:
     return a*fac(a-1)
print("factorial is",fac(5))

# fibonnaci series of the number 

def fibo(n):
   if n==0:
      return 0
   if n==1:
      return 1
   else:
      return fibo(n-1)+fibo(n-2)
   
print("series is")
for i in range(7):
   print(fibo(i),"+")
