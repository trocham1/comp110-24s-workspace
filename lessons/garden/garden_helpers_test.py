"""Test my garden functions."""

__author__ = "730711485"


from lessons.garden.garden_helps import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_normal() -> None:
    """This function should return recently add a plant in an exisiting plant_kind."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plant_kind: str = "flower"
    plant: str = "rose"
    new_add_by_kind_dictionary = by_kind
    assert add_by_kind(by_kind, plant_kind, plant) == new_add_by_kind_dictionary


def test_add_by_kid_empty_dictionary() -> None:
    """This function should return a new plant and plant kind in a empty list."""
    by_kind: dict[str, list[str]] = {}
    plant_kind: str = "flower"
    plant: str = "rose"
    new_add_by_kind_dictionary = by_kind
    assert add_by_kind(by_kind, plant_kind, plant) == new_add_by_kind_dictionary


def test_add_by_date_normal() -> None:
    """This function should return a new plant in a exisiting month in the dictionary."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    month: str = "June"
    plant: str = "Rose"
    new_by_date_list = by_date
    assert add_by_date(by_date, month, plant) == new_by_date_list


def test_add_by_date_empty_dictionary() -> None:
    """This function should return a new month and plant in a empty list."""
    by_date: dict[str, list[str]] = {}
    month: str = "April"
    plant: str = "marigold"
    new_by_date_list = by_date
    assert add_by_date(by_date, month, plant) == new_by_date_list


def test_look_up_kind_and_date_normal() -> None:
    """This function should return a 'no flower to plant in June'."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    plant_kinds: str = "flower"
    month: str = "June"
    str_output = f"No {plant_kinds} to plant in {month}"
    assert lookup_by_kind_and_date(by_kind, by_date, plant_kinds, month) == str_output


def test_look_up_kind_and_date_empty() -> None:
    """This function should return 'vegetables to plant in June: ['carrots']."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    plant_kinds: str = "vegetable"
    month: str = "June"
    str_output = f"({plant_kinds}s to plant in {month}: ['carrots'])"
    assert lookup_by_kind_and_date(by_kind, by_date, plant_kinds, month) == str_output