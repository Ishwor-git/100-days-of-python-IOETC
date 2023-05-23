# imports

import random
from string import punctuation

#functions
def make_list_str(input,option):
    if option.upper() == 'S':
        output = ''
        for i in input:
            output += i
    elif option.upper() == 'L':
        output = [i for i in input]
    else:
        raise Exception
    return output


def print_words(Words,symbols):
    random.shuffle(words)
    counter = 0
    output = ''
    for i in words:
        counter += 1
        if counter == 5:
            counter = 0
            print(output)
            output = ''
        else:
            sym = [random.sample(symbols,k=4),random.sample(symbols,k=4)]
            output += '     {}{}{}'.format(make_list_str(sym[0],'S'),i.upper(),make_list_str(sym[1],'S'))
        

def check_password(guess, passwd):
    if guess == passwd:
        print("Access Granted !")
        return True
    else:
        correct_guess = 0
        for i in guess:
            if i in passwd:
                correct_guess += 1
        print("{}/7 characters correct.".format(correct_guess))




# Program starts here

words = [
    "Amazing", "Capture", "Diamond", "Fantasy", "Journey",
    "Lantern", "Mystery", "Optimal", "Radical", "Silence",
    "Vibrate", "Warrior", "Zealous", "Balance", "Command",
    "Freedom", "Justice", "Lantern", "Monster", "Powerful",
    "Silence", "Thrive", "Victory",  "Whisper", "Courage",
    "Explore", "Harmony", "Justice",  "Lantern","Passion",
    "Secrets", "Twilight", "Venture", "Wisdom", "Creator",
    "Fantasy", "Journey", "Lantern", "Passion", "Thunder"
]
print("Decrypting password.....\n\n")
print_words(words, punctuation)
print('\nPossible passwords generated to failled to identify correct one. You must do it mannually..')
print("system safely enabled, you have 10 trials left")

passwd = random.choice(words)
trials = 10
while trials >= 0:
    trials -= 1
    usr_inp = input("Password >> ").upper()
    if check_password(usr_inp,passwd):
        break
    print("You have {} trials left".format(trials))
print("Password :: {}".format(passwd))
