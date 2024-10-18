def fruit_crisis() -> None:
    incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
    }

    min_key = min(incomes, key=incomes.get)
    min_value = incomes[min_key]
    sum_value = sum(incomes.values())

    incomes.pop(min_key)

    print(f"Общий доход за год составил {sum_value} рублей")
    print(f"Самый маленький доход у {min_key}. Он составляет {min_value} рублей")
    print(incomes)

fruit_crisis()
