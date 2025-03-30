from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a=None, b=None, c=None):
        if a is None or b is None or c is None:
            raise ValueError("Invalid triangle sides")
        self.side_a = a
        self.side_b = b
        self.side_c = c

    @staticmethod
    def area_formula(p, a, b, c):
        p /= 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    @property
    def get_area(self) -> float:
        return self.area_formula(self.get_perimeter, self.side_a, self.side_b, self.side_c)

    @property
    def get_perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c
