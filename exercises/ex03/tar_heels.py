"""An exercise in remainders and boolean logic."""

__author__ = "730348936"


# Begin your solution here...
number: int = int(input("Enter an int: "))

# Set up variables saying if input is divisible by 2 and/or 7
if (number % 2) == 0:
    divis_2: bool = True
else:
    divis_2: bool = False
if (number % 7) == 0:
    divis_7: bool = True
else:
    divis_7: bool = False
if (divis_2 and divis_7) is True:
    divis_both: bool = True
else:
    divis_both: bool = False

# Print output
if divis_both is True:
    print("TAR HEELS")
else:
    if divis_2 is True:
        print("TAR")
    else:
        if divis_7 is True:
            print("HEELS")
        else:
            print("CAROLINA")