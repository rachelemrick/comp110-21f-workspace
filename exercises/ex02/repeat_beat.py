"""Repeating a beat in a loop."""

__author__ = "730348936"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
i = 0
beat_string: str = ""

if number > 0: 
    while i < number:
        beat_string = beat_string + beat + " "
        i = i + 1
    print(beat_string[0:len(beat_string) - 1])
else: 
    print("No beat...")