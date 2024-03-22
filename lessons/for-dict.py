"""Pratice with Dictionaries and for Loops"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apple": True}

# print out the keys that have True Values
for key in in_stock:
    # key is going ot be "carrots", "beet", "apples"
    # in_stock[key] is going to be True, False, True
   if in_stock[key]: #if in_stock[key] is True
      print(key)