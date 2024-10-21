from threading import Thread
from random import randint
from time import sleep
from sympy import isprime
from math import factorial

input_file_path = input("Введите путь к файлу\n")

def random_numbers(input_file_path: str) -> None:
    with open(input_file_path, 'w', encoding='UTF-8') as file:
        for _ in range(10):
            numb = randint(1, 50)
            print(f"Записываем случайное число {numb} в файл {input_file_path}")
            file.write(f"{str(numb)}\n")
            sleep(1)

def finding_a_prime_number(file_path: str, output_path: str) -> None:
    with open(file_path, 'r', encoding='UTF-8') as file:
        numbers = [int(item.strip()) for item in file.readlines()]
        for numb in numbers:
            print(f"Ищем простое число {numb}")
            sleep(1)

        primes = [num for num in numbers if isprime(num)]
        for number in primes:
            print(f"Нашли простое число {number}")
            sleep(1)

    with open(output_path, 'a', encoding='UTF-8') as file:
        for item in primes:
            file.write(f"{str(item)} - простое число\n")

def finding_the_factorial_of_a_number(file_path: str, output_path: str) -> None:
    with open(file_path, 'r', encoding='UTF-8') as file:
        numbers = [int(item.strip()) for item in file.readlines()]
        for numb in numbers:
            print(f"Ищем факториал числа {numb}")
            sleep(1)

        factorials = {num: factorial(num) for num in numbers}

    with open(output_path, 'a', encoding='UTF-8') as file:
        for num, fact in factorials.items():
            file.write(f"Факториал {num} = {fact}\n")
            print(f"Нашли факториал числа {num} = {fact}")
            sleep(1)

thread1 = Thread(target=random_numbers(input_file_path))
thread2 = Thread(target=finding_a_prime_number(input_file_path, 'prime_numbers.txt'))
thread3 = Thread(target=finding_the_factorial_of_a_number(input_file_path, 'factorials_numbers.txt'))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
