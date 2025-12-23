print('''
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
.            _.,.__       .                                   .
.           ((o\\o\))     .                                   .
.     .-.    `  \\``      .    A tropical island              .
.  __(   )___.o"^^".,___  .                                   .
.     ===    ~~~~~~~~     .                                   .
.      ==             ldb .                                   .
.       =                 .                                   .
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

''')
print("Welcome to the Treasure Island \n \nYour mission is to find the treasure!\n")
ds_1 = input('You are at a crossroad, whare do you want to go "Left" or "right?" \n').lower()
if ds_1 == "left":
    ds_2 = input('You have come to a lake. You want to "Swim" or "wait"? \n').lower()
    if ds_2 == "wait":
        ds_3 = input("You arrive at 3 doores. Which door you will chose? Red, Blue or Yellow. \n").lower()
    if ds_3 == "yellow":
        print("You found the treasure. You win!\n")
    elif ds_3 == "red":
        print("You fall in a endless hole, Game over\n")
    elif ds_3== "blue":
        print("You enter a room of beast. Game over\n")
else: 
     print("Game over\n")