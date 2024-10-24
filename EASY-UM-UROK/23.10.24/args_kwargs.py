def f1(*args) -> None:
    print(args)


def f2(**kwargs) -> None:
    print(kwargs)


def f3(func, *args, **kwargs) -> None:
    print(*args)
    print(**kwargs)
    func()


f1(1, 2, 3, 4, 5, 6, 7)
f2(name="Denis", age=22, weight=88)
f3(say_hello, 1, 2, 3, 4, 5, 6, 7, name="Denis", age=24)
