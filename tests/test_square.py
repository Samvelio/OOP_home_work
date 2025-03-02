from src.Square import Square


class TestSquare():

    def test_square_perimeter(self):
        square = Square(5)
        assert isinstance(square, Square)
        assert square.side_a == 5
        assert square.side_b == 5
        assert square.get_perimeter == 20

    def test_square_area(self):
        square = Square(5)
        assert isinstance(square, Square)
        assert square.side_a == 5
        assert square.side_b == 5
        assert square.get_area == 25
