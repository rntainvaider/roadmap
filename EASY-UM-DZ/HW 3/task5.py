def get_modulus_number(number: int):
    return abs(number)


if __name__ == "__main__":
    number = int(input("Введите число: "))
    print(get_modulus_number(number))