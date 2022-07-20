from math import pi

import pytest

from src.circle import Circle


def test_created_broken_circle():
    with pytest.raises(TypeError):
        Circle(10, 20)


def test_circle_area(create_circle):
    assert create_circle.area == 314


def test_circle_perimetr(create_circle):
    assert create_circle.perimeter == 2 * pi * create_circle.radius


def test_sum_circle_area_add_square(create_circle, create_square):
    create_circle.add_area(create_square)


def test_sum_circle_area_add_not_figure(create_circle):
    with pytest.raises(AttributeError):
        create_circle.add_area('not figure')
