""""Caesar Cipher Hacker"""

def caesar_cipher(msg: str, k):       
    decoded_message = ""
    for i in msg:
        if i != " ":
            decoded_message = decoded_message + chr(ord(i) - k)
        else:
            decoded_message = decoded_message + " "
    return decoded_message


print("Enter the encrypted Caesar cipher message to hack:")

message = input(": ")


cnt = 1
while cnt < 27:
    print(f"Key #{cnt}: {caesar_cipher(message, cnt)}")
    cnt += 1

