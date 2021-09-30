"""Unit tests for list utility functions."""

__author__ = "730348936"


from exercises.ex05.utils import only_evens, sub, concat


# only_evens tests
def test_only_evens_empty() -> None:
    """Tests only_evens with an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_two_elements() -> None:
    """Tests only_evens with a 2 element list."""
    xs: list[int] = [2, 5]
    assert only_evens(xs) == [2]


def test_only_evens_five_elements() -> None:
    """Tests only_evens with a 5 element list."""
    xs: list[int] = [3, 6, 1, 9, 12]
    assert only_evens(xs) == [6, 12]


# sub tests
def test_sub_empty() -> None:
    """Tests sub with an empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 0) == []


def test_sub_1_to_4() -> None:
    """Tests sub with a list from indices 1 to 4."""
    xs: list[int] = [0, 3, 4, 5, 2, 11]
    assert sub(xs, 1, 4) == [3, 4, 5]


def test_sub_0_to_2() -> None:
    """Tests sub with a list from indices 0 to 2."""
    xs: list[int] = [0, 3, 4, 5, 2, 11]
    assert sub(xs, 0, 2) == [0, 3]


# concat tests
def test_concat_empty() -> None:
    """Tests concat with an empty list."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_evens_odds() -> None:
    """Tests concat with an even and an odd list."""
    xs: list[int] = [0, 2, 4]
    ys: list[int] = [1, 3, 5]
    assert concat(xs, ys) == [0, 2, 4, 1, 3, 5]


def test_concat_long_short() -> None:
    """Tests concat with a long and a short list."""
    xs: list[int] = [2, 4, 6, 7, 8, 11]
    ys: list[int] = [3]
    assert concat(xs, ys) == [2, 4, 6, 7, 8, 11, 3]