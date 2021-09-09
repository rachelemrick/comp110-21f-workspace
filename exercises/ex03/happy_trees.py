"""Drawing forests in a loop."""

__author__ = "730348936"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

# Set up variables
depth: int = int(input("Depth: "))
tree_string: str = ""
i = 0

# Loop to create forest
while i < depth:
    tree_string = tree_string + TREE
    print(tree_string)
    i = i + 1