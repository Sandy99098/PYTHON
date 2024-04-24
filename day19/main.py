# break and continue
#
# ?break
for i in range(0,11):
  print("5*",i,"=",5*i)
  if(i==5):
    break
print("loop has been end ")
 

# ? continue 
for i in range(0,11):
 if(i==5):
  print("skip the iteration 5") 
  continue #continue doesnot execute the specific condion and continue to execute 
 print("5*",i,"=",5*i)
 if(i==8):
    print("skip the iteration 8 ")
    continue
 print("5*",i,"=",5*i)
 
 #example of continue
 for i in range (6):
   if (i==4):
     print("skip the iteration 4");
     continue
   print("this is ",i)

#example
i = 1
while i <= 10:
  print("hello",i)
  i += 1 ;
  if(i==6):
    print("this is 6 and has been broken")
    break
    

#example of continue :
i=1;
while(i<=8):
  if i==6 :
    print("this is iteration 6 and will continue from it ")
    i=i+1
    continue
  print("2 *",i,"=",2*i)
  i=i+1
