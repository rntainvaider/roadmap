def numbers_big(numbers: int):
    count = 0
    for _ in str(numbers):
        count += 1
    return f"Количество десятичных цифр в водимом числе: {count}"

numbers = int(input("Ввести число для считывания десятичных цифр: "))
print(numbers_big(numbers))