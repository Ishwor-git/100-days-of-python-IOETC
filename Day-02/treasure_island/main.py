"""
Story :-
    User is in an island searching a way to the Treasure Island. He has options to go left or right if user 
chooses right, Sonic the Hedgehog gets first to the island and user loses. If he goes left, he reaches a 
beach from where he sees the island and he can either swim or wait for a ship to pass by. If he swims, he 
is eaten by a shark and loses if he waits, he gets to island in a ship shortly. after getting off the ship he 
sees a previously dug site and a cave nearby. If he searches the cave he is eaten by a bear and loses if he 
digs the site, he gets all the treasure and wins the game.

"""


print("Welcome to Treasure Island. ")
print("Your mission is to find the tresure.")

print("Left or Right? ")

dir_choice = input("Type Right/Left ")
dir_choice = dir_choice.lower()

if dir_choice == "right":
    print("Sonic the Hedgehog has reached the island. You lose.")
elif dir_choice == "left":
    print("Nice, you made it to the next level.")
else:
    print("Invalid Entry!")


print("""
    Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the 
sea, pick one. """)


swim_or_not = input("Type Swim/Wait: ")
if swim_or_not == "wait":
    print("""
        Nice, you made it to the next level, you're pretty good at this!
    """)
elif swim_or_not == "swim":
    print("You're eaten by a shark. Game over!")
else:
    print("Invalid Entry!")


print("""
    Now that you've made it to Treasure Island, you can dig or search the cave. 
""")

dig_or_cave = input("Type Dig/Cave: ")

if dig_or_cave == "dig":
    print("You've found the treasure, you win!")
elif dig_or_cave == "cave":
    print("Eaten by a bear. Game over!")
else:
    print("Invalid Entry!")

