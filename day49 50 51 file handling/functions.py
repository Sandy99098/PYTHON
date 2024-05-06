#  functions in the  file handling in python 
with open('myfile2.txt','r') as f:
    print( type(f))
    #  move to the 10th byte in the file 
    f.seek(10) # used to read after the 10th character
    # read the next 5 bytes 
    print(f.tell()) #10th position
    data=f.read(5)  
print( data)

# truncate(value)
print("using truncate :" )
with open('myfile.txt','w') as f:
    f.write("Hello world ")
    f.truncate(6) #by using this we can only print the value upto 5 digits
with open('myfile.txt','r') as f:
    print(f.read())