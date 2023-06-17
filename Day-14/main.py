#Imports
#import card_generator as  cg
import random

#Comstants
deck_52 = []
player_hand = []
dealer_hand = []
suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
player_total =0
dealer_total = 0

#class
class Card(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]\

#Functions
def ascii_version_of_card(cards:list, return_string=True):
    """
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == '10':  # ten is the only one who's rank is 2 char long
            rank = card.rank
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            rank = card.rank[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result

def ascii_version_of_hidden_card(cards:list):
    """
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """
    # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
    lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    # store the non-flipped over card after the one that is flipped over
    cards_except_first = ascii_version_of_card(cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    # make each line into a single list
    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    # convert the list into a single string
    return '\n'.join(lines)

def deck_generator(type:str):
    'type = suit of card'
    deck = []
    for i in range(9):
        deck.append(Card(type,str(i+2)))

    deck.append(Card(type,'Jack'))
    deck.append(Card(type,'Queen'))
    deck.append(Card(type,'King'))
    deck.append(Card(type,'Ace'))
    return deck

def get_card(card_no:int,dealer=False,player=False):
    global player_hand,dealer_hand
    if dealer:
        for i in range(card_no):
            dealer_hand.append(deck_52[0])
            deck_52.pop(0)
    elif player:
        for i in range(card_no):
            player_hand.append(deck_52[0])
            deck_52.pop(0)
    else:
        for i in range(card_no):
            if (i+1) % 2 == 0:
                dealer_hand.append(deck_52[0])
                deck_52.pop(0)
            else:
                player_hand.append(deck_52[0])
                deck_52.pop(0)
    
def get_total_value(user:list):
    total = 0
    for card in user:  
        total += card.points
    
    for card in user:
        if card.rank == 'Ace' and total > 21:
            total -= 10
    return total

def game_main():
    if player_total == 21:
        print("player won !")

    elif dealer_total >= 17:

        if dealer_total > 21 & player_total <21:
            print("player_hand Wins!")
        else:

            if dealer_total > player_total:
                print("Dealer wins")
            else:
                print("player_hand Wins!")
    else:
        while dealer_total < 17:
            get_card(1,dealer=True)
            dealer_total = get_total_value(dealer_hand)

def header():
    print("DEALER ---->")
    print(ascii_version_of_hidden_card(dealer_hand))
    print()
    print("YOU ---->")
    print(ascii_version_of_card(player_hand))
    pass

#Start Coding Here
for type in suits_name:
    deck_52 += deck_generator(type)

random.shuffle(deck_52)
get_card(4)
print('''
Stand --> No need for new card
hit --> Need one more card
''')
#loop
header()
usr_ch = input("Would you like to (S)tand or (H)it >> ").upper()

#end of code






