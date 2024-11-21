class Summa:
    a: int
    b: int

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"{self.a} + {self.b} = {self.a + self.b}"


summa = Summa(1, 2)
print(summa)
