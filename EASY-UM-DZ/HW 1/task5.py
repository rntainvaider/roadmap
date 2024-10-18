def get_clock():
    quantity_minutes = int(input("Введите количество минут: "))
    clock = quantity_minutes // 60
    minutes = quantity_minutes % 60
    return f"Часов: {clock}, минут: {minutes}"

if __name__ == "__main__":
    print(get_clock())