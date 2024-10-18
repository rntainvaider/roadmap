def get_points():
    russian_language = int(input("Введите количество баллов по русскому языку: "))
    mathematics = int(input("Введите количество баллов по математике: "))
    informatics = int(input("Введите количество баллов по информатике: "))
    count_points = russian_language + mathematics + informatics
    if 0 < russian_language < 100 and 0 < mathematics < 100 and 0 < informatics < 100:
        if 270 <= count_points <= 300:
            return f"Поздравляю, ты поступил на бюджет! Количество ваших баллов {count_points}"
        else:
            return f"К сожалению, ты не прошёл на бюджет. Количество ваших баллов {count_points}"
    else:
        return "Число ваших баллов не соответсвует диапазону!!!"

if __name__ == "__main__":
    print(get_points())