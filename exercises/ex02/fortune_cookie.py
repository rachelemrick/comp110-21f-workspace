"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730348936"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
cookie_value: int = randint(1, 4)

print("Your fortune cookie says...")

if cookie_value == 1:
    print("You will soon do something that you are proud of.")
else:
    if cookie_value == 2:
        print("You will make a new friend soon.")
    else:
        if cookie_value == 3:
            print("Your random acts of kindness will pay off soon.")
        else:
            print("Something good will happen in your professional life.")

print("Now, go spread positive vibes!")