"""Ex03 Battleship."""

__author__ = "730711485"

import random
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(size_grid: int, row_or_column: str) -> int:
    """Provide a correct argument."""
    assert row_or_column == "row" or row_or_column == "column"
    guess_a_row: int = int(input(f"Guess a {row_or_column}: "))
    while (guess_a_row) > size_grid or (guess_a_row) < 1:
        guess_a_row = int(input(f"The grid is only {size_grid} by {size_grid}. Try again: "))
    return guess_a_row


def print_grid(size_of_gride: int, row_guess: int, column_guess: int, if_user_guess_was_correct: bool) -> None:
    """Printing_the_grid."""
    boxcolor = ""
    if if_user_guess_was_correct:
        boxcolor = RED_BOX
    else:
        boxcolor = WHITE_BOX
    
    row_counter: int = 1
    while row_counter <= int(size_of_gride):
        row_emoji_string: str = ""
        column_counter: int = 1
        if row_guess == row_counter:
            while column_counter <= size_of_gride:
                if column_guess == column_counter:
                    row_emoji_string = row_emoji_string + boxcolor
                else: 
                    row_emoji_string = row_emoji_string + BLUE_BOX
                column_counter = column_counter + 1
        else:
            while column_counter <= int(size_of_gride):
                row_emoji_string = row_emoji_string + BLUE_BOX
                column_counter = column_counter + 1
        print(row_emoji_string)
        row_counter = row_counter + 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Guessing if the input is correct."""
    return secret_row == row_guess and secret_column == column_guess


def main(grid_size: int, secert_row: int, secret_column: int) -> None:
    """The whole thing."""
    user_turns_left = 0
    out = False
    while not out:
        user_turns_left += 1
        print(f"=== Turn {user_turns_left}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        print_grid(grid_size, row_guess, column_guess, correct_guess(secert_row, secret_column, row_guess, column_guess))
        out = correct_guess(secert_row, secret_column, row_guess, column_guess) or user_turns_left == 5
    if user_turns_left < 5:
        print("Hit!")
        print(f"You won in {user_turns_left}/5 turns!")
    else:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))