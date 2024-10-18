import math

class Figure:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        print(f'Фигура: {self.name}; площадь: {self.get_area()}')
        
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__('прямоугольник')
 
    def get_area(self):
        return self.a * self.b
    
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        super().__init__('круг')
    
    def get_area(self):
        return round(math.pi * self.radius * self.radius, 2)
    
class RectangulaCircle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__('прямоугольный треугольник')
        
    def get_area(self):
        return self.a * self.b / 2
    
class Trapezoid(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        super().__init__('трапеция')

    def get_area(self):
        return 1 / 2 * (self.a + self.b) * self.h

rec = Rectangle(20, 40)
rec.__str__()

cir = Circle(20)
cir.__str__()

rec_cir = RectangulaCircle(20, 40)
rec_cir.__str__()

tra = Trapezoid(15, 20, 2)
tra.__str__()