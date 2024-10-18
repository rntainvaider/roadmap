def get_character_level(experience: int):
    if 0 <= experience < 1000:
        return "Ваш уровень: 1"
    elif 1000 <= experience < 2500:
        return "Ваш уровень: 2"
    elif 2500 <= experience < 5000:
        return "Ваш уровень: 3"
    elif 5000 <= experience:
        return "Ваш уровень: 4"

if __name__ == "__main__":
    experience = int(input("Введите количество опыта: "))
    print(get_character_level(experience))