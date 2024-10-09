from src.Figure import Figure


class Rectangle(Figure):
    def add_area(self, side_b: int, side_a: int):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("side_a and aide_b should be greate than 0")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self) -> int:
        return self.side_a * self.side_b

    @property
    def get_perimeter(self) -> int:
        return 2 * (self.side_a + self.side_b)
