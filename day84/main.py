# # Your Python code goes here
# #  time module in python
# import time 
# def usinghwile():
#     i=0;
#     while i< 5000:
#         i=i+1;
#         print(i)

# def usingFor():
#     for i in range (5000):
#         print (i)
# init=time.time()
# usingFor()
# print(time.time()-init,"for")
# usinghwile()

# print(time.time()-init,"while")


# #  using time sleep
# import time
# print(5)
# time.sleep(3)
# print("This is printed after 3 second")



# time.strftime()
import time 
t=time.localtime()
formatted_time = time.strftime("%Y-%m-%d, %H:%M:%S")

print(formatted_time )