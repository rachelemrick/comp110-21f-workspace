"""List utility functions part 2."""

__author__ = "730348936"


# Define your functions below
# only_evens function
def only_evens(xs: list[int]) -> list[int]:
    """Returns a list of only the even elements of the input list."""
    i: int = 0
    new_list: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            new_list.append(xs[i])
        i += 1
    return new_list


# sub function
def sub(xs: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns only a subsection of a list."""
    if len(xs) == 0 or start_index > len(xs) or end_index <= 0:
        return []
    if start_index < 0:
        start_index = 0
    if end_index > len(xs):
        end_index = len(xs)
    i: int = start_index
    new_list: list[int] = []
    while i < end_index:
        new_list.append(xs[i])
        i += 1
    return new_list


# concat function
def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Returns a list that is all of the elements of the first list, and then all of the elements of the second."""
    i: int = 0
    j: int = 0
    new_list: list[int] = []
    while i < len(xs):
        new_list.append(xs[i])
        i += 1
    while j < len(ys):
        new_list.append(ys[j])
        j += 1
    return new_list