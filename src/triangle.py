from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    NAME = 'triangle'

    def __init__(self, side_a, side_b, side_c):
        if ((side_a + side_b) < side_c) or \
                ((side_a + side_c) < side_b) or \
                ((side_c + side_b) < side_a):
            raise ValueError('wrong figure')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self) -> float:
        half_perimeter = self.perimeter / 2
        return sqrt(half_perimeter *
                    ((half_perimeter - self.side_a) *
                     (half_perimeter - self.side_b) *
                     (half_perimeter - self.side_c)))

    @property
    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c
