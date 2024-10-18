def collectors(name: str, dent_amount: int):
    print(f"{name}, ваша задолженность состовляет {dent_amount} рублей.")
    flag = True
    while flag:
        n = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
        if n < dent_amount:
            print(f"Маловато, {name}. Давайте ещё раз")
        else:
            print(f"Отлично, {name}! Вы погасили долг. Спасибо!")
            flag = False

name = input("Введите ваше имя: ")
dent_amount = int(input("Введите сумму долга: "))
collectors(name, dent_amount)