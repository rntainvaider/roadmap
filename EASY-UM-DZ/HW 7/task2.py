def get_debt(count_debtors: int):
    total_sum_debt = 0
    for item in range(0, count_debtors + 1, 5):
        print(f"Должник с номером {item}")
        sum_debt = int(input("Сколько должны? "))
        total_sum_debt += sum_debt
    return f"Общая сумма долга: {total_sum_debt}"
count_debtors = int(input("Введите количество должников: "))
print(get_debt(count_debtors))