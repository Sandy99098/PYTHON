# string slicing and operation on strings
fruit="apple";
names="ram,sandy "
print(names[0:3]); #including 0 index but not 3 i.e last index
print(names[0:1]);
print(names[:3]);
print(names[:]);
print(fruit[0:-3]); # print(fruit[0:len(fruit)-3])= length is 5 and 5-3 is 2 so it slice upto 2 character
print(fruit[0:len(fruit)-3])
print("apple length is ",len(fruit));
print(fruit[-3:-1]) # 5-3 =2 .counting starts from 2 and ends at( 5-1=4)

aplhabets="abcde"
for i in aplhabets:
    print(i) ;

nm="shyam";
print(nm[-4:-2]) 
# len of shyam is 5, so 5-4 is 1, so starts from 1^th index and 
# ends at 5-2 is 3  but mot up to 3th index so ends at 2th index ;

