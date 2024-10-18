from random import randint

def games_guess_the_number():
    guess_a_number = randint(1, 10)
    count = 0
    while True:
        number = int(input("Введите число: "))
        if number > guess_a_number:
            count += 1
            print("Число больше, чем нужно. Попробуйте ещё раз!")
        elif number < guess_a_number:
            count += 1
            print("Число меньше, чем нужно. Попробуйте ещё раз!")
        else:
            count += 1
            print(f"Вы угадали! Число попыток: {count}")
            break

games_guess_the_number()