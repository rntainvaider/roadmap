import time


def timer(func) -> None:
    start = time.time()
    func()
    stop = time.time()
    print(stop - start)


def double() -> None:
    result = 0
    for _ in range(1000):
        result += sum([j**2 for j in range(10000)])
    print(result)
    return result


def coube(m) -> None:
    result = 0
    for _ in range(1000):
        result += sum([j**3 for j in range(m)])
    print(result)


timer(double)
