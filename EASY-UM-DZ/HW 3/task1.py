def get_weather():
    number = int(input("На улице идет дождь? Введите число: 1 - Идёт дождь, 0 - дождь не идёт.\n"))
    if 0 <= number <= 1:
        if number == 1:
            return "Пошёл дождь. Возьмите зонтик!"
        else:
            return "На улице нет дождя."
    else:
        return "Неправильно введено число!"
    
if __name__ == "__main__":
    print(get_weather())