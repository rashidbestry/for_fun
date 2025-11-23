from random import shuffle
suits=("Hearts","Diamonds","Clubs","Spades")
ranks=("One","Two","Three","Fore","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King")
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=ranks.index(rank)+1
    def __str__(self):
        return f"{self.suit} of {self.rank}"
class Deck:
    def __init__(self):
        self.deck_cards=[]
        for suit in suits:
            for rank in ranks:
                self.deck_cards.append(Card(suit,rank))
        shuffle(self.deck_cards)
    def take_one(self):
        return self.deck_cards.pop(0)
class Player:
    def __init__(self,name):
        self.name=name
        self.cards=[]
    def shoot(self):
        shuffle(self.cards)
        return self.cards.pop()
    def gain(self,gain_cards):
        if gain_cards==list:
            self.cards.extend(gain_cards)
        else:
            self.cards.append(gain_cards)
def main_engine(PL1_Wins=0,PL2_Wins=0):
    player_one=Player("player_one")
    player_two=Player("player_two")
    deck=Deck()
    for _ in range(26):
        player_one.gain(deck.take_one())
        player_two.gain(deck.take_one())
    round=0
    while True:
        round+=1
        print(f"Round {round}")
        if len(player_one.cards)<5:
            print("Player_One has less than 5 cards!!!\nPlayer_Two Win!!!")
            PL2_Wins+=1
            break
        elif len(player_two.cards)<5:
            print("Player_Two has less than 5 cards!!!\nPlayer_One Win!!!")
            PL1_Wins+=1
            break
        else:
            temp_cards=[]
            while True:
                player_one_shoots = player_one.shoot()
                player_two_shoots = player_two.shoot()
                if player_one_shoots.value>player_two_shoots.value:
                    player_one.gain(player_one_shoots)
                    player_one.gain(player_two_shoots)
                    for x in temp_cards:
                        player_one.gain(x)
                    break
                elif player_one_shoots.value<player_two_shoots.value:
                    player_two.gain(player_one_shoots)
                    player_two.gain(player_two_shoots)
                    for x in temp_cards:
                        player_two.gain(x)
                    break
                else:
                    temp_cards.append(player_one_shoots)
                    temp_cards.append(player_two_shoots)
                    continue
    while True:
        s=input(f"Press any key to play again ({PL1_Wins}-{PL2_Wins}) : ")
        game_launcher(PL1_Wins,PL2_Wins)

def game_launcher(PL1_Wins,PL2_Wins):
    main_engine(PL1_Wins,PL2_Wins)

if __name__=="__main__":
    game_launcher(PL1_Wins=0,PL2_Wins=0)






