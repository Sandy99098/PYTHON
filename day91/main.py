#  generators in python
def my_generator():
     for j in range(6):
         yield j
         
g=my_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# for i in range (6):
#     print(next(g))
    
    
#  generate when needed. it doesnot generate automatically . 
