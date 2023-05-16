characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inc_choice = input("Do you want to (e)ncode or (d)ecode ? ").lower()
text = input("Enter your message > ").upper()
key = int(input("Enter the key value > "))
if key > 26: key -= 26
processed_text = ''

if inc_choice == 'e':

    for i in text:

        if i in characters:
            ind = characters.index(i)
            ind += key           
            processed_text += characters[ind]

        else:
            processed_text += i

elif inc_choice == 'd':

    for i in text:
        
        if i in characters:
            ind = characters.index(i)
            ind -= key
            processed_text += characters[ind]
        
        else:
            processed_text += i

else:
    print("Invalid Entry !")
    raise ValueError

print("Your processed message --> {}".format(processed_text))