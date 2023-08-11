# This is going to be the source code for the game

from class_tarjeta import *

Ralph = Card("HOla","Caracola","Como molas")

count = 0

def userInput():
    ans = input("Answer: ")
    try:
        str(ans)
        ans.strip().lower()
        #print(ans)
        #print(Ralph.answer)
        
    except:
        print("Please enter a valid answer!")

    if ans == Ralph.answer():
        print("Correct!")
        count = count + 1
        if count == 6:
            print("You win! Congratulations, you win this game!")
        else:
            pass
    else:
        print("wrong")

userInput()