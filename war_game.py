# CARD CLASS -----------------------------------------------------------------------------------------------------------

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11,
          "Queen": 12, "King": 13, "Ace": 14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# DECK CLASS -----------------------------------------------------------------------------------------------------------

import random

class Deck:
    def __init__(self):
        self.all_cards = []
        for x in suits:
            for y in values.keys():
                self.all_cards.append(Card(x, y))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# PLAYER CLASS ---------------------------------------------------------------------------------------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"