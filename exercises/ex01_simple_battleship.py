"""EX01 - Simple Battleship - A cute step toward Battleship"""

__author__ = "730711485"

Pick_a_number_player_1: int = (input("Pick a secret boat location between 1 and 4: "))
if Pick_a_number_player_1 <= "0":
    print("Error! " + Pick_a_number_player_1 + " too low!")
if Pick_a_number_player_1 <= "0":
    exit()  

if Pick_a_number_player_1 > "4":
    print("Error! " + Pick_a_number_player_1 + " too high!")
if Pick_a_number_player_1 > "4":
    exit()

"""Player two"""
Pick_a_number_player_2: int = (input("Guess a number between 1 and 4: "))
if Pick_a_number_player_2 <= "0":
    print("Error! " + Pick_a_number_player_2 + " too low!")
if Pick_a_number_player_2 <= "0":
    exit()
if Pick_a_number_player_2 > "4":
    print("Error!" + Pick_a_number_player_2 + " too high!")
if Pick_a_number_player_2 > "4":
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

"""Part_Checking User Inpurt for Match"""

boxcolor: str = ""


if Pick_a_number_player_2 == Pick_a_number_player_1:
    boxcolor=RED_BOX
else:
    boxcolor=WHITE_BOX
    
boxes:str = ""
if Pick_a_number_player_2 == "1":
    boxes = boxes + boxcolor
else:
    boxes = boxes + BLUE_BOX
if Pick_a_number_player_2 == "2":
    boxes = boxes + boxcolor
else:
    boxes = boxes + BLUE_BOX
if Pick_a_number_player_2 == "3":
    boxes = boxes + boxcolor
else:
    boxes = boxes + BLUE_BOX
if Pick_a_number_player_2 == "4":
    boxes = boxes + boxcolor
else:
    boxes = boxes + BLUE_BOX

print(boxes)
if Pick_a_number_player_1 == Pick_a_number_player_2:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.") 


