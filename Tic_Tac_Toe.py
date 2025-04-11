def welcome(key):
    if key=="cont":
        print("You wanna play again!")
    else:
        print("\nWelcome to Tic Tac Toe: ")
def confirm_play():
    while True:
        confirm = input("Are you ready to play? Enter Yes or NO: ")
        if "N" == confirm:
            return False
        if "Y" == confirm:
            return True
        else:
            print("Please enter correct input!\n")
    while True:
        player1 = input("Do you want to be X or O : ")
        if "X" == player1.upper():
            player2 = "O"
            break
        if "O" == player1.upper():
            player2 = "X"
            break
        else:
            print("Please enter correct input!\n")
    print("\nPlayer 1 will go first.")
def start_game(key):
    if key=="cont":
        welcome("cont")
    else:
        welcome("new")
    replay = confirm_play()
    control = 1
    status = False
    liste = [[""], [""], [""], [""], [""], [""], [""], [""], [""]]
    while replay == True:
        jump = None
        def choose_position():
            if control % 2 == 0:
                OX = "X"
                print("Player1 Go on!!!")
            if control % 2 == 1:
                OX = "O"
                print("Player2 Go on!!!")
            choose = int(input("Choose your next position: (1-9)"))
            if liste[choose] == "X":
                print("Please mark empty box!!")
                choose_position()
            else:
                liste[choose - 1] = OX
                display_board()
        def display_board():
            ls = [[f"{liste[0][0]}", "|", f"{liste[1][0]}", "|", f"{liste[2][0]}"],
                  [f"{liste[3][0]}", "|", f"{liste[4][0]}", "|", f"{liste[5][0]}"],
                  [f"{liste[6][0]}", "|", f"{liste[7][0]}", "|", f"{liste[8][0]}"]]
            for x in range(len(ls)):
                print("----------------------")
                for y in range(len(ls[0])):
                    print(f"{ls[x][y]:^4}", end="")
                print()
            print("----------------------")
        if liste[0] == liste[1] == liste[2] == "X":status=True
        if liste[3] == liste[4] == liste[5] == "X":status=True
        if liste[6] == liste[7] == liste[8] == "X":status=True
        if liste[0] == liste[1] == liste[2] == "O":status=True
        if liste[3] == liste[4] == liste[5] == "O":status=True
        if liste[6] == liste[7] == liste[8] == "O":status=True
        if status:
            if control % 2 == 0:
                winer = "Player1"
            else:
                winer = "Player2"
            print(f"{winer} winner!!!!!")
            replay=False
            continue
        choose_position()
        control += 1
    start_game("cont")
start_game("new")
