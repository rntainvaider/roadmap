str_1 = input()
str_2 = input()


def get_tuple(string_1: str, string_2: str) -> tuple[list[str], list[str]]:
    list_1 = string_1.split()
    list_2 = string_2.split()
    return list_1, list_2


def get_dict(func):
    def wrapper(*args) -> dict[str, str]:
        res = func(*args)
        dict_str = dict()
        for key, value in zip(res[0], res[1]):
            dict_str[key] = value
        return dict_str

    return wrapper


get_tuple = get_dict(get_tuple)
d = get_tuple(str_1, str_2)
print(*sorted(d.items()))
