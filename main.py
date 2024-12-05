def decorator(func):
    def wrapper(*args, **kwargs):
        print("Отработал декоратор")
        res = func(*args, **kwargs)
        return res

    return wrapper


@decorator
def demo_func():
    print("Отработала оригинальная функция")
