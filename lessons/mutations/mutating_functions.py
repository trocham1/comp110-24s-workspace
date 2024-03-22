"""Functions that either mutate a list or not!"""

a: list[str] = ["Louie", "Bear", "Bo"]

def remove_first(input_list: list[str]) -> None:
    """Remove the first element of input_list. Mutating!"""
    input_list.pop(0)


def get_first(input_list: list[str]) -> str:
    """Return first element of input_list without mutating."""
    return input_list[0]


def get_and_remove_first(input_ist: list[str]) -> str:
    """Return first element AND remove it."""
    elem: str = input_ist[0]
    input_ist.pop(0)
    return elem

print(get_and_remove_first(a))
