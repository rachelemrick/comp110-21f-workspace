"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730348936"


class Simpy:
    """Simplified Numpy class."""
    values: list[float]

    def __init__(self, xs: list[float]):
        """Constructor method for Simpy class."""
        self.values = xs

    def __str__(self) -> str:
        """String representation for Simpy class."""
        return f"Simpy({self.values})"

    def fill(self, x: float, number_of_xs: int):
        """Mutates: Creates a Simpy object full of repeated float values."""
        i = 0
        result: list[float] = []
        while i < number_of_xs:
            result.append(x)
            i += 1
        self.values = result

    def arange(self, start: float, stop: float, step=1.0):
        """Mutates: Creates a Simpy object given a range of values."""
        assert step != 0.0
        i = start
        result: list[float] = []
        if step > 0:
            while i < stop:
                result.append(i)
                i += step
        else:
            while i > stop:
                result.append(i)
                i += step
        self.values = result

    def sum(self) -> float:
        """Sums the values in the Simpy object."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the addition operator."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            result: list[float] = []
            i = 0
            while i < len(self.values):
                result.append(self.values[i] + rhs.values[i])
                i += 1
            Simpy_result: Simpy = Simpy(result)
            return Simpy_result
        elif isinstance(rhs, float):
            result: list[float] = []
            i = 0
            while i < len(self.values):
                result.append(self.values[i] + rhs)
                i += 1
            Simpy_result: Simpy = Simpy(result)
            return Simpy_result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the power operator."""
        result: list[float] = []
        i = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.append(self.values[i] ** rhs.values[i])
                i += 1
        elif isinstance(rhs, float) or isinstance(rhs, int):
            while i < len(self.values):
                result.append(self.values[i] ** rhs)
                i += 1
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overloads the == operator."""
        result: list[bool] = []
        i = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overloads the > operator."""
        result: list[bool] = []
        i = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        elif isinstance(rhs, float):
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads the subscription operator."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            result_list: list[float] = []
            i = 0
            while i < len(self.values):
                if rhs[i]:
                    result_list.append(self.values[i])
                i += 1
            return Simpy(result_list)