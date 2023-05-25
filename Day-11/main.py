#imports


# Functions

def start_stop(command):
    pass

def balance_check(command):
    pass

def game_center():
    pass

def command_center(command):
    pass

# Start code here
print('''Welcome to Cho-han. We roll two dice
and you will guess if two dice add to even(Cho) or odd(han). 
You start with $100 and can add more using commands
You can bet in percentage but use'll loose 3/4 of amount you'll win.
''')
print(''' List of commands you can use :
/q = quit game at current state.
/c = check your current balance
/n = continue to next round
/a = add certain amount to your balance
''')
      
while True:
    usr_blc = 100
    house_blc = 10000
    ch = input("command >> ")
    command_center(ch)
    

