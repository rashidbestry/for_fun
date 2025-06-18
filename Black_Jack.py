from random import shuffle
from time import sleep


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
          'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in values.keys():
                self.deck.append(Card(suit,rank))
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.life=True
        self.hand=True

    def add_card(self, card):
        if card.rank != "Ace":
            self.cards.append(card)
            self.value+=card.value
        else:
            self.adjust_for_ace()
            self.cards.append(card)

    def adjust_for_ace(self):
        self.aces+=1
        if self.value<11:self.value+=11
        else:self.value+=1

class Chips:

    def __init__(self):
        self.bet = 0
        self.total = 0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet


def take_bet(player_chip, dealer_chip):
    player_chip.bet, dealer_chip.bet = 0, 0
    print(f"\n\nPlayer Total:{player_chip.total}  |  Dealer Total:{dealer_chip.total}")
    bet = int(input("\nPlease insert bet you want!: "))
    if 0 < bet <= player_chip.total and 0 < bet <= dealer_chip.total:
        player_chip.bet = dealer_chip.bet = bet
        player_chip.total-=bet
        dealer_chip.total-=bet
        sleep(1)
        print("\nBet accepted!\n")
        sleep(1)
        print("Game started!")
        sleep(1)
        return True
    else:
        print("\nPlease wait checking balances!")
        for x in range(10): sleep(0.3), print(">>", end="")
        if player_chip.total<50:
            print("\n\n\t\tPlayer balance less than 50 $\n\n\t\tDealer Wins the Game!!!\n")
            return False
        elif dealer_chip.total<50:
            print("\n\n\t\tDealer balance less than 50 $\n\n\t\tPlayer Wins the Game!!!\n")
            return False

def hit_or_stand(player_hand,dealer_hand,deck):
    answer = input("\tPlayer! Hit or Stand ?")
    if answer in ("h", "H"):
        player_hand.add_card(deck.deal())
    else:
        if dealer_hand.value<17:
            dealer_hand.add_card(deck.deal())
            if dealer_hand.value>17:
                dealer_hand.hand = False
        else:
            dealer_hand.hand=False

def show_some(player_hand,player_chip,dealer_hand,dealer_chip):
    print("\n--------------Dealer holds-----------------")
    dealer_value=0
    for card in dealer_hand.cards[1::]:
        print(f"\t{card}")
        dealer_value+=card.value
    print(f"\tXXXXXXXXXXXX")
    print(f"\n\tScore: {dealer_value}",f"\tBet:{dealer_chip.bet} ; Total {dealer_chip.total}")
    print("-------------------------------------------")
    print("--------------Player holds-----------------")
    for card in player_hand.cards:
        print(f"\t{card}")
    print(f"\n\tScore: {player_hand.value}",f"\tBet:{player_chip.bet} ; Total {player_chip.total}")
    print("-------------------------------------------")

def show_all(player_hand,player_chip,dealer_hand,dealer_chip):
    print("\n--------------Dealer holds-----------------")
    for card in dealer_hand.cards:
        print(f"\t{card}")
    print(f"\n\tScore: {dealer_hand.value}", f"\tBet:{dealer_chip.bet} ; Total {dealer_chip.total}")
    print("-------------------------------------------")
    print("--------------Player holds-----------------")
    for card in player_hand.cards:
        print(f"\t{card}")
    print(f"\n\tScore: {player_hand.value}", f"\tBet:{player_chip.bet} ; Total {player_chip.total}")
    print("-------------------------------------------")

def win_chek(player_hand,player_chip,dealer_hand,dealer_chip):
    if player_hand.value>21:
        dealer_chip.win_bet()
        dealer_chip.win_bet()
        for x in range(8):
            for y in range(3):
                print("Dealer Wins! ",end="")
            print()
            sleep(0.1)
            if x ==3:
                show_all(player_hand, player_chip, dealer_hand, dealer_chip)
                sleep(1)

        player_hand.life=False
    elif dealer_hand.value>21:
        player_chip.win_bet()
        player_chip.win_bet()
        for x in range(8):
            for y in range(3):
                print("Player Wins! ",end="")
            print()
            sleep(0.1)
            if x ==3:
                show_all(player_hand, player_chip, dealer_hand, dealer_chip)
                sleep(1)
        dealer_hand.life=False
    elif player_hand.value<=21 and player_hand.value>dealer_hand.value and dealer_hand.hand==False:
       player_chip.win_bet()
       player_chip.win_bet()
       for x in range(8):
           for y in range(3):
               print("Player Wins! ", end="")
           print()
           sleep(0.1)
           if x == 3:
               show_all(player_hand, player_chip, dealer_hand, dealer_chip)
               sleep(1)
       dealer_hand.life = False
    elif dealer_hand.value <= 21 and dealer_hand.value > player_hand.value and dealer_hand.hand==False:
       dealer_chip.win_bet()
       dealer_chip.win_bet()
       for x in range(8):
           for y in range(3):
               print("Dealer Wins! ", end="")
           print()
           sleep(0.1)
           if x == 3:
               show_all(player_hand, player_chip, dealer_hand, dealer_chip)
               sleep(1)
       player_hand.life = False
    elif player_hand.value==21 and player_hand.value>16:
        if len(player_hand.cards):
            print("\n\t\t$$$ Blackjack $$$\n")
            sleep(2)
        player_chip.win_bet()
        player_chip.win_bet()
        for x in range(8):
            for y in range(3):
                print("Player Wins! ", end="")
            print()
            sleep(0.1)
            if x == 3:
                show_all(player_hand, player_chip, dealer_hand, dealer_chip)
                sleep(1)
        dealer_hand.life = False
    elif dealer_hand.value==21:
        if len(dealer_hand.cards):
            print("\n\t\t$$$ Blackjack $$$\n")
            sleep(2)
        dealer_chip.win_bet()
        dealer_chip.win_bet()
        for x in range(8):
            for y in range(3):
                print("Dealer Wins! ", end="")
            print()
            sleep(0.1)
            if x == 3:
                show_all(player_hand, player_chip, dealer_hand, dealer_chip)
                sleep(1)
        player_hand.life = False
    elif player_hand.value==dealer_hand.value and dealer_hand.hand==False:
       player_chip.win_bet()
       dealer_hand.win_bet()
       for x in range(8):
           for y in range(3):
               print("Push! ", end="")
           print()
           sleep(0.1)
       dealer_hand.life = False

def game_engine(*args):
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    player_chip = Chips()
    dealer_chip = Chips()
    player_chip.total=dealer_chip.total=args[0]
    first_while=True
    while first_while:
        player_hand.cards.clear()
        dealer_hand.cards.clear()
        player_hand.life,dealer_hand.life = True,True
        player_hand.hand, dealer_hand.hand = True, True
        player_hand.value,dealer_hand.value = 0,0
        player_chip.bet,dealer_chip.bet=0,0
        if len(deck.deck)<10:
            deck=Deck()
        first_while = take_bet(player_chip, dealer_chip)
        if not first_while:
            continue
        for _ in range(2):
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

        show_some(player_hand, player_chip, dealer_hand, dealer_chip)
        win_chek(player_hand, player_chip, dealer_hand, dealer_chip)
        while player_hand.life==True and dealer_hand.life==True:
            hit_or_stand(player_hand,dealer_hand,deck)
            print("\n")
            print("Cheking ->")
            for x in range(15):
                sleep(0.2), print(">", end="")
            print("\n")
            show_some(player_hand, player_chip, dealer_hand, dealer_chip)
            win_chek(player_hand, player_chip, dealer_hand, dealer_chip)
    ask=input("\nDo you want to play again! (Y or N): ")
    if ask in ("Y","y"):
        game_launcher()
    else:
        "see ya bro !!!"

def game_launcher():
    print("\n--== Welcome to Blackjack GAME! (Rashid edition) ==--")
    balance=int(input("Please enter your balance: "))
    print("\n\tGreat! Now lets start to play!!!\n")
    print("Loading game ->")
    for x in range(15):sleep(0.2),print(">",end="")
    print("\nShuffling cards ->")
    for x in range(10):sleep(0.2),print(">", end="")
    print("\nDistribute Cards ->")
    for x in range(5):sleep(0.2),print(">", end="")
    game_engine(balance)

if __name__=="__main__":
    game_launcher()

