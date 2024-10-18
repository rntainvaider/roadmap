def please_rate():
    count_positive_number = 0
    count_negative_number = 0
    while True:
        print("0 - выйти из программы")
        number = int(input("Введите число: "))
        if -100 <= number <= 100:
            if 0 < number <= 100:
                count_positive_number += 1
            elif -100 <= number < 0:
                count_negative_number += 1
            elif number == 0:
                break
        else:
            print(f"Число не входит в диапазoн -100 - 100!!!")
            continue

    return (f"Кол-во положительных чисел: {count_positive_number}\n"
        f"Кол-во отрицательных чисел: {count_negative_number}")

print(please_rate())