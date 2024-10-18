def get_salary_for_the_year() -> float:
    month = 1
    sum_salary_for_the_year = 0
    for _ in range(1, 13):
        salary_for_the_month = int(input(f"Введите зарплату за {month} месяц\t"))
        sum_salary_for_the_year += salary_for_the_month
        month += 1

    average_salary_per_year = sum_salary_for_the_year / month

    return round(average_salary_per_year, 3)

print(get_salary_for_the_year())