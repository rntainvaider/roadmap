def input_numbers() -> list[int]:
    return list(map(int, input("Введите числа через пробел: ").split()))


class Numbers:
    def __init__(self, numbers: list[int]) -> None:
        self._numbers = numbers

    def get_numbers(self, *, reversed_: bool = False) -> list[int]:
        if reversed_:
            return self._numbers[::-1]
        return self._numbers

    def append(self, number: int) -> None:
        self._numbers.append(number)

    def remove(self, value: int) -> None:
        self._numbers[:] = [number for number in self._numbers if number != value]

    def replace(self, number_old: int, number_new: int, *, only_first: bool) -> None:
        if only_first:
            self._numbers[self._numbers.index(number_old)] = number_new
        else:
            self._numbers[:] = [
                number_new if number == number_old else number for number in self._numbers
            ]

    def contains(self, number: int) -> bool:
        return number in self._numbers


MENU = """
1. Добавить новое число в список
2. Удалить число из списка
3. Показать содержимое списка
4. Проверить есть ли значение в списке
5. Заменить значения в списке
6. Выход
"""


def main() -> None:
    numbers = Numbers(input_numbers())
    while True:
        print(MENU)
        choice = int(input("Выберите операцию: "))
        if choice == 1:
            number_new = int(input("Введите число: "))
            if numbers.contains(number_new):
                print("Такое число есть в списке!")
            else:
                numbers.append(number_new)
        elif choice == 2:
            number_pop = int(input("Введи число для удаления: "))
            if numbers.contains(number_pop):
                numbers.remove(number_pop)
            else:
                print("Такого числа нет в списке!")
        elif choice == 3:
            print("1. Вывести с начала?\n2. Вывести с конца?")
            choice = int(input("Выберите операцию: "))
            if choice == 1:
                print(numbers.get_numbers())
            elif choice == 2:
                print(numbers.get_numbers(reversed_=True))
        elif choice == 4:
            number = int(input("Введи число для проверки: "))
            if numbers.contains(number):
                print("Есть значение в списке!")
            else:
                print("Нет значения в списке!")
        elif choice == 5:
            number_old = int(input("Введите число которое хотите заменить: "))
            if not numbers.contains(number_old):
                print("Такого числа нет в списке!")
                continue
            number_new = int(input("Введите число которым хотите заменить: "))
            print("1. Только первое вхождение?\n2. Все вхождения?")
            choice = int(input("Выберите операцию: "))
            if choice == 1:
                numbers.replace(number_old, number_new, only_first=True)
            elif choice == 2:
                numbers.replace(number_old, number_new, only_first=False)
        elif choice == 6:
            break


main()
