def get_average_on_the_segment(a: int, b: int, c: int):
    summa_numbers = 0
    count_numbers = 0
    for item in range(a, b + 1):
        if item % c == 0:
            summa_numbers += item
            count_numbers += 1
    
    arithmetic_mean = summa_numbers / count_numbers

    return arithmetic_mean

a = int(input("Введите начало отрезка: "))
b = int(input("Введите конец отрезка: "))
c = int(input("Введите кратность чисел отрезку: "))
print(get_average_on_the_segment(a, b, c))