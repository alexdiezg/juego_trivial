# This is going to be the source code for the game

from class_tarjeta import *

Ralph = Card("Hola","Caracola","Como molas")

def userInput():
    count = 0
    ans = input("Answer: ")
    try:
        ans = ans.strip()
        #print(ans)
        #print(Ralph.answer)
        
    except:
        print("Please enter a valid answer!")

    if ans == Ralph.answer:
        print("Correct!")
        count = count + 1
        if count == 6:
            print("You win! Congratulations, you win this game!")
        else:
            pass
    else:
        print("wrong")



def readCards(f, dictName):
    fhand = open(f, "r")
    x = 1
    for line in fhand:
        aux = line.split(",")
        dictName["id{0}".format(x)] = aux
        x = x + 1
    fhand.close()
    return dictName

Science = dict()
History = dict()
Sports = dict()
Geography = dict()
Films = dict()
Culture = dict()

print(readCards("science.txt", Science))
# print(readCards("history.txt", History))
# print(readCards("sports.txt", Sports))
# print(readCards("geography.txt", Geography))
# print(readCards("films.txt", Films))
# print(readCards("culture.txt", Culture))