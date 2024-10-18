def check_accountant(number_one, number_two):
    one_category = number_one % 100
    two_category = number_two % 100
    sum_category = one_category + two_category
    return f"Сумма: {sum_category}"


if __name__ == "__main__":
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    print(check_accountant(number_one, number_two))