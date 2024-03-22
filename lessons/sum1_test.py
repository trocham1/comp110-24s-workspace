"""Test sum functionality."""

from lessons.sum1 import sum

def test_sum_empty() -> None:
    assert sum([]) == 0

def test_sum_one_element() -> None:
    """Sum of one element shoudl return that element."""
    test: list[int] = [7]
    assert sum(test) == 7

def test_sum_positive() -> None:
    """Sum of positive numbers should return sum of those number."""
    test: list[int] = [2, 4, 6]
    assert sum(test) == 12

def test_sum_with_neagtive() -> None:
    """Sum should work with positive and negative numbers."""
    test: list[int] = [2, -2, 4]
    assert sum(test) == 4


