#else if elif excercise (good morining)
#using time module
import time
timestamp=time.strftime('%H:%M:%S');
print("TIME in H:M:S IS ",timestamp);
#getting hour 
Hour=time.strftime('%H')
print("hour is ",Hour);
#getting minute 
Minute=time.strftime("%M")
print("minute is ",Minute);
#get second
Second=time.strftime("%S")
print("second is ",Second);

Hour=int(Hour);
Minute=int(Minute);
Second=int(Second);
# Hour="24"
if(0< Hour <12):
    print("Good Morning Sandy");
elif(12<Hour<17):
    print("Good AfterNoon Sandy");
elif(17<=Hour<20):
    print(" good evening");
elif(24<Hour):
    print("time is invalid")
else:
    print("Good Night Sandy")
    
    # ?to print date and time

import datetime
#call the current date and time 
current_dateTime=datetime.datetime.now();#insert thevalue in current date and timme
formatted_datetime=current_dateTime.strftime('%Y-%m-%d  %H:%M:%S')
print(formatted_datetime);

   