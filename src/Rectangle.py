from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_b: int, side_a: int):
        super().__init__(side_a, side_b, 0)
        if side_a <= 0 or side_b <= 0:
            raise ValueError("side_a and aide_b should be greate than 0")

    @property
    def get_area(self) -> int:
        return self.side_a * self.side_b

    @property
    def get_perimeter(self) -> int:
        return 2 * (self.side_a + self.side_b)

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure.")
        return self.get_area + other_figure.get_area
