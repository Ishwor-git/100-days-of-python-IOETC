import random


print("Bagels, a deductive logic game.")
print("I am thinking of a 3-digit number. Try to guess what it is.")

print("""Here are some clues:
        When I say: 
        Pico --> Digit is correct but is in the wrong position.
        Fermi --> Digit is correct and is in the right position.
        Bagels --> No digit is correct.""")

while True:
    random_num = random.randint(100, 999)
    print("""I have thought of a three-digit number.
You have 10 guesses to get it.
                                    """)
    for i in range(1, 11):
        guess = int(input(f"Guess #{i}: "))
        resp = ""
        if guess == int(random_num):
            print(f"You got it! The number was {random_num}.")
            break
        else:
            guess = str(guess)
            random_num = str(random_num)
            for j in range(3):
                if guess[j] in random_num and guess[j] == random_num[j]:
                    resp = resp + " " + "Fermi"
                elif guess[j] in random_num:
                    resp = resp + " " + "Pico"

            if resp == "":
                print("Bagels")
            else:
                print(resp)
    if i>10:
        print(f"You ran out of guesses! The number was {random_num}")
    ask_user = input("Do you want to play again? (yes/no) ").lower()
    if ask_user == 'no':
        print("Thanks for playing.")
        break

