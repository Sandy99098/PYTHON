l=[100,2,30,4,5];
print (l);
l.append(10)
print (l);
l.sort(); #sorting in ascending order
print (l);

print("REVERSE IN LIST")
l.sort(reverse=True) #sorting in descending order
print (l);
l.reverse(); #reverse the list
print (l);

l=[1,2,2,0,4,5];
print(l.index(5)) # returns the index of first occurence of he elements
print(l.count(2)) #return how many times the element of the list is repeated


print("COPY IN LIST")

m=l.copy() # copy the content of l in m but doesnot affect the list of "l"
m[0]=12 
print(m)

print("INSERT IN LIST")
l.insert(1,9000) #insert 9000 in 1 index
print(l);

#extending in list
colour=["red","green","white"];
colour1=["purple","indegeo"]
colour.extend(colour)
print(colour)
#concatenation in list
colour=["red","green","white"];
print("concatenate of list is :")
c= colour+colour1
print(c)
