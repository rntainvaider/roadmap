# class Animal:
#     """Демонстрация статических и классовых методов"""

#     total_animals = 0

#     def __init__(self, name, species) -> None:
#         self.name = name
#         self.species = species
#         Animal.total_animals += 1

#     @staticmethod
#     def describe_animal(name, species) -> None:
#         """Статистический метод для описания животных"""
#         print(f"Это {species} по имени {name}")

#     @classmethod
#     def create_animal(cls, name, species) -> None:
#         """Классовый метод для создания животных, имеет доступ к атрибутам класса"""
#         return cls(name, species)


# cat = Animal("рыжик", "кот")
# Animal.describe_animal("рыжик", "кот")


print(-47 % (-8))
