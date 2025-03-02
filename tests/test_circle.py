from src.Circle import Circle


class TestCircle():

    def test_circle_perimeter(self):
        circle = Circle(10)
        assert isinstance(circle, Circle)
        assert circle.radius == 10
        assert abs(circle.get_perimeter)

    def test_circle_area(self):
        circle = Circle(10)
        assert circle.radius == 10
        assert abs(circle.get_area)
