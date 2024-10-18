def get_max_num():
    numbers = []
    for _ in range(3):
        number = int(input("Введите число: "))
        numbers.append(number)

    max_number = 0
    for num in numbers:
        if num > max_number:
            max_number = num

    return f"Максимальное число {max_number}"

if __name__ == "__main__":
    print(get_max_num())