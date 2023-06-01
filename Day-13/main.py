#imports
import data
import random

#globals
word_value = random.choice(data.catagory['animals1']).upper()
word_value_bkp = word_value
word_index = [0]
level = 0
score = 1

#functions

def output_design_word(word:str,index:list):
    length = len(word)
    decoration_value = ["_" for i in range(length)]
    decoration_text = ''
    for i in index:
        decoration_value[i] = word[i]

    for i in range(length):
        decoration_text += '{} '.format(decoration_value[i])
    return decoration_text

def value_check(usr_inp:str):
    global level, score
    if usr_inp in word_value:
        word_index.append(word_value.index(usr_inp))
        score += 1
    else:
        level += 1


def hangman_intro(level:int):
    print(data.hangman[level])
    
    print("Catagory : Animlas\n")
    print(output_design_word(word_value,word_index))
   

#start code here

while level < len(data.hangman):
    hangman_intro(level)

    if score >= len(word_value):
        print("\nYou guessed it right ! \nYou saved yourself from hanging.")
        break

    usr_inp = input("What is your guess? >> ").upper()

    if len(usr_inp) != 1:
        continue

    value_check(usr_inp)

    

print("\nGame Over\nWord : {}".format(word_value))