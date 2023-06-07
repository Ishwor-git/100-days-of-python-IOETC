#Imports
import card_generator as  cg
import random

#Comstants
deck_52 = []
player_hand = []
dealer_hand = []
suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']

#Functions

def deck_generator(type:str):
    'type = suit of card'
    deck = []
    for i in range(9):
        deck.append(cg.Card(type,str(i+2)))

    deck.append(cg.Card(type,'Jack'))
    deck.append(cg.Card(type,'Queen'))
    deck.append(cg.Card(type,'King'))
    deck.append(cg.Card(type,'Ace'))
    return deck

#Start Coding Here
for type in suits_name:
    deck_52 += deck_generator(type)
