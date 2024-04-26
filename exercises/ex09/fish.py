"""File to define Fish class."""


class Fish:
    """Fish."""

    #  The Attributes.
    age: int

    def __init__(self):
        """Init."""
        self.age = 0
        return None
    
    def one_day(self):
        """Day one."""
        self.age += 1
        return None