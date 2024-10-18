def get_factorial(numb: int) -> int:
    factorial = 1
    for item in range(1, numb+1):
        factorial *= item

    return f"Факториал числа {numb} равен {factorial}"

numb = int(input("Введите число: "))
print(get_factorial(numb))