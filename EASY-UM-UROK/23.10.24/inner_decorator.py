class MyClass:
    def __init__(self, value) -> None:
        self._value = value

    @property
    def value(self):
        return self._value

    @staticmethod  # встроенный декоратор, статический метод
    def sum(a, b) -> None:
        print(a + b)

    def value_plus_two(self) -> None:
        print(self._value + 2)


class ClassMethodClass:
    @classmethod
    def get_class(cls, a):
        return cls(a)


my_class = MyClass(22)
my_class.sum(3, 5)
my_class.value_plus_two()
my_class.value = 22
my_class
