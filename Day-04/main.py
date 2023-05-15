import random

global usr,comp
usr = 0
comp = 0

def print_win(val):
    global usr, comp
    if val == 0:
        usr += 1
        print('You Won !')
    else:
        comp += 1
        print('Computer Won !')
    return None

rounds = int(input('How many rounds do you wanna play ? '))


print('!!!!! Scissors Paper Rock !!!!!')
for i in range(rounds):

    choices = ['S','P','R']
    print('\nRound {}'.format(i+1))
    print("What is your choice ?")
    usr_choice = input("(s)cissors / (P)aper / (R)ock ? ").upper()

    comp_choice = random.choice(choices)

    print("You : {}\nComputer : {}".format(usr_choice, comp_choice))

    if usr_choice in choices:

        if usr_choice != comp_choice:
            
            if usr_choice == 'S' and comp_choice == 'P':
                print_win(0)
            
            elif usr_choice == 'S' and comp_choice == 'R':
                print_win(1)
            
            elif usr_choice == 'P' and comp_choice == 'S':
                print_win(1)

            elif usr_choice == 'P' and comp_choice == 'R':
                print_win(0)

            elif usr_choice == 'R' and comp_choice =='S':
                print_win(0)
            
            else:
                print_win(1)

        else:
            print("Game is draw !!!")

    else:
        print('{} is not available options in this game.\nPlease try again.\nterminating the game !!!')
        break

print("Game Over !\n\nScore ::\nYou:{}     Computer{}".format(usr, comp))