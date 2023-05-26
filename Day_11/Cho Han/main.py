import random


print("""Cho-Han 
In this traditional Japanese dice game, two dice are rolled in a bamboo 
cup by the dealer sitting on the floor. The player must guess if the 
dice total to an even (cho) or odd (han) number. 
\n""")


print("""The dealer swirls the cup and you hear the rattle of dice. 
The dealer slams the cup on the floor, still covering the 
dice and asks for your bet. 
""")

def cho_or_han(ch, die_1, die_2, b):
    print("The dealer lifts the cup to reveal: \nGO - GO")
    sum = 0
    a = int(random.choice(die_1))
    m = int(random.choice(die_2))
    sum = a + m
    if sum % 2 == 0:
        comp = "even"
    else:
        comp = "odd"
    if comp == ch:
        return f"{a} - {m}\n You won! You take {b*2}\n The house collects {b/10} fee."
    else:
        return f"{a} - {m}\n You lose!"
    


while True:

    amount = 5000
    print(f"You have {amount} mon. How much do you bet?")
    bet = int(input("Enter the bet amount: \n"))

    if bet <= amount:
        cho_han = input("CHO(Even) or HAN(Odd)? ").lower()
        d1 = [1, 2, 3, 4, 5, 6]
        d2 = [1, 2, 3, 4, 5, 6]

        print(cho_or_han(cho_han, d1, d2, bet))
        
        round = input("Another round? (y/n) ").lower()
        if round == 'n':
            break
    else: 
        print("Insuffienct money.")