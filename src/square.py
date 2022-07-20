from src.figure import Figure
from math import pow


class Square(Figure):
    NAME = 'square'

    def __init__(self, side_a):
        self.side_a = side_a

    @property
    def area(self) -> float:
        return pow(self.side_a, 2)

    @property
    def perimeter(self) -> float:
        return self.side_a * 4
