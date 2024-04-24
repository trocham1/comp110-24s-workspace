""""Ga."""

class ChristmasTreeFarm:
    """A christmas tree farm!"""

    #  This is the attrutue.
    plots: list[int]

    # This is the constructor.
    def __init__(self, plots: int, initital_planting: int) -> None:
        """Sets up the farm."""
        self.plots = []
        i: int = 0
        while i < initital_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1

    #  This is the method.
    def plant(self, plot_number) -> None:
        """Plants a given tree at a plot number."""
        self.plots[plot_number]

    # Method.
    def growth(self) -> None:
        """Grows each plants."""
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1
            i += 1