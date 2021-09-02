"""Counting letters in a string."""

__author__ = "730348936"


# Begin your solution here...

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i = 0
letter_count = 0

while i < len(word):
    if word[i] == letter:
        letter_count = letter_count + 1
    i = i + 1

print("Count: " + str(letter_count))