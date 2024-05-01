# marks=[12,56,78,34]
# index=0
# for mark in marks:
#     print(mark)
#     if (index==2):
#         print("wow")
#     index +=1

#eg of eneumerate

marks=[12,56,78,34]
for index,mark in enumerate(marks): # first for index and 2nd for value .
    print(mark)
    if (index==2):
        print("wow")

#2
marks=[12,56,78,34]
for index,mark in enumerate(marks,start=1): # first for index and 2nd for value .
    print(mark)
    if (index==2):
        print("wow")