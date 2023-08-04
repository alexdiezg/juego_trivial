# This file will define and handle the card class

class Card():
    def __innit__(self, question, answer, category):
        self.quesiton = question
        self.answer = answer
        self.category = category
    
    print("Soy una tarjeta")

Card("España?", "Si", "Obvio")
