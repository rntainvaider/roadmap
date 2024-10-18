# def get_square_triangle():
#     a = int(input("Введите длину катета a: "))
#     b = int(input("Введите длину катета b: "))
#     square = (a * b) / 2
#     return square

# if __name__ == "__main__":
#     print(get_square_triangle())


class SquareTriangle:
    def __init__(self) -> None:
        self.a = None
        self.b = None

    def __str__(self) -> str:
        return f"Сумма площади треугольника равна {self.a * self.b / 2}"

class BuilderSquareTriangle:
    def __init__(self) -> None:
        self.square_triangle = SquareTriangle()

    def get_a(self, a: int):
        self.square_triangle.a = a
        return self

    def get_b(self, b:int):
        self.square_triangle.b = b
        return self

    def get_square_builder(self):
        return self.square_triangle
    

if __name__ == "__main__":
    builder_square_triangle = BuilderSquareTriangle()

    a = int(input("Введите длину катета a: "))
    b = int(input("Введите длину катета b: "))
    
    s = (builder_square_triangle.get_a(a).get_b(b).get_square_builder())
    print(s)