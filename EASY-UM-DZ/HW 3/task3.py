"""1 Вариант, более сложнее"""
def use_dental_floss(month: str):
    month_and_count_days = {"Январь": 31, "Февраль": 29, "Март": 31, "Апрель": 30, 
                            "Май": 31, "Июнь": 30, "Июль": 31, "Август": 31, 
                            "Сентябрь": 30, "Октябрь": 31, "Ноябрь": 30, "Декабрь": 31}
    
    if month in month_and_count_days:
        day_dental_floss = int(input("Введите день использования зубной нити: "))
        if 0 < day_dental_floss <= month_and_count_days[month]:
            if day_dental_floss % 2 == 0:
                return "Сегодня четный день, используйте зубную нить!"
            else:
                return "Сегодня нечетный день, не используйте зубную нить!!!"
        else:
            return f"Такого дня не существует {day_dental_floss}!!!"
    else:
        return f"Такого месяца не существует {month}!!!"

if __name__ == "__main__":
    month = input("Введите название месяца: ")
    print(use_dental_floss(month))


"""2 Вариант, более простой"""
# def use_dental_floss(month: str, count_days:int):
#     days = list()
#     for day in range(1, count_days+1):
#         days.append(day)
#     day_dental_floss = int(input("Введите день использования зубной нити: "))
#     if 0 < day_dental_floss <= count_days:
#         if day_dental_floss % 2 == 0:
#             return "Сегодня четный день, используйте зубную нить!"
#         else:
#             return "Сегодня нечетный день, не используйте зубную нить!!!"
#     else:
#         return f"Такого дня не существует {day_dental_floss}!!!"

# if __name__ == "__main__":
#     month = input("Введите название месяца: ")
#     count_days = int(input("Введите количество дней в месяце: "))
#     print(use_dental_floss(month, count_days))