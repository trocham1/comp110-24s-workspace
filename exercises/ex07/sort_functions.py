"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    index_counter = range(1, len(x))
    for i in index_counter:
        sorting_value = x[i]
        while x[i-1] > sorting_value and i>0: # if the item on the left is greater than the item on right, then switch it.
            x[i], x[i-1] = x[i-1] , x[i]
            i -= 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    index_counter = range(0, len(x)-1)
    for i in index_counter:
        min_value = i
        for j in range(i+1, len(x)):
            if x[j] < x[min_value]:
                min_value = j
        if min_value != i:
            x[min_value], x[i] = x[i], x[min_value]
    return None
