"""Splitting a dictionary into two lists!"""

__author__ = "730711485"


def get_keys(list1: dict[str, int]) -> list[str]:  # Use [] for dict and {} for list.
    """The function should return a list."""
    list2: list[str] = []
    for key in list1:
        list2.append(key)
    return list2


a: dict[str, int] = {"Hello": 1, "World": 2}


def get_values(list2: dict[str, int]) -> list[int]:
    """The function should return the value of a list."""
    list3: list[int] = []
    for key in list2:
        list3.append(list2[key])
    return list3