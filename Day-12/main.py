# imports

from data import data
import random

#constants

score = 0

#functions
def compare_data():
    val1 = random.choice(data)
    val2 = random.choice(data)
    return [val1,val2]

def display(data:list):
    print("\nWho has more followers 1. {} ({}) or 2. {} ({})".format(data[0]['name'], data[0]['description'],data[1]['name'], data[1]['description']))
    usr_inp = int(input("What do you think ? (1 or 2) >> "))
    return usr_inp

#start code here
while True:
    values = compare_data()
    values_bkp = values.copy()
    usr_inp = display(values)
    print()
    for i in values:
        print("Name : {}    Followers(Million) : {}".format(i['name'],i['follower_count']))
    usr_guess_count = values[usr_inp-1]['follower_count']
    del values[usr_inp-1]
    remaining_value_count = values[0]['follower_count']

    if usr_guess_count > remaining_value_count:
        score += 1
        print("You Guessed it right !\nYour current score = {}".format(score))
    else:
        print("You Failled successfully !\nYour total score = {}".format(score))
        break