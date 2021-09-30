"""List utility functions."""

__author__ = "730348936"


# TODO: Implement your functions here.

# Define function "all" 
def all(haystack: list[int], needle: int) -> bool:
    """Takes a list and an integer. Returns True if the list is only comprised of that integer, and False otherwise."""
    if len(haystack) == 0:
        return False
    i: int = 0
    while i < len(haystack):
        if haystack[i] != needle:
            return False
        i = i + 1
    return True


# Define function "is_equal"
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Takes two lists. Returns True if every element of both is equal, False otherwise."""
    if len(list_1) != len(list_2):
        return False
    i: int = 0
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i = i + 1
    return True


# Define function "max"
def max(input: list[int]) -> int:
    """Returns the largest value in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest_value = input[0]
    while i < len(input):
        if input[i] > largest_value:
            largest_value = input[i]
        i = i + 1
    return largest_value