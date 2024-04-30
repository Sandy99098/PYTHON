try:
    l=[1,2,3,4]
    i=int(input("Enter the index that you wanna get :"))
    print(l[i])
except ValueError:
    print("enter integer only")
except IndexError:
 print("Index error occured")
finally: # run eventhough error occured
    print("I am always executed")

