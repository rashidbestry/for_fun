import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def game_launcher():
    conditions = [rock, paper, scissors]
    while True:
        win = False
        machine = random.choice(conditions)
        print("***************************")
        print("\tWhat do you choose?\n\t>> 0 for Rock <<\n\t>> 1 for Paper <<\n\t>> 2 for Scissors <<")
        my_choice = int(input(">>: "))
        if my_choice not in (0,1,2):
            print("Your input is invalid")
            continue
        print(machine, "\nComputer chose:")
        print(conditions[my_choice])
        if conditions[my_choice] == machine:
            print("No winner try again!!!")
            continue
        if my_choice == 0 and machine == scissors:
            print("You Win!!!")
            continue
        if my_choice == 0 and machine == paper:
            print("You Lose!!!")
            continue
        if my_choice == 1 and machine == rock:
            print("You Win!!!")
            continue
        if my_choice == 1 and machine == scissors:
            print("You Lose!!!")
            continue
        if my_choice == 2 and machine == rock:
            print("You Lose!!!")
            continue
        if my_choice == 2 and machine == paper:
            print("You Win!!!")
            continue

if __name__ == "__main__":
    game_launcher()
