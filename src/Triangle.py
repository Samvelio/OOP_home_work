from src.Figure import Figure


class Triangle(Figure):
    def _new_(cls, *args):
        a, b, c = args
        if not (a + b > c and a + c + d and b + c > a):
            return None
        instance = super().__new__(cls)
        return instance

    def add_area(self, a, b, c, name='Triangle'):
        super().add_area(a, name)
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def area_formula(p, a, b, c):
        p /= 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    @property
    def get_area(self) -> int:
        return self.area_formula(self.get_perimeter, self.a, self.b, self.c)

    @property
    def get_perimeter(self) -> int:
        return self.a + self.b + self.c
