import time


def timer(func) -> None:
    def wrapper_function(*args, **kwargs) -> None:
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print(f"Время работы функции {stop - start}")

    return wrapper_function


@timer
def double() -> None:
    result = 0
    for _ in range(1000):
        result += sum([j**2 for j in range(10000)])
    print(result)
    return result


@timer
def triple(m) -> None:
    result = 0
    for _ in range(1000):
        result += sum([j**3 for j in range(m)])
    print(result)
    return result


double()
triple(22)
