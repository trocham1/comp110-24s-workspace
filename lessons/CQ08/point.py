"""Profile."""
from __future__ import annotations


class Point:
    """Class."""

    #  The attributes.
    x: float
    y: float

    # Constructor is next.
    def __init__(self, x_init: float, y_init: float):
        """The constructor."""
        self.x = x_init
        self.y = y_init

    # This is the method. The Mutating Method.
    def scale_by(self, factor: int) -> None:
        """Update the x and y attributes by multiple from factor."""
        self.x = self.x * factor
        self.y = self.y * factor
        self.x
        self.y

    # Method. The Non-Muatating method.
    def scale(self, factor: int) -> Point:
        """The scale."""
        a = self.x * factor
        b = self.y * factor
        return Point(self.x * factor, self.y * factor)


number: Point = Point(5, 4)
number.scale_by(5)
number.scale(10)