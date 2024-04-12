"""Writing a recursive Function."""

__author__ = "730711485"


def g(n: int, k: int) -> int:
    """This is the standard function in python."""
    return n * k


# Recursive Definition
def f(n: int, k: int) -> int:
    """Recursive Definition."""
    if n == 0:  # Base case is here.
        return 0
    else:  # The recursive rule is here.
        return f(n - 1, k) + k
    

print(f(5, 4))