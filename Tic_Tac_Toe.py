import random
p = ["BOARD", " ", " ", " ", " ", " ", " ", " ", " ", " "]
players = {}
def board_print():
    print("******",p[0],"******")
    board=[[p[1], p[2],p[3]],[p[4], p[5],p[6]],[p[7], p[8],p[9]]]
    for x in board:
        print(f"-------------------")
        offs=[2,5,7]
        for num,y in enumerate(x,1):print(end=f"|  {y}  | " if num in offs else f"  {y}   ")
        print()
    print("-------------------")
def players_fun():
    player_1 = int(input("Which one you prefer 1>X or 2>O : "))
    if player_1 == 1:
        players["player_1"] = "X"
        players["player_2"] = "O"
    else:
        players["player_1"] = "O"
        players["player_2"] = "X"
    print("\nLet's Play the game!")

def checking():
    cheks=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for x,y,z in cheks:
        if p[x]==p[y]==p[z] and p[x]!=" ":
            return True
    return False
def game_engine():
    r = random.choice(["player_1","player_2"])
    counter=9
    while counter>0:
        print(f"Player {r[-1]} your turn {players[r]}")
        board_print()
        stamp=int(input("Mark from 1 to 9: "))
        if p[stamp]=="X" or p[stamp]=="O":
            print("\nPick another socket!")
            continue
        p[stamp]=players[r]
        board_print()
        counter-=1
        if r=="player_1":r="player_2"
        else:r="player_1"
        if checking():break
        else:continue
    if checking():
        print(f"\nCongratulations Player {r[-1]} win the game!!!")
    else:
        print(f"\nNo winners!")
        start_game(state=True,cont=True)
def start_game(state,cont=False):
    global p
    if state and not cont:
        print("Welcome to Tic_Tac_Toe!!!")
        p = ["BOARD", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    if state and cont:
        print("\nLets Play again!!!")
        p = ["BOARD", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    if not state:return "\nGame is Over!!!"
    while state:
        board_print()
        players_fun()
        game_engine()
        condition=input("\nDid you wanna play again? Y or N : ")
        print("Wrong! You gonna play!!!")
        start_game(state=True,cont=True)
if __name__=="__main__":
    start_game(state=True,cont=None)