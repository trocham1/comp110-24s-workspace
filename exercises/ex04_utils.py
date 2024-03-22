"""ex04_utils."""

__author__ = "730711485"


# The all function.
def all(list1: list[int], value: int) -> bool:
    """The all function should return a bool operation."""
    counter: int = 0
    true_counter: int = 0
    false_counter: int = 0
    if len(list1) == 0:
        return False
    else:
        while counter < len(list1):
            if list1[counter] == value:
                true_counter += 1
            else: 
                false_counter += 1
            counter += 1
        if false_counter == 0:
            return True
        else: 
            return False


# The max function.


def max(list2: list[int]) -> int:
    """Max should return the largest number in the list."""
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    counter: int = 0
    highest_num: int = (list2[counter])
    while counter < len(list2):
        if list2[counter] > highest_num:
            highest_num = list2[counter]
        counter += 1
    return highest_num


# The is_equal function.


def is_equal(list3: list[int], list4: list[int]) -> bool:
    """The function check every element in a list to see if they are true."""
    counter: int = 0
    true_counter: int = 0
    false_counter: int = 0
    if len(list3) < len(list4) or len(list3) > len(list4):
        return False
    else:
        while counter < len(list3):
            if list3[counter] == list4[counter]:
                true_counter += 1
            else:
                false_counter += 1
            counter += 1
    if false_counter == 0:
        return True
    else:
        return False


# This is the extend function.
def extend(list5: list[int], list6: list[int]) -> None:
    """This extend function append two list together into a longer list."""
    counter: int = 0
    while counter < len(list6):
        list5.append(list6[counter])
        counter += 1
    return None