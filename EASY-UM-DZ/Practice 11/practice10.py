from random import randint


nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3,
          16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12,
          9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

set_nums_1 = set()
set_nums_2 = set()

for num in nums_1:
    set_nums_1.add(num)

for num in nums_2:
    set_nums_2.add(num)

print(f"1-е множество: {set_nums_1}")
print(f"2-е множество: {set_nums_2}")
min_elem1 = min(set_nums_1)
min_elem2 = min(set_nums_2)

print(f"Минимальный элемент 1-го множества: {min_elem1} Минимальный элемент 2-го множества: {min_elem2}")

set_nums_1.remove(min(set_nums_1))
set_nums_2.remove(min(set_nums_2))

random_num_1 = randint(100, 200)
random_num_2 = randint(100, 200)
set_nums_1.add(random_num_1)
set_nums_2.add(random_num_2)

print(f"Случайное число для 1-го множества: {random_num_1} Случайное число для 2-го множества: {random_num_2}")

result = set_nums_1.union(set_nums_2)

print(f"Объединение множеств: {sorted(result)}")

intersection_sets = set_nums_1.intersection(set_nums_2)

print(f"Пересечение множеств: {intersection_sets}")

difference_set = set_nums_2.difference(set_nums_1)

print(f"Элементы, входящие в nums_2, но не входящие в nums_1: {difference_set}")
