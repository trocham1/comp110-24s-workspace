"""Mutating functions."""

__author__ = "730711485"


def manual_append(a: list[int], b: int) -> None:
    """Appending a list in the end."""
    a.append(b)


c: list[int] = [1, 2, 3]
manual_append(c, 2)
print(c)


def double(d: list[int]) -> None:
    """Doubling a list."""
    e = 0
    while e < len(d):
        d[e] *= 2
        e += 1


f: list[int] = [1, 2, 3]
double(f)
print(f)