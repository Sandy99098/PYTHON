#  cutom error 
# a=int(input("Enter the number between 5 and 10:44"))
# if (a>10 or a<5):
#     raise ValueError("Enter number between 5 and 10 only")


# age=int(input("Enter your age \n"))
# if(age>90 or age <18 ):
#      raise ValueError("Your age must be between 18 and 90")


class CustomError(Exception):

     pass

try:
     age=int(input("Enter your age \n"))
     if(age>90 or age <18 ):
          print(age)
     if (age=="quit"):
          raise CustomError("User quit")
           

except CustomError as e:
     print("custom error :",e)
except ValueError:
    print("Enter the valid age ")



    
     
# example 
class CustomError(Exception):
    pass  # No need for any conditions in the class definition

try:
    age = input("Enter your age ('quit' to exit)\n")
    if age == "quit":
        raise CustomError("User quit")  # Raise the custom exception if user input is 'quit'
    
    age = int(age)  # Convert the user input to an integer
    
    if age > 90 or age < 18:
        raise CustomError("Invalid age")  # Raise the custom exception for invalid age
    
except CustomError as e:
    print("Custom Error:", e)  # Print the error message associated with the raised custom exception
except ValueError:
    print("Invalid input: Please enter a valid age")
