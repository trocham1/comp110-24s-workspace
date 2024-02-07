"""NUmber Guessing Game."""
from random import randint

SECRET: int = randint(1,100000)
correct: bool = False

while not correct: #correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number")
        # something to help us exit
        correct = True
    elif guess > SECRET:
        print("Guess is too hight!")
    elif guess < SECRET:
        print("Guess is too low!")
    else:
        print("Guess again, you maggot!")