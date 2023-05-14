# Guess the number game

import random

while True:
    print("I'm thinking of a number between 1 and 100, try to guess it")
    print()
    print("Choose a difficulty: Type 'easy' or 'hard': ")
    difficulty = input("Easy/Hard?  ").lower()

    if difficulty == 'easy':
        c = 10

    elif difficulty == 'hard':
        c = 5
    
    print(f"Difficulty level set to '{difficulty}'. You have {c} tries to guess the number.")
    print()

    ran_gen_num = random.randint(1, 100)

    while c > 0:
        print(f"You have {c} guesses left for the number that I'm thinking of.")
        print()
        guess = int(input("Take your guess: "))
        if guess < ran_gen_num:
            print("Too low.")
            print()
            c -= 1
        elif guess > ran_gen_num:
            print("Too high.")
            print()
            c -= 1
        elif guess == ran_gen_num:
            print(f"Correct! The answer was {ran_gen_num}. Thanks for completing that!")
            print()
            break
        
        if c == 0:
            print(f"You exceeded the number of guesses limit. You lose! The correct number was {ran_gen_num}")
            print()

    ask_user = input("Do you want to play again? Type 'y' if yes and 'n' to quit: ").lower()
    if ask_user == 'n':
        break

