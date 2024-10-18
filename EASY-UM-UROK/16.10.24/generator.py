def double(n: int) -> None:
    for i in range(n):
        print(i**2)


# def double_generator(n: int) -> list[int]:
# return [i**2 for i in range(n)]

double_generator = (i**2 for i in range(10))


double(10)
print(double_generator.__next__())
print(double_generator.__next__())
print(double_generator.__next__())
