"""EX05 - Dictionary Functions Testing."""


__author__ = "730718367"


import pytest

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use_case_1() -> None:
    """Test function invert with dict[str, str]."""
    test_dict: dict[str, str] = {"a": "Apple", "b": "Banana", "c": "Coconut"}
    assert invert(test_dict) == {"Apple": "a", "Banana": "b", "Coconut": "c"}


def test_invert_use_case_2() -> None:
    """Test function invert with empty dict."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_edge_case() -> None:
    """Test function invert with dict[str, str] with same value."""
    test_dict: dict[str, str] = {"a": "Apple", "b": "Apple", "c": "Coconut"}
    with pytest.raises(KeyError):
        invert(test_dict)


def test_favorite_color_use_case_1() -> None:
    """Test function favorite_color with dict[str, str]."""
    test_dict: dict[str, str] = {"A": "White", "B": "Gray", "C": "Black", "D": "Black"}
    assert favorite_color(test_dict) == "Black"


def test_favorite_color_use_case_2() -> None:
    """Test function favorite_color with empty dict."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_favorite_color_edge_case() -> None:
    """Test function favorite_color with dict[str, str] with two favorite color."""
    test_dict: dict[str, str] = {"A": "White", "B": "White", "C": "Black", "D": "Black"}
    assert favorite_color(test_dict) == "White"


def test_count_use_case_1() -> None:
    """Test function count with list[str]."""
    test_list: list[str] = ["A", "A", "B", "C"]
    assert count(test_list) == {"A": 2, "B": 1, "C": 1}


def test_count_use_case_2() -> None:
    """Test function count with empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_edge_case() -> None:
    """Test function count with list[str] with values with different case letter."""
    test_list: list[str] = ["a", "A", "B", "C"]
    assert count(test_list) == {"a": 1, "A": 1, "B": 1, "C": 1}


def test_alphabetizer_use_case_1() -> None:
    """Test function alphabetizer with list[str]."""
    test_list: list[str] = ["apple", "banana", "coconut"]
    assert alphabetizer(test_list) == {"a": ["apple"], "b": ["banana"], "c": ["coconut"]}


def test_alphabetizer_use_case_2() -> None:
    """Test function alphabetizer with empty list."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_alphabetizer_edge_case() -> None:
    """Test function alphabetizer with list[str] with different case letter."""
    test_list: list[str] = ["apple", "Avocado", "banana", "coconut"]
    assert alphabetizer(test_list) == {"a": ["apple", "Avocado"], "b": ["banana"], "c": ["coconut"]}


def test_update_attendance_use_case_1() -> None:
    """Test function update_attendnace with dict[str, list[str]], str, str."""
    test_dict: dict[str, list[str]] = {"Monday": ["Abby", "Ben"], "Wednesday": ["Cathy"]}
    test_day: str = "Friday"
    test_student: str = "Danny"
    update_attendance(test_dict, test_day, test_student)
    assert test_dict == {"Monday": ["Abby", "Ben"], "Wednesday": ["Cathy"], "Friday": ["Danny"]}


def test_update_attendance_use_case_2() -> None:
    """Test function update_attendnace with empty dict, str, str."""
    test_dict: dict[str, list[str]] = {}
    test_day: str = "Friday"
    test_student: str = "Danny"
    update_attendance(test_dict, test_day, test_student)
    assert test_dict == {"Friday": ["Danny"]}


def test_update_attendance_edge_case() -> None:
    """Test function update_attendnace with dict[str, list[str]] but with already existing str, str."""
    test_dict: dict[str, list[str]] = {"Monday": ["Abby", "Ben"], "Wednesday": ["Cathy"], "Friday": ["Danny"]}
    test_day: str = "Friday"
    test_student: str = "Danny"
    update_attendance(test_dict, test_day, test_student)
    assert test_dict == {"Monday": ["Abby", "Ben"], "Wednesday": ["Cathy"], "Friday": ["Danny"]}