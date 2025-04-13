# CARD CLASS
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
dic = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11,
       "Queen": 12, "King": 13, "Ace": 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = dic[rank]
    def __str__(self):
        return self.suit + "of" self.rank

card_temp = Card("Diamonsd","Seven")

card_temp.suit

