"""Some function for my garden plan!"""


__author__ = "730711485"


# Function name: add_by_kind
# Parameters: dict[str, list[str]], str, str
# Return Type: None


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Adding plant based on plant type."""
    if plant_kind in plants_by_kind:  # if key "plant_kind" is in "plants_by_kind"
        plants_by_kind[plant_kind].append(plant)
    else:
        # if key "plant_kind" is NOT in "plant_by_kind"
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)
    return plants_by_kind


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Adding plant based on month."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)
    return plants_by_date


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kinds: str, month: str) -> str:
    """Function look up month and plant."""
    assert plant_kinds in plants_by_kind
    assert month in plants_by_date
    # look up the list of plants of kind "plant_kind"
    list_of_plants_by_kinds: list[str] = plants_by_kind[plant_kinds]
    # look up the list of plants by month planted
    list_of_plants_by_date: list[str] = plants_by_date[month]
    # list_of_plants_by_kind = ["migrorat", ]
    combined: list[str] = []
    for plant in list_of_plants_by_kinds:
        for other_plant in list_of_plants_by_date:
            if other_plant == plant:
                combined.append(other_plant)
    # <plant_kind> to p
    if len(combined) > 0:
        return f"({plant_kinds}s to plant in {month}: {combined})"
    else:
        #  No <plant_kinds> to plant in <month>.
        return f"No {plant_kinds} to plant in {month}"
    

by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
plant_kinds: str = "vegetable"
month: str = "June"

print(lookup_by_kind_and_date(by_kind, by_date, plant_kinds, month))