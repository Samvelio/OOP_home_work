from src.Rectangle import Rectangle


class RectangleTest():

    def test_rectangle_perimeter(self):
        rectangle = Rectangle()
        assert isinstance(rectangle, Rectangle)
        assert rectangle.side_a == 2
        assert rectangle.side_b == 7
        assert rectangle.get_perimeter == 18

    def test_rectangle_area(self):
        rectangle = Rectangle()
        assert rectangle.side_a == 5
        assert rectangle.side_b == 9
        assert rectangle.get_area == 45
