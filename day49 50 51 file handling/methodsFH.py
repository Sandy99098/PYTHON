# f = open("myfile.txt","r")
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     if not line :
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"greeting is {i} {m1}")
#     print(f"greeting is {i} {m2}")
#     print(f"greeting is {i} {m3}")
#     print(line)
#     if not line:
#         print(line,type(line))


# writelines method in file handling 
f = open("myfile2.txt",'w')
lines =['line1\n','line2\n','line3\n']
f.writelines(lines) #use to write each elements of line in files
f.close()
