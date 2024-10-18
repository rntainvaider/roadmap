def get_even_positive_numbers():
    count_numbers = 0
    for _ in range(1, 11):
        numb = int(input("Введи число: "))
        if numb % 2 == 0 and numb > 0:
            count_numbers += 1

    return f"Cколько чисел являются одновременно чётными и положительными {count_numbers}"

print(get_even_positive_numbers())