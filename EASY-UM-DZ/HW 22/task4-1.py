class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_calm = False  # Состояние спокойствия
        self.is_hungry = True  # Состояние голода

    def info(self):
        """Выводит информацию о ребёнке."""
        return f"Ребёнок: {self.name}, Возраст: {self.age}, Спокоен: {self.is_calm}, Голоден: {self.is_hungry}"

    def calm_down(self):
        """Успокаивает ребёнка."""
        self.is_calm = True

    def feed(self):
        """Кормит ребёнка."""
        self.is_hungry = False


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []  # Список детей

    def add_child(self, child):
        """Добавляет ребёнка в список детей, если его возраст меньше на 16 лет, чем у родителя."""
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f"{child.name} добавлен(а) как ребёнок.")
        else:
            print(f"{child.name} слишком стар(а), чтобы быть ребёнком {self.name}.")

    def info(self):
        """Сообщает информацию о родителе и его детях."""
        info_str = f"Родитель: {self.name}, Возраст: {self.age}\nДети:\n"
        for child in self.children:
            info_str += f" - {child.info()}\n"
        return info_str

    def calm_child(self, child):
        """Успокаивает указанного ребёнка."""
        if child in self.children:
            child.calm_down()
            print(f"{self.name} успокоил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def feed_child(self, child):
        """Кормит указанного ребёнка."""
        if child in self.children:
            child.feed()
            print(f"{self.name} накормил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")


# Пример использования классов
parent = Parent("Иван", 40)
child1 = Child("Анна", 10)
child2 = Child("Сергей", 25)

# Добавляем детей родителю
parent.add_child(child1)  # Добавится успешно
parent.add_child(child2)  # Отказ из-за возраста

# Вывод информации о родителе и детях
print(parent.info())

# Успокоить и покормить ребёнка
parent.calm_child(child1)
parent.feed_child(child1)

# Проверка состояний ребёнка после действий
print(child1.info())
