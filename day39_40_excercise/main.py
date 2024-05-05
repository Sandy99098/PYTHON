import random
import string

option = int(input("Enter 1 for encryption or 2 for decryption: "))
st = input("Enter the message: ")
words = st.split(" ")
if option == 1:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = ''.join(random.choices(string.ascii_lowercase, k=3))
            r2 = ''.join(random.choices(string.ascii_lowercase, k=3))

            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])  # Reverse the word
    print("Encrypted message:", " ".join(nwords))
elif option == 2:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
            pass
        else:
            nwords.append(word[::-1])  # Reverse the word
    print("Decrypted message:", " ".join(nwords))
else:
    print("Invalid option. Please enter 1 or 2.")
