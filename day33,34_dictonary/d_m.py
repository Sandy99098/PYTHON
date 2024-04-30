#   dictionary methods in python 
eID1={
    100:12,
    122:23,
    125:54
}
eID2={
100:67,
90:94
}

eID1.update(eID2)
print(eID1)
for key in eID1:
    print(key,":",eID1[key])
    # print(f"The value corresponding to the key {key} is {eID1[key]}")

#clear the dictionary

eID2.clear()
print("This is empty dictionay ",eID2)

eID1.popitem() #pop the last item
print(eID1) 
# del eID1[100] #delete the item of key 100
# del eID1 #delete entire dictionary

