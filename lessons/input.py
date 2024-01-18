"""pratice with varibales and input function"""

first_name: str = ("What is your name")
fav_number_str: str = input("What is your favorite number?")
fav_number: int = int(fav_number_str)
higher_number: int = fav_number + 1

print("hello " + first_name + "!")
print("My favorite number is " + str(higher_number))