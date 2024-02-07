"""One Shot Battleship"""

__author__ = "730711485"

grid_size: int = "4"
secret_row: int = "3"
secret_column: int = "2"

guess_a_row: int = (input("Guess a row: "))
while (guess_a_row) > (grid_size): #if row guess is higher than grid size.
    guess_a_row_again: int = (input(f"The gride is only {grid_size} by {grid_size}. Try again: "))
    guess_a_row = guess_a_row_again

guess_a_column: int = input("Guess a column: ")
while (guess_a_column) > (grid_size): # if column guess is higher than gride size.
    guess_a_column_again: int = (input(f"The gride is only {grid_size} by {grid_size}. Try again: "))
    guess_a_column = guess_a_column_again

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Determing if the target area is red or white.
if guess_a_row == secret_row and guess_a_column == secret_column:
    boxcolor = RED_BOX
else:
    boxcolor = WHITE_BOX
row_counter: int = 1
while row_counter <= int(grid_size):
    row_emoji_string: str = ""
    column_counter: int = 1
    if guess_a_row == row_counter:
        while column_counter <= grid_size:
            if guess_a_column == column_counter:
                row_emoji_string = row_emoji_string + boxcolor
            else: row_emoji_string = row_emoji_string + BLUE_BOX
            column_counter = column_counter + 1
    else:
        while column_counter <= int(grid_size):
            row_emoji_string = row_emoji_string + BLUE_BOX
            column_counter = column_counter + 1
    print(row_emoji_string)
    row_counter = row_counter + 1




if guess_a_row == secret_row and guess_a_column == secret_column:
    print("Hit!")
elif guess_a_column == secret_column and guess_a_row != secret_row:
    print("Close1 Correct column, wrong row.")
elif guess_a_row == secret_row and guess_a_column != secret_column:
    print("Close! Correct row, wrong column")
else: print("Miss!")