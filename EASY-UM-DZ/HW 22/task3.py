import math

class Circle:
    def __init__(self, x: int = 0, y: int = 0, radius: int = 1) -> None:
        self.x = x
        self.y = y
        self.radius = radius

class CircleCan(Circle):
    def get_area(self) -> float:
        area = round(math.pi * self.radius ** 2, 2)
        return area

    def get_perimeter(self) -> float:
        perimeter = round(2 * math.pi * self.radius, 2)
        return perimeter

    def increase(self, k: int) -> None:
        self.radius *= k

    def intersect_with_another_circle(self, other_circle) -> None:
        distance = math.sqrt((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2)
        return distance <= self.radius + other_circle.radius

circle_can1 = CircleCan(2, 3, 5)
circle_can2 = CircleCan(2, 4, 5)

circle_can1.increase(2)
circle_can2.increase(3)

print(f"Площадь круга 1: {circle_can1.get_area()}")
print(f"Периметр круга 1: {circle_can1.get_perimeter()}")
print(f"Площадь круга 2: {circle_can2.get_area()}")
print(f"Периметр круга 2: {circle_can2.get_perimeter()}")

if circle_can1.intersect_with_another_circle(circle_can2):
    print("Круги пересекаются")
else:
    print("Круги не пересекаются")
