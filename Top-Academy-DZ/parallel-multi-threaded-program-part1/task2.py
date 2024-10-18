from random import randint
from threading import Thread
import time

class Task:
    def __init__(self) -> None:
        self.rand_numbers = list()
        self.prime_numbers = list()
        self.factorial_numbers = list()

    def fill_with_random_numbers(self, name_file: str) -> None:
        with open(name_file, 'w+') as file:
            for _ in range(10):
                ran_num = randint(1, 10)
                file.write(f"{str(ran_num)}\n")
                self.rand_numbers.append(ran_num)
                print(f"Заполняем файл случайными числами - {ran_num}")
                time.sleep(1)

        print(f"Сформированный список {self.rand_numbers}")

    def get_prime_numbers(self) -> None:
        for item in self.rand_numbers:
            print(f"Ищем простые числа {item}")
            time.sleep(1)
            if int(item) > 0:
                k = 0
                for i in range(1, item + 1):
                    if item % i == 0:
                        k += 1
                if k == 2:
                    self.prime_numbers.append(i)

        with open("prime_numbers.txt", 'w') as file:
            for item in self.prime_numbers:
                file.write(f"{str(item)}\n")

        print(f"Все простые числа списка - {self.prime_numbers}")

    def get_factorial_numbers(self) -> None:
        fac_numb = 1
        for number in self.rand_numbers:
            fac_numb = 1
            for numb in range(number, 0, -1):
                fac_numb *= numb
            self.factorial_numbers.append(fac_numb)
            print(f"Ищем факториал числа {number} = {fac_numb}")
            time.sleep(1)
        print(f"Сформированный список факториалов {self.factorial_numbers}")

        with open("factorial_numbers.txt", 'w') as file:
            for item in self.factorial_numbers:
                file.write(f"{str(item)}\n")

name_file = input("Введите название файла с расширением\n")

task = Task()

t1 = Thread(target=task.fill_with_random_numbers(name_file))
t2 = Thread(target=task.get_prime_numbers)
t3 = Thread(target=task.get_factorial_numbers)

t1.start()
t1.join()

t2.start()
t3.start()
