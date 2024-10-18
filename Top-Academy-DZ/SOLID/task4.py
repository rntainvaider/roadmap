class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
        
rect = Rectangle()
rect.set_width(4)
rect.set_height(5)
print("Площадь прямоугольника:", rect.area())  

square = Square()
square.set_width(4)
print("Площадь квадрата:", square.area())