"""Practicing Counters"""

num_string: str ="303"

# How many odd number is in the string
num_of_odds: int = 0
if int(num_string[0]) % 2 == 1:
    num_of_odds = num_of_odds + 1

if int(num_string[1]) % 2 == 1:
    num_of_odds = num_of_odds + 1

if int(num_string[2]) % 2 == 1:
    num_of_odds = num_of_odds + 1

print(num_of_odds)