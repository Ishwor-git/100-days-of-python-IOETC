#globals

usr_blc = [100,0,0,0]       #[Starting amount, profit, loss, additational amount]
house_blc = [100000, 0, 0]  #[Starting amount, profit, loss]
tot_house = 0
tot_usr = 0


#imports
import random

# Functions

def balance_account(command:str, bet=0):
    if command == 'add':
        amt = int(input("Enter amount you want to add in USD >>"))
        usr_blc[3] += amt
        print("Successfully added ${}.".format(amt))

    elif command == 'cur':
        print("Your current blc is {}".format(tot_usr))
    
    elif command == 'win':
        usr_blc[1] += bet 
        house_blc[2] += bet
        print("You win !")
    
    elif command == 'lose':
        usr_blc[2] += (4/5) * bet
        house_blc[1] += (4/5) * bet
        print("You lost !")
    pass

def game_center():

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    sum = dice1 + dice2
    value = ''

    if sum % 2 == 0:
        value = 'cho'
    else:
        value = 'han'
    
    usr_bet = float(input("What is your bet ? >> "))
    usr_inp = input("What is your guess (cho/han) ? >> ")
    print("Dice 1 : {}  Dice 2 : {}".format(dice1,dice2))
    if usr_inp == value:
        balance_account('win', bet=usr_bet)
    else:
        balance_account('lose',bet=usr_bet)
    pass

def command_center(command:str):
    if command == '/a':
        balance_account('add')

    elif command == '/c':
        balance_account('cur')
    
    elif command == '/n':
        game_center()
    
    else:
        print("Invalid Command\n")

    

# Start code here

print('''Welcome to Cho-han. We roll two dice
and you will guess if two dice add to even(Cho) or odd(han). 
You start with $100 and can add more using commands
You can bet in percentage but use'll loose 4/5 of amount you'll win.
''')
print(''' List of commands you can use :
/q = quit game at current state.
/c = check your current balance
/n = continue to next round
/a = add certain amount to your balance
''')

while True:
    tot_usr = usr_blc[0] + usr_blc[1] + usr_blc[3] - usr_blc[2]
    tot_house = house_blc[0] + house_blc[1] - house_blc[2]
    ch = input("\ncommand >> ").lower()
    if ch == '/q':
        print("\n\nYour Stat !!!\nStarting amount : {}\nTotal profit : {}\nTotal Loss : {}\nAddition amount you spent : {}\nTotal current sum : {}".format(usr_blc[0],usr_blc[1],usr_blc[2],usr_blc[3],tot_usr))
        print("\nHouse stat !!!\nTotal profit : {}\nTotal Loss : {}\nTotal current sum : {}".format(house_blc[1],house_blc[2],tot_house - house_blc[0]))
        break
    else:
      command_center(ch)
    

