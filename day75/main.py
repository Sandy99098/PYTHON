# Your Python code goes here
# excercise solution  
# os rename
# clear the clutter 

import os
files=os.listdir("clutteredFolder")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
    os.rename(f"clutterFolder/file.txt","clutterFolder/{i}.txt")
    i+=1