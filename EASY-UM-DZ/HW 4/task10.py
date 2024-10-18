def get_post_office_hours(hours: int) -> str:
    if 0 <= hours <= 23:
        if 14 <= hours <= 15 or 10 <= hours <= 12 or 18 <= hours <= 20 or 22 <= hours <= 23 or 0 <= hours <= 7:
            return "Посылку получить нельзя"
        else:
            return "Можно получить посылку"
    else:
        return f"Неправильный формат времени {hours}. Нужно вводить от 0 до 23!"

hours = int(input("Введите время работы почты в часах: "))
print(get_post_office_hours(hours))