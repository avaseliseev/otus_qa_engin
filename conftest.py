import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture
def create_square():
    return Square(10)


@pytest.fixture
def create_triangle():
    return Triangle(10, 12, 14)


@pytest.fixture
def create_circle():
    return Circle(10)


@pytest.fixture
def create_rectangle():
    return Rectangle(10, 15)
