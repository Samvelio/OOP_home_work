from src.Rectangle import Rectangle


class TestRectangle():

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(2, 7)
        assert isinstance(rectangle, Rectangle)
        assert rectangle.side_a == 7
        assert rectangle.side_b == 2
        assert rectangle.get_perimeter == 18

    def test_rectangle_area(self):
        rectangle = Rectangle(5, 9)
        assert rectangle.side_a == 9
        assert rectangle.side_b == 5
        assert rectangle.get_area == 45
