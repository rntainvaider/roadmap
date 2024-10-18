def get_number_replace():
    number = int(input("Введите четырехзначное число: "))
    if len(str(number)) == 4:
        number_replace = str(number)[::-1]
        num_one = number // 1000 % 10
        num_two = number // 100 % 10
        num_fhree = number // 10 % 10
        num_four = number % 10
        return (f"Число в обратном порядке при помощи срезов: {number_replace}\n"
            f"Число в обратном порядке при помощи арифметики: {num_four}{num_fhree}{num_two}{num_one}")
    else:
        return f"Число '{number}' не является четырехзначным"

if __name__ == "__main__":
    print(get_number_replace())