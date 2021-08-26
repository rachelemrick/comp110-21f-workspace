"""This program lets you input two numbers and outputs four comparisons with them."""

__author__ = "730348936"

s_left: str = input("Left-hand side: ")
s_right: str = input("Right-hand side: ")
i_left = int(s_left)
i_right = int(s_right)

less_than = str(i_left < i_right)
greater_equal = str(i_left >= i_right)
equal_to = str(i_left == i_right)
not_equal = str(i_left != i_right)

print(s_left + " < " + s_right + " is " + less_than)
print(s_left + " >= " + s_right + " is " + greater_equal)
print(s_left + " == " + s_right + " is " + equal_to)
print(s_left + " != " + s_right + " is " + not_equal)