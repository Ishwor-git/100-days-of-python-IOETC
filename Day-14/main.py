import card_generator as  cg
import random

def deck_generator(type:str):
    deck = []
    for i in range(9):
        deck.append(cg.Card(type,str(i+2)))

    deck.append(cg.Card(type,'Ace'))
    deck.append(cg.Card(type,'Jack'))
    deck.append(cg.Card(type,'Queen'))
    deck.append(cg.Card(type,'King'))
    return deck

suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
deck_52 = []
for type in suits_name:
    deck_52 += deck_generator(type)

print(cg.ascii_version_of_card(random.choice(deck_52)))