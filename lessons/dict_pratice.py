"""Pratice with dictionaries"""

# The syntax is below
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3 # Adding another item in the dictionary
print("After adding mint")
print(ice_cream)

#Removing an item in the dictionary
ice_cream.pop("mint")
print("After remvoing mint")
print(ice_cream)

#Accessing
print(f"Number of vanilla orders: {ice_cream["vanilla"]}")

#Updating a value in a dictionary
ice_cream["vanilla"] += 1
print("After adding one vanilla")
print(ice_cream)

#Checking if it in a dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)