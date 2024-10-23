# Ваша задача: создать декоратор check_address, который будет проверять,
# входит ли адрес в список допустимых адресов (например, внутри города).
# Если адрес некорректный, декоратор должен выводить сообщение об ошибке и не вызывать исходную функцию order_taxi.


def check_address(func) -> None:
    def wrapper(address) -> None:
        allowed_addresses = ["пр.Ленина, дом 22", "пр.Ленина, дом 25", "ул.Энгельса, дом 17"]
        if address in allowed_addresses:
            func(address)
        else:
            print(f"Неверный адрес! Вот список допустимых адресов: {allowed_addresses}")

    return wrapper


@check_address
def order_taxi(address) -> None:
    print("Такси вызвано!")


order_taxi("ул. Лесная, дом 43")
order_taxi("пр.Ленина, дом 25")
