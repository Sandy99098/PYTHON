# encryption and decryption cipher key
option=int(input("enter what you wanna do 1.encryption 2.decryption \n"))
if(option==1):
    plain_text=input("Enter the plain text that you want to encrypt \n")
    key=int("Enter the key from 1 to 25")
    
    for i in range(len(plain_text)):

     
     encrypted=plain_text[i]+key
if(option==2):
 cipher_text=input("ENter the cipher text for decryption")
