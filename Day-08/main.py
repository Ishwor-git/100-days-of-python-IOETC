#libraries
from random import randint as random


#functions

def bagles_logic(test,value):
    common_letters = 0
    for i in test:
        common_letters += 1
        if i in value:
            if test.index(i) == value.index(i):
                print('Fermi')
            else:
                  print("Pico")
    if common_letters == 0:
       print("Bagles")

    return None



#start
print('''This is the bagles, a simple puzzle game.
I have a 3 different digit number. You must guess the number in less than 10 guesses.
I will give following hints based on your input : -
1) "Pico" = correct digit in wrong place
2) "Fermi" correct digit in the correct place
3) “Bagels” if your guess has no correct digits

Best of luck \n''')


comp_value = str(random(100,1000))
for i in range(10):
    print("\n# Trial {}".format(i+1))
    user_guess = input("Your guess >> ")
    if user_guess == comp_value:
        print("You guessed it right !")
        break
    else:
        bagles_logic(user_guess,comp_value)

print("\nGame Over !\nComputer Value = {}".format(comp_value))