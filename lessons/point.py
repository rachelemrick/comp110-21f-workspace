"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point."""
        return Point(self.x * factor, self.y * factor)
    
    # Magic Methods
    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"

    # Operator Overload
    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for a Point * float."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Overload the addition operator for a Point + Point."""
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


p0: Point = Point(1.0, 2.0)
p1: Point = p0 * 2.0
print(p0)
print(p1)

# Magic Methods
p1_repr: str = repr(p1)
print(p1_repr)

# Operator Overload
print(p0 + p1)
print(p0[1])