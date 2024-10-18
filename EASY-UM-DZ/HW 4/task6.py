def foolproof(number: int):
    if -99 <= number <= -10 or 10 <= number <= 99:
        return f"Число {number} двухзначное"
    else:
        return f"Чиисло {number} не двухзначное"

if __name__ == "__main__":
    number = int(input("Введите двухзначное число: "))
    print(foolproof(number))