def get_dict_square_of_the_number(num: int) -> dict[int, int]:
    dict_square_of_the_number = dict()

    for item in range(1, num + 1):
        dict_square_of_the_number[item] = item ** 2

    return dict_square_of_the_number

print(get_dict_square_of_the_number(5))
