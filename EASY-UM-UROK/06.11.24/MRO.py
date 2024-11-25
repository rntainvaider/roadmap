class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, place) -> None:
        super().__init__(name, age)
        self.place = place

    def action(self) -> None:
        print("Студент учится")


class Employer(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.place = place

    def action(self) -> None:
        print("Сотрудник работает")


class Citizen(Student, Person):
    pass


citizen = Citizen("Ivan", 33, "Kremle")
citizen.action()
