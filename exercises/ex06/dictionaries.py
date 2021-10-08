"""Practice with dictionaries."""

__author__ = "730348936"


# Define your functions below
# invert function
def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of strings, it flips the keys and values."""
    new_dict = dict()
    list_new_keys = []
    for key in old_dict:
        value: str = old_dict[key]
        if value in list_new_keys:
            raise KeyError("Can't have duplicate keys.")
        else:
            list_new_keys.append(value)
            new_dict[value] = (key)
    return new_dict


# favorite_color function
def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns the color that is in the input dictionary the most."""
    colors_scores: dict[str, int] = {}
    for name in names_colors:
        color = names_colors[name]
        if color not in colors_scores:
            colors_scores[color] = 1
        else:
            colors_scores[color] += 1
    first_name: str = list(names_colors.keys())[0]
    score_of_top_scoring_color: int = 1
    top_scoring_color: str = names_colors[first_name]
    for color in colors_scores:
        score = colors_scores[color]
        if score > score_of_top_scoring_color:
            score_of_top_scoring_color = score
            top_scoring_color = color
    return top_scoring_color


# count function
def count(input: list[str]) -> dict[str, int]:
    """Returns a dictionary of how many times each string appears in a list."""
    result: dict[str, int] = {}
    for string in input:
        if string in result:
            result[string] += 1
        else:
            result[string] = 1
    return result