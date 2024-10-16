def even_numbers(n: int):
    for number in range(n):
        if number % 2 == 0:
            yield number


def ood_numbers(n: int):
    for number in range(n):
        if number % 2 != 0:
            yield number


def all_type_numbers(n: int):
    yield from even_numbers(n)
    yield from ood_numbers(n)


for number in all_type_numbers(20):
    print(number)

# numbers = even_numbers(10)
# print(numbers.__next__())
# print(numbers.__next__())
# print(numbers.__next__())
