"""Caesar's Cipher"""

while True:
    print("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    choice = input("Encode/Decode? ").lower()
    if choice == 'encode':
        message = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        print()
        encoded_message = ""
        for i in message:
            if i != " ":
                encoded_message = encoded_message + chr(ord(i) + 2)
            else:
                encoded_message = encoded_message + " "
        print(f"Here's the encoded result: {encoded_message}")
    
    elif choice == 'decode':
        message = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))        
        print()
        decoded_message = ""
        for i in message:
            if i != " ":
                decoded_message = decoded_message + chr(ord(i) - 2)
            else:
                decoded_message = decoded_message + " "
        print(f"Here's the decoded result: {decoded_message}")
    print()
    print("Do you want to run this program again?")
    ask_user = input("Type 'yes' or 'no': ")
    if ask_user == 'no':
        print("Goodbye!")
        break
