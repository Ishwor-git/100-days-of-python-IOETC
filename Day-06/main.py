
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input("Enter your encrypted message > ").upper()
processed_text = ''

for key in range(27):
    processed_text = ''
    for i in text:

            if i in characters:
                ind = characters.index(i)
                ind -= key
                processed_text += characters[ind]
            
            else:
                processed_text += i

    print("key #{} --> {}".format(key,processed_text))