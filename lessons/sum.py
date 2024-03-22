"""Summing the elements of a list using different loops."""

__author__ = "730711485"

# Part 1.w_sum().


def w_sum(vals: list[float]) -> float:
    """Summing a list using a while loop."""
    idx: int = 0
    sum1: float = (0)
    while idx < len(vals):
        sum1 += vals[idx]
        idx += 1
    return sum1


print(w_sum([1.1, 0.9, 1.0]))


# Part 2.f-sum().

def f_sum(vals: list[float]) -> float:
    """Summing using a for...in... loop."""
    sum2: float = (0)
    for elem in vals:
        sum2 += elem
    return sum2


print(f_sum([1.1, 0.9, 1.0]))


# Part 3. f_range_sum().

def f_range_sum(vals: list[float]) -> float:
    """Summing a list using for...in rang()."""
    sum3: float = (0)
    for elem in range(0, len(vals)):
        sum3 += vals[elem]
    return sum3


print(f_range_sum([1.1, 0.9, 1.0]))
