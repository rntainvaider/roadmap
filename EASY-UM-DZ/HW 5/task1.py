def get_cubes_of_numbers(number: int):
    lst_cubes_of_number = list()
    for item in range(1, number + 1):
        result = item ** 3
        lst_cubes_of_number.append(f"{item} ** 3 = {result}")
    return "\n".join(lst_cubes_of_number)

number = int(input("Введите число по которое вы хотите получить кубы чисел: "))
print(get_cubes_of_numbers(number))