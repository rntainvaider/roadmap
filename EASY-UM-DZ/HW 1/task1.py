def get_result(a=8, b=10, c=12, d=18):
    res = ((-3 + a ** 2) * b - 2 ** 3) / c - 2 * d
    return round(res, 2)

if __name__ == "__main__":
    print(get_result())