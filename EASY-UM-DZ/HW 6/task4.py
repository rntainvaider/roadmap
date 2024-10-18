def caring_for_nature():
    number_of_violations = 0
    sector_num = 30
    for _ in range(30, 36):
        sector = int(input(f"Людей в {sector_num} секторе: "))
        sector_num += 1
        if 0 <= sector <= 10:
            print("Всё спокойно.")
        else:
            number_of_violations += 1
            print("Нарушение! Слишком много людей в секторе!")

    return f"Количество нарушений: {number_of_violations}"

print(caring_for_nature())
