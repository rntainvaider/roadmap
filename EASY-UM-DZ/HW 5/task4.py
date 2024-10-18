def get_count_even_numbers():
    count_even_numbers = 0
    while True:
        numb = int(input("Введите число (последовательность заканчивается при вводе нуля)\n"))
        if numb == 0:
            break
        elif numb % 2 == 0:
            count_even_numbers += 1

    return f"Количество чётных чисел в последовательности {count_even_numbers}"

print(get_count_even_numbers())