from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Circle(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return 2 * math.pi * self.radius

    def volume(self):
        return math.pi * self.radius * 2 * self.height


class Cube(Shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge
    

circle = Circle(5, 10)
print(f"Площадь круга - {circle.area()}")
print(f"Объём круга - {circle.volume()}")

cube = Cube(10)
print(f"Площадь куба - {cube.area()}")
print(f"Объем куба - {cube.volume()}")