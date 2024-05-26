# function caching in python
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

