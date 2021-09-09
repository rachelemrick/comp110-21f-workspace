"""Finding duplicate letters in a word."""

__author__ = "730348936"

# Begin solution here by setting up variables
word: str = input("Enter a word: ")
word_len: int = len(word)
i1: int = 0
i2: int = 0
duplicate: bool = False

# Loop to choose the letter we search for, using counter i1
while i1 < word_len:
    letter: str = word[i1]
    # Loop to search for chosen letter, using counter i2
    while i2 < word_len:
        if letter == word[i2] and i1 != i2:
            duplicate = True
        i2 = i2 + 1
    # Reset i2 when done with i2 loop, and add 1 to i1
    i2 = 0
    i1 = i1 + 1

print("Found duplicate: " + str(duplicate))