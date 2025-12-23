import random  

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to the most famous hand game \n You should choose one option")
PlayerInput = int(input("what do you choose? Type '0' for ROCK , '1' for PAPER OR '2' SCISSORS \n"))
Computer_chose_val = random.randint(0, 2)

game_list = [Rock, Paper, Scissors]

if PlayerInput >=0 and PlayerInput <= 2:
    print("You chose:")
    print(game_list[PlayerInput])
    print("\nComputer chose:")
    print(game_list[Computer_chose_val])

    if PlayerInput == Computer_chose_val:
        print("\nDraw, Try again")
    elif PlayerInput == 0 and Computer_chose_val == 1:
        print("\nYou lose, Paper covers Rock. Try again")
    elif PlayerInput == 0 and Computer_chose_val == 2:
        print("\nYou WIN! Rock crushes Scissors. You are the best!")
    elif PlayerInput == 1 and Computer_chose_val == 0:
        print("\nYou WIN! Paper covers Rock. You are the best!")
    elif PlayerInput == 1 and Computer_chose_val == 2:
        print("\nYou lose, Scissors cut Paper. Try again")
    elif PlayerInput == 2 and Computer_chose_val == 0:
        print("\nYou lose, Rock crushes Scissors. Try again")
    elif PlayerInput == 2 and Computer_chose_val == 1:
        print("\nYou WIN! Scissors cut Paper. You are the best!")
else:
    print("You typed and invalid number, you lose, try again")