def get_wages(hours: int, loan_balance: int, food: int):
    wages = (200 * hours) / (2 ** 3) + hours
    sum_food_and_loan_balance = loan_balance + food
    if wages >= sum_food_and_loan_balance:
        return "Часов хватает.Можно отдохнуть."
    else:
        return "Часов не хватает. Придётся поработать!"

if __name__ == "__main__":
    hours = int(input("Введите отработанные часы: "))
    loan_balance = int(input("Введите остаток по кредиту: "))
    food = int(input("Введите траты на еду: "))
    print(get_wages(hours, loan_balance, food))