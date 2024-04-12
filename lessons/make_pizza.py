"""Pratice instantiating pizza class"""


from pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
sals_pizza: Pizza = Pizza("small", 2, False)


def price(pizza_order: Pizza) -> float:
    """Calculate and return cost of pizza."""
    if pizza_order.size == "large":
        cost = 6.0
    else:
        cost = 5.0
    #  charge .75 per toppings
    cost += .75 * pizza_order.toppings
    #  charge $1 for gluten free
    if pizza_order.gluten_free:
        cost += 1
    return cost


print(my_pizza.toppings)
print(my_pizza.price())
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())