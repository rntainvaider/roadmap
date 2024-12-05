"""Вы работаете со сторонним кодом, который иногда может возвращать некорректные значения.

Ваша задача: Создайте декоратор ensure_result_is_number, который будет возвращать None,
если значение функции не является числом, иначе — возвращать результат работы функции."""

import random


def ensure_result_is_number(func):
    def wrapper(*args, **kwars):
        res = func(*args, **kwars)
        if str(res).isdigit():
            return res
        return None

    return wrapper


@ensure_result_is_number
def test_function():
    return random.choice(["Passed", 10, "Failed", 5.5])


# Функция вернула не int и не float
print(test_function())
# None

# Функция вернула float
print(test_function())
# 5.5

# Функция вернула int
print(test_function())
# 10
