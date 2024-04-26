"""File to define River class."""

__author__ = "730711485"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check the ages."""
        #  The bear loop.
        new_bear_list: list[Bear]
        new_bear_list = self.bears
        for bear in new_bear_list:
            if bear.age > 5:
                new_bear_list.remove(bear)
        self.bears = new_bear_list

        #  The fish loop.
        new_fish_list: list[Fish]
        new_fish_list = self.fish
        for fish in new_fish_list:
            if fish.age > 3:
                new_fish_list.remove(fish)
        self.fish = new_fish_list
        return None

    def bears_eating(self):
        """Bear eating."""
        if len(self.fish) >= 5:
            self.fish.remove_fish(3)
            self.bears.eat(3)
        return None
    
    def check_hunger(self):
        """Check the hunger of the bear."""
        new_bear_list: list[str]
        new_bear_list = self.bears
        for bear in new_bear_list:
            if bear.hunger_score < 0:
                new_bear_list.remove(bear)
        self.bears = new_bear_list

    def repopulate_fish(self):
        """Repopulate fish."""
        a = (len(self.fish) // 2) * 4
        b: list[str] = []
        for i in range(a):
            b.append(i)
        self.fish.append(b)
        return None
    
    def repopulate_bears(self):
        """Repopulate bear."""
        if len(self.bears) > 1:
            a = len(self.bears) // 2
            b: list[str] = []
            for i in range(a):
                b.append(i)
            self.bears.append(b)
        return None
    
    def view_river(self):
        """View the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fis in self.fish:
            fis.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """A week in the river."""
        for i in range(7):
            self.one_river_day()
    
    def remove_fish(self, amount: int):
        """Remove fish."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)
            i += 1
        return None