import pytest

from src.rectangle import Rectangle


def test_created_rectangle_three_args():
    with pytest.raises(TypeError):
        Rectangle(10, 20, 30)


def test_square_area(create_rectangle):
    assert create_rectangle.area == create_rectangle.side_a * create_rectangle.side_b


def test_rectangle_perimetr(create_rectangle):
    assert create_rectangle.perimeter == (create_rectangle.side_a + create_rectangle.side_b) * 2


def test_sum_rectangle_area_add_circle(create_rectangle, create_circle):
    create_rectangle.add_area(create_circle)


def test_sum_rectangle_area_add_not_figure(create_rectangle):
    with pytest.raises(AttributeError):
        create_rectangle.add_area('not figure')
