def check_values(tr_val, inp_val):                           #Function to check inputs
    if inp_val in tr_val:
        return True
    else:
        print("Invalid Entry. Terminating the game...")
        return False


print("Welcome to treasure island !\nYou have found map of the treasure island but you are confused if you should go left or right in order to reach the island.\nYou are not the only one who wants the treasure.\n\n")

ch1 = input("What do you choose (L)eft or (R)ight ?  ").upper()

if check_values(['R','L'],ch1):                                 #checking if input is available for next step

    if ch1 == "L":
        
        print("\nAfter walking for sometime you reached a beach from there you can see the Tresure island \nbut it's all way across ocean. Now you are in another dilema\n\n")
        ch2 = input("Do you want to (S)wim all across or (W)ait for a ship to pass by  ?").upper()

        if check_values(['S','W'],ch2):

            if ch2 == 'W':
                
                print('\nShip did arrived though it took its time but it got to island at last.Thought it would be late but sheems like party hasnt started yet\nNow you started searching but found nothing except just two possible palces.\n\n')
                ch3 = input("Do you want to (D)ig what looks like quite unfemelier terren or search a mysterious (C)ave  ?").upper()

                if check_values(['D','C'],ch3):

                    if ch3 == 'D':
                        print('\nAha! there is all you seek. Hidden treasure since begning of time.\nGood Job You Won')

                    else:
                        print('\nthis is the defination of unlucky. When a step close to winning but got eaten by scary Bear. Anyway Bear won.\nBetter Luck Next Time')

            else:
                print('\nWhat a poor choice!. You swam right into mouth of freaking shark.\nBetter Luck next time.')


    else:
        print("\nI told you you are not alone.\nYou choose time consuming path hence Sonic the Hedgehog took all the treasure\nYou Lost :-( \nBetter Luck Next Time")

   