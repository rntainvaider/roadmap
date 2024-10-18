class Shape:
    def __init__(self):
        pass
    
    def Show(self):
        pass
    
    def Save(self, file_name):
        pass
    
    @staticmethod
    def Load(file_name):
        pass
    
class Square(Shape):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length
        
    def Show(self):
        print(f"Square: Top-left {self.x}, {self.y}, Length: {self.length}")
    
    def Save(self, file_name):
        with open(file_name, "a") as file:
            file.write(f"Square, {self.x}, {self.y}, {self.length}\n")
    
    @staticmethod        
    def Load(file_name):
        squares = []
        with open(file_name, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == "Square":
                    data = line.strip().split(",")
                    squares.append(Square(int(data[1]), int(data[2]), int(data[3])))
        return squares
                    
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def Show(self):
        print(f"Rectangle: Top-left {self.x}, {self.y}, Width: {self.width}, Height: {self.height}")
    
    def Save(self, file_name):
        with open(file_name, "a") as file:
            file.write(f"Rectangle, {self.x}, {self.y}, {self.width}, {self.height}\n")
        
    @staticmethod        
    def Load(file_name):
        rectagles = []
        with open(file_name, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == "Rectangle":
                    data = line.strip().split(",")
                    rectagles.append(Rectangle(int(data[1]), int(data[2]), int(data[3]), int(data[4])))
        return rectagles
            
class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def Show(self):
        print(f"Circle: {self.x}, {self.y}, Radius: {self.radius}")
    
    def Save(self, file_name):
        with open(file_name, "a") as file:
            file.write(f"Circle, {self.x}, {self.y}, {self.radius}\n")
    
    @staticmethod        
    def Load(file_name):
        sircles = []
        with open(file_name, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == "Circle":
                    data = line.strip().split(",")
                    sircles.append(Square(int(data[1]), int(data[2]), int(data[3])))
        return sircles
            
class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def Show(self):
        print(f"Ellipse: Top-left {self.x}, {self.y}, Width: {self.width}, Height: {self.height}")
    
    def Save(self, file_name):
        with open(file_name, "a") as file:
            file.write(f"Ellipse, {self.x}, {self.y}, {self.width}, {self.height}\n")
    
    @staticmethod        
    def Load(file_name):
        ellipses = []
        with open(file_name, "r") as file:
            for line in file:
                if line.strip().split(",")[0] == "Ellipse":
                    data = line.strip().split(",")
                    ellipses.append(Ellipse(int(data[1]), int(data[2]), int(data[3]), int(data[4])))
        return ellipses
            
shapes = [Square(10, 12, 5), Rectangle(5, 4, 2, 3), Circle(5, 2, 10), Ellipse(2, 4, 12, 10)]

file_name = "shapes.txt"
for shape in shapes:
    shape.Save(file_name)
    
new_shapes = []
new_shapes.extend(Square.Load(file_name))
new_shapes.extend(Rectangle.Load(file_name))
new_shapes.extend(Circle.Load(file_name))
new_shapes.extend(Ellipse.Load(file_name))

for shape in new_shapes:
    shape.Show()