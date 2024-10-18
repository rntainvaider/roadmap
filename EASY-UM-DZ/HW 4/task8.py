def housewarming(price: int, square: int):
    if square >= 100 and 7_000_000 <= price < 10_000_000:
        return f"Квартира подходит. Сумма {price}, {square} кв."
    elif 80 <= square < 100 and 0 < price < 7_000_000:
        return f"Квартира подходит. Сумма {price}, {square} кв."
    else:
        return "Квартира не подходит!"

if __name__ == "__main__":
    price = float(input("Введите стоимость квартиры: "))
    square = float(input("Введите количество квадратов: "))
    print(housewarming(price, square))