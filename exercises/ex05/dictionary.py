"""ex05 dictionary."""

__author__ = "730711485"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Function should inverts the keys and values."""
    dict2: dict[str, str] = {}
    for key in dict1:
        value: str = dict1[key]
        dict2[value] = key
    return dict2


print(invert({'a': 'z', 'b': 'y', 'c': 'x'}))
print(invert({'apple': 'cat'}))


def favorite_color(dict2: dict[str, str]) -> str:  # Unsure about this one.
    """This function return the most popular color."""
    track = {}
    popular_color = ()
    for key, value in dict2.items():
        if value not in track:
            track[value] = 0
        else:
            track[value] += 1
    popular_color = max(track, key=track.get)
    return popular_color


print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def count(list2: list[str]) -> dict[str, int]:
    """This function count how many time a certain value has appeared in the list."""
    dict4: dict[str, int] = {}
    for key in list2:
        if key in dict4:
            dict4[key] += 1
        else:
            dict4[key] = 1
    return dict4


a: list[str] = ["a", "a", "a", "b"]
print(count(a))


def alphabetizer(list5: list[str]) -> dict[str, list[str]]:
    """This function return a dictonary of words that belong to a letter."""
    dict5: dict[str, list[str]] = {}
    for elem in list5:
        letter = elem[0]
        if letter in dict5:
            dict5[letter].append(elem)
        else:
            dict5[letter] = [elem]
    return dict5


alphabetizer(["Python", "sugar", "Turtle", "party", "table"])


def update_attendance(dict6: dict[str, list[str]], day: str, student: str) -> None:
    """This function mutate and return a dictionary."""
    student_list: list[str] = []
    if day in dict6:
        student_list = dict6[day]
        student_list.append(student)
        dict6[day] = student_list
    else:
        dict6[day] = student


attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)