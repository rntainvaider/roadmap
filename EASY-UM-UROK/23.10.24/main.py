def decorator(func):  # Декоратор
    def wrapper(name) -> None:  # Оберточная функции
        print("Добрый день!")
        func()
        print(f"Еще что-нибудь!")

    return wrapper


@decorator
def say_hello(func) -> None:
    print(f"Привет!, {name}")


@decorator
def say_french_hello() -> None:
    print("Салют!")


say_hello("Алексей")
