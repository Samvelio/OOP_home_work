from src.Figure import Figure


class Square(Figure):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than or equal to 0")
        super().__init__(side_a, side_a, 0)

    @property
    def get_area(self) -> int:
         return self.side_a * self.side_b

    @property
    def get_perimeter(self) -> int:
         return 4 * self.side_a
