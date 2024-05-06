#  file handling in python 
# rb for reading binary files . like opening the img files and pdf 

# read
# f= open("myfile.txt","r") 
# text=f.read()
# print(text)
# f.close

# # write 

# f= open("myfile2.txt","w") 
# f.write("Hello i am sandy ")
# f.close


with open('myfile.txt','a') as f:
    f.write("Hey i am doing good ")