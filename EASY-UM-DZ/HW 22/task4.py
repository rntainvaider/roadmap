class Child:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.is_calm = True
        self.is_hunger = False

    def info(self) -> str:
        return f"Ребенок: {self.name}, Возраст: {self.age}, Спокоен: {self.is_calm}, Голоден: {self.is_hunger}"

    def calm_down(self) -> None:
        self.is_calm = False

    def feed(self) -> None:
        self.is_hunger = True

class Parent:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.children = list()

    def add_fhild(self, child: Child) -> None:
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f"{child.name} добавлен(а) как ребенок.")
        else:
            print(f"{child.name} слишком стар(а), чтобы стать ребенком {self.name}")

    def info(self) -> str:
        return f"Меня зовут {self.name}, мне {self.age} лет, мои дети {self.list_cildren}"

    def calm_child(self) -> None:
        pass

    def feed_baby(self) -> None:
        pass
