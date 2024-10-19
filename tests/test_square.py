from src.Square import Square


class SquareTest():

    def test_square_perimeter(self):
        square = Square()
        assert isinstance(square, Square)
        assert square.side_a == 5
        assert square.side_b == 5
        assert square.get_perimeter == 25

    def test_square_area(self):
        assert square.side_a == 5
        assert square.side_b == 5
        assert square.get_area == 25
        