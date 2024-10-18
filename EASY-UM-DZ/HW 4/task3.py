def function(x: int):
    if x > 0:
       return x - 12
    elif x == 0:
        return 5
    elif x < 0:
        return x ** 2

if __name__ == "__main__":
    x = int(input("Введите число: "))
    print(function(x))