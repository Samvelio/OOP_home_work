import math
from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(0, 0, 0)
        if radius < 0:
            raise ValueError("Radius must be > 0")
        self.radius = radius

    @property
    def get_area(self) -> int:
        return math.pi * self.radius ** 2

    @property
    def get_perimeter(self) -> int:
        return 2 * math.pi * self.radius
