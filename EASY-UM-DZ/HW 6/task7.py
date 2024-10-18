def segment(a, b):
    sum_numbers = 0
    count_numbers = 0
    for item in range(a, b + 1):
        if item % 3 == 0:
            sum_numbers += item
            count_numbers += 1

    arithmetic_mean = sum_numbers / count_numbers

    return f"Средне арифметическое равно {arithmetic_mean}"

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(segment(a, b))