"""Unit tests for dictionary functions."""

# Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730348936"


# invert tests
def test_invert_empty_dictionary() -> None:
    """Tests invert with an empty dictionary."""
    assert invert({}) == {}


def test_invert_two_elements() -> None:
    """Tests invert with a two element dictionary."""
    assert invert({"a": "z", "b": "y"}) == {"z": "a", "y": "b"}


def test_invert_four_elements() -> None:
    """Tests invert with a four element dictionary."""
    test_dict = {"1": "a", "2": "b", "3": "c", "4": "d"}
    assert invert(test_dict) == {"a": "1", "b": "2", "c": "3", "d": "4"}


# favorite_color tests
def test_favorite_color_single() -> None:
    """Tests favorite_color with a single element dictionary."""
    assert favorite_color({"Rachel": "black"}) == "black"


def test_favorite_color_two_elements() -> None:
    """Tests favorite_color with a two element dictionary."""
    assert favorite_color({"Rachel": "red", "Alex": "blue"}) == "red"


def test_favorite_color_three_elements() -> None:
    """Tests favorite_color with a three element dictionary."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


# count test
def test_count_empty_input() -> None:
    """Tests count with an empty input list."""
    assert count([]) == {}


def test_count_two_elements() -> None:
    """Tests count with a two element input list."""
    assert count(["a", "b"]) == {"a": 1, "b": 1}


def test_count_four_elements() -> None:
    """Tests count with a four element input list, with repeats."""
    output: dict = {"a": 1, "b": 2, "c": 1}
    assert count(["a", "b", "c", "b"]) == output