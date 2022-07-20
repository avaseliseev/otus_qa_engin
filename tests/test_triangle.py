import pytest

from src.triangle import Triangle


def test_created_broken_triangle():
    with pytest.raises(ValueError):
        Triangle(10, 20, 40)


def test_triangle_area(create_triangle):
    assert create_triangle.area == 58.787753826796276


def test_triangle_perimetr(create_triangle):
    assert create_triangle.perimeter == create_triangle.side_a + \
           create_triangle.side_b + create_triangle.side_c


def test_sum_triangle_area_add_circle(create_triangle, create_circle):
    create_triangle.add_area(create_circle)


def test_sum_triangle_area_add_not_figure(create_triangle):
    with pytest.raises(AttributeError):
        create_triangle.add_area('not figure')
