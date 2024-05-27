# function caching in python (memoization)
# used if we have limited values /eg fetching home button in the browser  
#  used when the function took long time for the executions
from functools import lru_cache
import time
lru_cache(maxsize=None)
def fc(n):
    time.sleep(4)
    return n*4

start_time=time.time()
print(start_time)
print(fc(65))
print(fc(5))
print(fc(25))

print(fc(65))
print(fc(75))
print(fc(2))
print(fc(3))
print(fc(2))
print(fc(2))
print(fc(3))
print(fc(3))
print(fc(3))

end_time=time.time()
print(end_time)

# 

def fibo(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibo(n-1, cache) + fibo(n-2, cache)
    cache[n] = result
    return result

n = int(input("Enter the number of terms you want to generate: "))

print("The generated Fibonacci series is:")
for i in range(n):
    print(fibo(i))


# 
from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter the number of terms you want to generate: "))

print("The generated Fibonacci series is:")
for i in range(n):
    print(fibo(i))
