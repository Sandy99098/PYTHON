#tuples in python . we cannot change the tuple
tup=(1,23,13,"red","blue")
tupl=(1,) #use comma so thatt pyhton will know that it is tuple
print(type(tup),tup)
print("len of tuple ",len(tup))
print(tup[-1])

if 23 in tup:
    print("yes it is in tuple")

else:
    print("no")

#slicing

print(tup[:2])
print(tup[0:1])
print(tup[3:5])

