"""Demonstrate Basic List syntax"""

# Create an empty list
grocery_list: list[str] = list () # <- constructor
grocery_list: list[str] = [] # <- literal
print("Empty list: ")
print(grocery_list)

# Add to a list
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding thing")
print(grocery_list)

# Create a list with objects in it
grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated list: ")
print(grocery_list2)

grocery_list2.append("whipped cream")
print("Add another thing")
print(grocery_list2)

# Indexing
print("Printing one thing:")
print(grocery_list2[2])

# Modifying by Index
x: list[str]= ["c", "a", "r", "s"]
x[2] = "t"
print(x)

grocery_list[0] = "cinnamon toast crunch"
print("Modifying: ")
print(grocery_list)


# Length of a list
print("Length:")
print(len(grocery_list))

# Removing an item
grocery_list.pop(1)
print("Remove an item:")
print(grocery_list)

# Function name: display
# Parameter: list[str]
# Return Nothing!
# Print out the list!
print(" Function!")

def display(n: list[str]) -> None:
    """idk"""
    print(n)

display(grocery_list)
x = display(["Anusha", "Jack", "Vrinda"])
print(x)


# Create a list!
# Name: create
# Parameters: str and str
# RV: list[str]
#Put both parameters into list and return that list

def create(word1: str, word2: str) -> list[str]:
    new_list: list[str] = [word1, word2]
    return new_list

print(create("Hello" , "World"))