option = int(input("Enter what you want to do: 1. Encryption 2. Decryption\n"))

if option == 1:
    plain_text = input("Enter the plain text that you want to encrypt: ")
    key = int(input("Enter the encryption key (a number between 1 and 25): "))

    encrypted_text = ""
    for char in plain_text:
        # Encrypt each character by shifting it by the key value
        if char.isalpha():  # Check if the character is a letter
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        else:
            encrypted_char = char  # Leave non-alphabetic characters unchanged
        encrypted_text += encrypted_char

    print("Encrypted text:", encrypted_text)

elif option == 2:
    cipher_text = input("Enter the cipher text for decryption: ")
    key = int(input("Enter the decryption key (a number between 1 and 25): "))

    decrypted_text = ""
    for char in cipher_text:
        # Decrypt each character by shifting it back by the key value
        if char.isalpha():  # Check if the character is a letter
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
        else:
            decrypted_char = char  # Leave non-alphabetic characters unchanged
        decrypted_text += decrypted_char

    print("Decrypted text:", decrypted_text)

else:
    print("Invalid option. Please enter 1 for encryption or 2 for decryption.")
