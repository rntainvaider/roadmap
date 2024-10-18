def segment(a: int, b: int, c: int):
    for item in range(a, b + 1, c):
        y = (item ** 3) + (2 * item ** 2) - (4 * item - 1)
        print(f"В точке {item} функция равна {y}")

a = int(input("Введите начало отрезка: "))
b = int(input("Введите конец отрезка: "))
c = int(input("Введите шаг: "))
segment(a, b, c)