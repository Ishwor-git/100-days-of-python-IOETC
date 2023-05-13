print('Hello User. Im thinking a number between 1 and hundred can you guess it ? You got 10 guesses.')
from random import randint
number = randint(1,100)
count = 10

while count > 0:
    guess  = int(input("What's your guess? "))
    if guess > number:
        print('Your guess higher\n')

    elif guess < number:
        print("Your guess is lower\n")
    
    else:
        print("Thats the one !")
        break


    if count == 1:
        print('sorry youre out of guess\n')
        break

    count -= 1
        
    print('You got {} moves\n'.format(count))

