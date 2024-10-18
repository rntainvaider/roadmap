from random import randint
from threading import Thread
import time

class Task:
    def __init__(self) -> None:
        self.random_numbers = list()
        self.average = 0
        self.summa = 0

    def ran_num(self) -> None:
        for _ in range(10):
            numb = randint(1, 10)
            self.random_numbers.append(numb)
            print(f"Формируем список - {numb}")
            time.sleep(1)
        print(f"Список - {self.random_numbers}")

    def sum_list(self) -> None:
        self.summa = sum(self.random_numbers)
        print(f"Cумму списка - {self.summa}")

    def average_list(self) -> None:
        self.average = sum(self.random_numbers) / len(self.random_numbers)
        print(f"Cреднеарифметическое списка - {self.average}")

task = Task()

t1 = Thread(target=task.ran_num)
t2 = Thread(target=task.sum_list)
t3 = Thread(target=task.average_list)

t1.start()
t1.join()

t2.start()
t3.start()
