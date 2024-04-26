# list in python 
marks=[16,44,37,48,"5","sandy"]; #here 5 is string
print("marks : ",marks[0],marks[1],marks[2],marks[3]);
print(marks[-2])
print(marks[len(marks)-2])

if 50 in marks:
    print("yes")
else:
    print("no")

if "sandy" in marks:
    print("yes")
else:
    print("no")

if "5" in marks:
    print("yes")
else:
    print("no")
#slicing
print(marks[:])
print(marks[0:])
print(marks[1:6])
print(marks[1:5:3]) #slicing

# ?list comprehension
print("list comprehension")
list=[i for i in range(4)]
print(list)

# condition in list comprehension
list=[i*i for i in range(7) if i%2==0]
print(list)
