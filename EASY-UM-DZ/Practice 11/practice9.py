strings = input("Введите строку: ")
symbols = {'.', ',', ';', ':', '!', '?'}

count = 0
for i in strings:
    for j in symbols:
        if i == j:
            count += 1

print(f"Количество знаков пунктуации: {count}")
