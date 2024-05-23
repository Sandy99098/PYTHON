#Shutil method in Python  -  high ;eve; file operations
import shutil

shutil.copy("main.py","main2.py")

shutil.copy2("main.py","main2.py")  #details wil go at the meta data

shutil.copytree("main.py","main2.py") # copy the folder 

shutil.move(",tutorial/file.file","file.file")



shutil.rmtree("main.py") # use for file directory 


import os
os.remove("helo.txt")

