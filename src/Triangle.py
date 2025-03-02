from src.Figure import Figure


class Triangle(Figure):
    def _new_(cls, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Invalid triangle sides")
        instance = super().__new__(cls)
        return instance

    def __init__(self, a, b, c):
        super().__init__(a, b, c)
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
