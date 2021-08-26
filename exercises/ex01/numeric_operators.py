"""This program lets you input two numbers and outputs four operations with them."""

__author__ = "730348936"

s_left: str = input("Left-hand side: ")
s_right: str = input("Right-hand side: ")
i_left = int(s_left)
i_right = int(s_right)
exponent = str((i_left ** i_right))
divide = str((i_left / i_right))
floor = str((i_left // i_right))
modulus = str((i_left % i_right))
print(s_left + " ** " + s_right + " is " + exponent)
print(s_left + " / " + s_right + " is " + divide)
print(s_left + " // " + s_right + " is " + floor)
print(s_left + " % " + s_right + " is " + modulus)