# This file will define and handle the card class

class AnsException(Exception):
    pass

class Card:
    def __init__(self, question: str, answer, category):
        self.question = question
        self.answer = answer
        self.category = category
        #print(question)

# Create a new file for the code below. That shouldn't be part of the class, it should be part either of the main code or a different class.

    def userInput(self):
        ans = input("Answer: ")
        try:
            str(ans)
            ans.strip().lower()
            print(ans)
        except:
            print("Please enter a valid answer!")
        if ans == answer:
            print("Correct!")
        else:
            print("wrong")