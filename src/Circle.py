import math
from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius, name='Circle'):
        super().__init__(radius, name)
        self.radius = radius

    @property
    def get_area(self) -> int:
        return math.pi * self.radius ** 2

    @property
    def get_perimeter(self) -> int:
        return 2 * math.pi * self.radius
