import datetime


# Декоратор логгера
def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            # Логирование вызова функции
            call_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = old_function.__name__
            arguments = f"args: {args}, kwargs: {kwargs}"
            result = old_function(*args, **kwargs)
            log_message = (
                f"[{call_time}] Function '{func_name}' called with {arguments}\n"
                f"Returned: {result}\n"
            )
            with open(path, "a", encoding="utf-8") as log_file:
                log_file.write(log_message)
            return result

        return new_function

    return __logger


# Приложение-калькулятор
class Calculator:
    def __init__(self):
        self.log_path = "calculator.log"

    @logger("calculator.log")
    def add(self, a, b):
        """Сложение"""
        return a + b

    @logger("calculator.log")
    def subtract(self, a, b):
        """Вычитание"""
        return a - b

    @logger("calculator.log")
    def multiply(self, a, b):
        """Умножение"""
        return a * b

    @logger("calculator.log")
    def divide(self, a, b):
        """Деление"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b


# Тестирование приложения
if __name__ == "__main__":
    calculator = Calculator()

    # Выполняем арифметические операции
    print("Addition: ", calculator.add(10, 5))
    print("Subtraction: ", calculator.subtract(10, 5))
    print("Multiplication: ", calculator.multiply(10, 5))
    print("Division: ", calculator.divide(10, 5))

    # Пример ошибки
    try:
        calculator.divide(10, 0)
    except ValueError as e:
        print("Error: ", e)

    # Проверяем содержимое лога
    with open("calculator.log", "r", encoding="utf-8") as log_file:
        print("\nLogs:")
        print(log_file.read())
