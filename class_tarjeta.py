# This file will define and handle the card class

class Card:
    def __innit__(self, question, answer, category):
        self.quesiton = question
        self.answer = answer
        self.category = category
    def userInput():
        ans = input("Answer: ")
        try:
            str(ans)
            ans.strip().lower()
            print(ans)
        except:
            print("Please enter a valid answer!")
