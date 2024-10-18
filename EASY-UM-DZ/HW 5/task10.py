from random import randint

def games_guess_the_number():
    _ = int(input("Загадайте число от 1 до 10: "))
    count = 0
    while True:
        number_selection = randint(1, 10)
        numb = int(input(f"Твоё число равно, меньше или больше, чем число {number_selection}?\nгде  1 — равно, 2 — больше, 3 — меньше: "))
        if numb == 1:
            count += 1
            print(f"Вы угадали! Число попыток: {count}")
            break
        elif numb == 2:
            count += 1
            continue
        elif numb == 3:
            count += 1
            continue

games_guess_the_number()