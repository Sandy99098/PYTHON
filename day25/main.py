#methods in tuple

tup=(1,2,46,"hello world")

#count
print(tup.count(2))

temp=list(tup)
temp.append(33)
print(temp)

temp.pop(2) #pop or delete the index of 2
print(temp)
tup3=tuple(temp) #conversion into tuple so that we can change tupe by converting into list ans then change into tuple

#concatenation 
#since we cannot change the tuple so  we should create new variable to conccatenate the tuple

tup1=(1,2,32)
tup3=(1,1,3,3,2,65,1,2,"hellsdf")
conc=tup1+tup3
print(conc)

#index . print the first occurence of element in tuple
res=tup3.index(3)
print("occurence of 3 in tuple  is ",res)
res=tup3.index(1,1,7) #.index(index,indexstart range , end range)
print("occurence of 1 in tuple  is ",res ,"index")




