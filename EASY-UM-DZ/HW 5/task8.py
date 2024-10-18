import math

def get_contribution(x, y, p):
    summa = x
    count_month = 0
    while True:
        s = (summa * p / 100)
        summa += math.floor(s)
        count_month += 1
        if summa >= y:
            break
    year = 36 // 12
    month = 36 % 12
    return f"Через {year} года и {month} месяцев получится данная сумма {y}"

x = int(input("Введите сумму вклада: "))
y = int(input("Введите сумму которую вы хотите получить: "))
p = int(input("Введите процент вклада: "))
print(get_contribution(x, y, p))
