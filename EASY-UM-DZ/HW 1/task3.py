def get_next_and_previous():
    number = int(input("Введите число: "))
    return (f"После числа {number} идёт число {number + 1}\n"
            f"До числа {number} идёт число {number - 1}")

if __name__ == "__main__":
    print(get_next_and_previous())