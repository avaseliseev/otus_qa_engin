from src.figure import Figure
from math import pi, pow


class Circle(Figure):
    NAME = 'circle'

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self) -> float:
        return pi * pow(self.radius, 2)

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.radius
