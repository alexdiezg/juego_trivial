# This is going to be the source code for the game

from class_tarjeta import *

Ralph = Card("HOla","Caracola","Como molas")

def userInput():
    ans = input("Answer: ")
    try:
        str(ans)
        ans.strip().lower()
        #print(ans)
        if ans == Ralph.answer():
            print("Correct!")
        else:
            print("wrong")
    except:
        print("Please enter a valid answer!")
    
userInput()

