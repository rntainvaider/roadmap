def get_tax(sum_salary: float):
    if 0 < sum_salary < 10_000:
        return sum_salary * 13 / 100
    elif 10_000 <= sum_salary < 50_000:
        return 20 * (sum_salary - 10_000) / 100 + 10_000 * 13 / 100
    elif sum_salary >= 50_000:
        return 30 * (sum_salary - 50_000) / 100 + 20 * (50_000 - 10_000) / 100 + 10_000 * 13 / 100

if __name__ == "__main__":
    sum_salary = float(input("Введите сумму зарплата без налога: "))
    print(get_tax(sum_salary))