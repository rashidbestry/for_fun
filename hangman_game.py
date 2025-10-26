one_six= ''' \t\t+---+
\t\t      |
\t\t      |
\t\t      |
\t\t      |
\t\t      |
\t\t========= '''
two_six= ''' \t\t+---+
\t\t  |   |
\t\t      |
\t\t      |
\t\t      |
\t\t      |
\t\t========= '''
three_six= ''' \t\t+---+
\t\t  |   |
\t\t  0   |
\t\t      |
\t\t      |
\t\t      |
\t\t========= '''
four_six= ''' \t\t+---+
\t\t  |   |
\t\t  0   |
\t\t /|\  |
\t\t      |
\t\t      |
\t\t========= '''
five_six= ''' \t\t+---+
\t\t  |   |
\t\t  0   |
\t\t /|\  |
\t\t /    |
\t\t      |
\t\t========= '''
six_six= ''' \t\t+---+
\t\t  |   |
\t\t  O   |
\t\t /|\  |
\t\t / \  |
\t\t      |
\t\t========= '''

def game_launcher():
    word="rashid"
    print("\n\t**************************")
    print("\tWelcome to Hangman game!!!")
    guess=["_"]*len(word)
    live=[one_six,two_six,three_six,four_six,five_six,six_six]
    stage=0
    print("\t\t<< Game starts >>\n")
    while True:
        if stage==5:
            print("\n\n\t\t## YOU LOSE A LIFE ##!\n")
            print(live[5])
            break
        penalty=True
        print(f"\t\t<< {5-stage} of 5 LIVES >>\n")
        print(live[stage])
        print("Word to guess: ","".join(guess))
        letter = input("Guess a letter: ")
        stage+=1
        if letter in word:
            for num,char in enumerate(word):
                if char==letter:
                    guess[num]=letter
                    penalty=False
                    stage-=1
        else:
            print("\n\t\tThe letter not in the word! minus a LIVE ")
        if "_" not in guess:
            print(f"You are guess the word '{word}' CONGRATULATIONS!!!")
            break
    game_launcher()

if __name__ == "__main__":
    game_launcher()
