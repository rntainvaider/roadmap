def check_age(age: int):

    if age >= 18:
        result = "Доступ разрешён"
    else:
        result = "Доступ запрещён"

    return result


def get_cost(weight: int):
    if weight <= 10:
        return "Стоимость доставки: 200 руб."
    else:
        return "Стоимость доставки: 500 руб."


def check_auth(login: str, password: str):

    if login == "admin" and password == "password":
        result = "Добро пожаловать"
    else:
        result = "Доступ ограничен"
    return result
