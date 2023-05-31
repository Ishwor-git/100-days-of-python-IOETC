#imports
import data
import random

#constants
word_value = random.choice(data.catagory['animals']).upper()
word_value_bkp = word_value
word_index = [0]

#functions

def output_design_word(word:str,index:list):
    length = len(word)
    decoration_value = ["_" for i in range(length)]
    for i in index:
        decoration_value[i] = word[i]
    decoration_text = ''
    for i in range(length):
        decoration_text += '{} '.format(decoration_value[i])
    return decoration_text

def value_check():
    pass


def hangman_intro(level:int):
    print(data.hangman[level])
    

    print("Catagory : Animlas\n")
    print(output_design_word(word_value,word_index))
    pass

#start code here
level = 0
hangman_intro(level)
print(word_value)