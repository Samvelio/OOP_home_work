import math
from src.Figure import Figure


class Circle(Figure):
    def add_area(self, radius, name='Circle'):
        if radius < 0:
            raise ValueError("Radius must be >0")
        super().add_area(radius, name)
        self.radius = radius

    @property
    def get_area(self) -> int:
        return math.pi * self.radius ** 2

    @property
    def get_perimeter(self) -> int:
        return 2 * math.pi * self.radius
