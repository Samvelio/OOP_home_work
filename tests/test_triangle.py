from src.Triangle import Triangle


class TriangleTest():

    def test_triangle_perimeter(self):
        triangle = Triangle()
        assert isinstance(triangle, Triangle)
        assert triangle.side_a == 3
        assert triangle.side_b == 4
        assert triangle.side_c == 5
        assert triangle.get_perimeter == 12

    def test_triangle_area(self):
        assert isinstance(triangle, Triangle)
        assert triangle.side_a == 4
        assert triangle.side_b == 5
        assert triangle.side_c == 6
        assert triangle.get_area == 11.62
