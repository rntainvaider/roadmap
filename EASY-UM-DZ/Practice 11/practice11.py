stroka = input("Введите строку: ")
numbers_stroki = set()

for item in stroka:
    if item.isdigit():
        numbers_stroki.add(item)

print(f"Различные цифры строки: {''.join(sorted(numbers_stroki))}")
