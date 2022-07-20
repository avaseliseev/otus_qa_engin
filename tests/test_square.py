import pytest

from src.square import Square


def test_created_square_two_args():
    with pytest.raises(TypeError):
        Square(10, 20)


def test_square_area(create_square):
    assert create_square.area == create_square.side_a ** 2


def test_square_perimetr(create_square):
    assert create_square.perimeter == create_square.side_a * 4


def test_sum_square_area_add_triangle(create_square, create_triangle):
    create_square.add_area(create_triangle)


def test_sum_square_area_add_not_figure(create_square):
    with pytest.raises(AttributeError):
        create_square.add_area('not figure')
