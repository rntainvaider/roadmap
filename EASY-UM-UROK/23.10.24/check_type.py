# 3. Проверка типа данных:Реализуйте декоратор `check_type`,
# который будет проверять тип аргументов функции и поднимать исключение,
# если они не соответствуют заданным.


def check_type(func) -> None:
    def wrapper(n) -> None:
        if isinstance(n, int):
            double(n)
        else:
            print("Тип данных не соответствует")

    return wrapper


@check_type
def double(n):
    print(n**2)
    return number**2
