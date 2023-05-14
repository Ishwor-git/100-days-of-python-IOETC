"""
    ROCK, PAPER SCISSORS GAME
"""
import random

print("""Press:
        'S' for Scissors
        'P' for Paper
        'R' for Rock""")

options = ['S', 'P', 'R']
defaults = {'S': 'Scissors', 'P': 'Paper', 'R': 'Rock'}

user_choice = input("Enter your choice: (S/P/R) ").upper()
computer_choice = random.choice(options)

if user_choice == 'S' and computer_choice == 'P':
    print(f"You chose: {defaults[user_choice]}")
    print(f"The computer chose: {defaults[computer_choice]}")
    print(f"You win, {defaults[user_choice]} beats {defaults[computer_choice]}.")

elif user_choice == 'P' and computer_choice == 'S':
    print(f"You chose: {defaults[user_choice]}")
    print(f"The computer chose: {defaults[computer_choice]}")
    print(f"You lose, {defaults[computer_choice]} beats {defaults[user_choice]}.")

elif user_choice == 'S' and computer_choice == 'R':
    print(f"You chose: {defaults[user_choice]}")
    print(f"The computer chose: {defaults[computer_choice]}")
    print(f"You lose, {defaults[computer_choice]} beats {defaults[user_choice]}.")

elif user_choice == 'R' and computer_choice == 'S':
    print(f"You chose: {defaults[user_choice]}")
    print(f"The computer chose: {defaults[computer_choice]}")
    print(f"You win, {defaults[user_choice]} beats {defaults[computer_choice]}.")

elif user_choice == 'P' and computer_choice == 'R':
    print(f"You chose: {defaults[user_choice]}")
    print(f"The computer chose: {defaults[computer_choice]}")
    print(f"You win, {defaults[user_choice]} beats {defaults[computer_choice]}.")

elif user_choice == 'R' and computer_choice == 'P':
    print(f"You chose: {defaults[user_choice]}")
    print(f"The computer chose: {defaults[computer_choice]}")
    print(f"You lose, {defaults[computer_choice]} beats {defaults[user_choice]}.") 

elif user_choice == 'S' and computer_choice == 'S' or user_choice == 'P' and computer_choice == 'P' or user_choice == 'R' and computer_choice == 'R':
    print(f"You chose: {defaults[user_choice]}")
    print(f"The computer chose: {defaults[computer_choice]}")
    print("It's a draw.")




