#  warlus operator
# a = False
# # print(a=True) # type eroor occured sp use walrus operators

# print(a:= True)

# list =[1,34,5,6,5,7]
# while (n:= len(list) )>0:
#     print(list.pop())
    
    
    #  walrus operator for taling customer's order 
order=list()
while(o:= input("Enter your order ") )!="quit":
    (order.append(o))

while(l:=len(order))>0: 
    print("Your orders list is")   
    print(order.pop())

