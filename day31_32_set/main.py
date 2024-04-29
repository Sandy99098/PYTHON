#set in python ,collection of well defined objects 
s={2,3,4,2,6} #set doesnot take repeated valuess
print(type(s))
print(s)

#set doesnot maintain order
hello={}; #this is dictionary not a empty set
print(type(hello))
hello=set(); #this is  an empty set
print(type(hello))
for value in s:
    print(value)


# //day32 :' set methods
s1={1,2,3,4,1,6}
s2={172,3,4,1,34}
print("s1:",s1,"s2:",s2)
#union 
#union s1 and s2 
print("union is ",s1.union(s2))

#update
s1.update(s2) #change the value of s1 and add the values of s2 in s1
print("s1 s2 after update",s1,s2 )

#intersection
s1={1,2,9,5}
s2={1,9,34} 
print("intersectionof s1 and s2 is ",s1.intersection(s2))

#difference
print("difference of s1 and s2 is",s1.difference(s2)) #it only returns the values of the difference 
s1.difference_update(s2) #it difference the value of s1 and s2 and store it in s1 
print("difference_update  of s1 and s2 on s1 is -")
print(s1)

#intersection update
s1={1,2,34}
s1.intersection_update(s2) #i#it intercsection the value of s1 and s2 and store it in s1 
print("intersection_update  of s1 and s2 on s1 is :")
print(s1)

#is disjoint()
print("is it is disjoint(true if set doesnot contain intersection) ?? ",s1.isdisjoint(s2))

#is superset
cities={"pokhara","kathmandu"}
city={"pokhara"}

print(" is cities is super set of city??",cities.issuperset(city))
print(" is city is sub set of city??",city.issubset(cities))


# add
# add items in the set
s1={1,2,3}
s1.add(79)
print(s1)

#to remove from the set
s1.remove(3) #if 3 is not in s1 : errro will occur in program
s1.discard(3) #if 3 is not in set then error wont occur

#pop
print(s1.pop()) #pop random values from the set

#delete the set
s4={1,2,3,54,7}
del s4
print("del s4 ,the set4 is deleted")


#delete the elements of the set 
set1={1,2,32}
print(" the set 'set1' is cleared")
set1.clear()
print(set1," it means set is empty")

#to check if the items is exit in the set
set2={1,3,5,78}
if 1  in set2:
    print(" yes it is present")
else:
    print(" it is not present in the set ")
