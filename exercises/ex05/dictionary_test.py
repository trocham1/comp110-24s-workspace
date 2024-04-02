"""Unit Test!"""

__author__ = "730711485"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use_case() -> None:
    """This function should return an inverted dictionary of the letters."""
    dict1: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    dict2: dict[str, str] = {'z': 'a', 'y': 'b', 'x': 'c'}
    dict3: dict[str, str] = invert(dict1)
    assert dict3 == dict2


def test_invert_use_case_1() -> None:
    """This function return an inverted dictionary of the words."""
    dict1: dict[str, str] = {'apple': 'cat'}
    dict2: dict[str, str] = {'cat': 'apple'}
    assert invert(dict1) == dict2


def test_invert_edge_case() -> None:  # Checked this one again.
    """This function should return an inverted dictionary containing blank."""
    dict1: dict[str, str] = {'apple': ""}
    dict2: dict[str, str] = {"": 'apple'}
    assert invert(dict1) == dict2


def test_favorite_color_use_case1() -> None:
    """This function should return the most popular color from a dictionary containing names."""
    dict1: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    dict2 = ("blue")
    assert favorite_color(dict1) == dict2


def test_favorite_color_use_case2() -> None:
    """This function should return the most popular color from a dictionary containing colors as names."""
    dict1: dict[str, str] = {"blue": "yellow", "red": "yellow"}
    popular_color = ("yellow")
    dict2 = popular_color
    assert favorite_color(dict1) == dict2


def test_favorite_color_edge_case() -> None:
    """This function should return the popula color from blank name."""
    dict1: dict[str, str] = {"": "yellow", "": "yellow"}
    dict2 = ("yellow")
    assert favorite_color(dict1) == dict2


def test_count_use_case1() -> None:
    """This function return the count for a list of same letters."""
    list1: list[str] = ["a", "a", "a"]
    dict1: dict[str, int] = {"a": 3}
    assert count(list1) == dict1


def test_count_use_case2() -> None:
    """This function return the count for a list of all number."""
    list1: list[str] = [1, 1, 1]
    dict1: dict[str, int] = {1: 3}
    assert count(list1) == dict1


def test_count_edge_case() -> None:
    """This function return the count for a blank list."""
    list1: list[str] = ["", "", ""]
    dict1: dict[str, int] = {"": 3}
    assert count(list1) == dict1


def test_alphabetizer_use_case_1() -> None:
    """This function return a dictionary of words beloning to a letter."""
    list1: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    dict1: dict[str, list[str]] = {'P': ['Python'], 's': ['sugar'], 'T': ['Turtle'], 'p': ['party'], 't': ['table']}
    assert alphabetizer(list1) == dict1


def test_alphabetizer_use_case_2() -> None:
    """This function return a dictionary of words from a list of lowercase words."""
    list1: list[str] = ["python", "sugar", "turtle", "party", "table"]
    dict1: dict[str, list[str]] = {'p': ['python', 'party'], 's': ['sugar'], 't': ['turtle', 'table']}
    assert alphabetizer(list1) == dict1


def test_alphabetizer_edge_case() -> None:
    """This funcion return a dictionary of word that are all the same."""
    list1: list[str] = ["python", "python", "python"]
    dict1: dict[str, list[str]] = {'p': ['python', 'python', 'python']}
    assert alphabetizer(list1) == dict1


def test_update_attendance_1() -> None:
    """This function return and mutate the dictionary."""
    attendance_log: dict = {"Monday": ["Vrinda"]}
    day = "Tuesday"
    student = "Kaleb"
    student_list = update_attendance(attendance_log, day, student)
    assert update_attendance(attendance_log, day, student) == student_list


def test_update_attendance_2() -> None:
    """This function return and mutate the diictionary."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day = "Tuesday"
    student = "Kaleb"
    student_list: dict[str] = update_attendance(attendance_log, day, student)
    assert update_attendance(attendance_log, day, student) == student_list


def test_update_attendance_edge_case() -> None:
    """This function return a dictionary from a empty dictionary."""
    attendance_log_1: dict = {}
    day_1 = "Tuesday"
    student_1 = "Vrinda"
    student_list: dict = {'Tuesday': ['Vrinda']}
    assert update_attendance(attendance_log_1, day_1, student_1) == student_list