def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
n=int(input("Enter the number of series you want to generate \n "))
print(f" the generated series is :" )
for i in range(n):
    print(fibo(i) , end=" ")


