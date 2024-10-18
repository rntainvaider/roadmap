def get_numbers():
    number = int(input("Введите четырехзначное число: "))
    if len(str(number)) == 4:
        one_num = number // 1000 % 10
        two_num = number // 100 % 10
        fhree_num = number // 10 % 10
        four_num = number % 10
        
        return f"Каждая цифра в от{one_num} {two_num} {fhree_num} {four_num}"
    else:
        return "Это не четырехзначное число!!!"

if __name__ == "__main__":
    print(get_numbers())