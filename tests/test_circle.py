from src.Circle import Circle


class CircleTest():

    def test_circle_perimeter(self):
        circle = Circle()
        assert isinstance(circle, Circle)
        assert circle.radius == 10
        assert circle.get_perimeter == 62,8

    def test_circle_area(self):
        assert circle.radius == 5
        assert circle.get_area == 78,5
