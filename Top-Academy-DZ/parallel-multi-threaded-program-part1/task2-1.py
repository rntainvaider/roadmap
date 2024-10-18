from random import randint
from threading import Thread

name_file = "random_numbers.txt" #input("Введите название файла и расширение\n")

class GenerateAFileWithNumbers:
    def __init__(self) -> None:
        self.random_numbers = list()

    def generate_random_numbers(self) -> None:
        for _ in range(1, 10):
            random_number = randint(1, 10)
            self.random_numbers.append(str(random_number))

    def write_numbers_to_file(self, name_file: str) -> None:
        with open(name_file, 'w+') as file:
            file.writelines(f"{number}\n" for number in self.random_numbers)

# class PrimeNumbers:
#     def __init__(self) -> None:
#         self.prime_numb = list()

#     def read_file_with_numbers(self) -> None:
#         with open(name_file, 'r') as file:
#             f = file.read()
#             for number in f:
#                 print(number)

#     def get_prime_numbers(self):
#         ...

generate_a_file_with_numbers = GenerateAFileWithNumbers()

generate_a_file_with_numbers.generate_random_numbers()
# generate_a_file_with_numbers.write_numbers_to_file(name_file)

# prime_numbers = PrimeNumbers()
# print(prime_numbers.read_file_with_numbers())

t1 = Thread(target=generate_a_file_with_numbers.write_numbers_to_file(name_file))

t1.start()
t1.join()
