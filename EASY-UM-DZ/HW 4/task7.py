import random

def games():
    numbers = list()
    count = 3
    while count > 0:
        number = random.randint(1, 5)
        numbers.append(number)
        count -= 1
        print(number)
    if numbers[0] == numbers[1] == numbers[2]:
        return "Все числа совпадают"
    elif numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[1] == numbers[2]:
        return "Два числа совпадает"
    else:
        return "Все числа разные"

if __name__ == "__main__":
    print(games())