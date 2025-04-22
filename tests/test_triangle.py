import pytest
from src.Triangle import Triangle


class TestTriangle():

    def test_triangle_perimeter(self):
        triangle = Triangle(3, 4, 5)
        assert isinstance(triangle, Triangle)
        assert triangle.side_a == 3
        assert triangle.side_b == 4
        assert triangle.side_c == 5
        assert triangle.get_perimeter == 12

    def test_triangle_area(self):
        triangle = Triangle(4, 5, 6)
        assert isinstance(triangle, Triangle)
        assert triangle.side_a == 4
        assert triangle.side_b == 5
        assert triangle.side_c == 6
        assert triangle.get_area, 2 == 9.92

    def test_none_side(self):
        with pytest.raises(ValueError):
            Triangle()
