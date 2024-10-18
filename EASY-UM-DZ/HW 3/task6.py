import random
def dice_game(throw: str):
    if throw == "да":
        one_throw = random.randint(1, 6)
        two_throw = random.randint(1, 6)
        sum_throw = one_throw + two_throw

        data = f"Кубик Кости: {one_throw}\nКубик владельца: {two_throw}\nСумма: {sum_throw}"

        if one_throw >= two_throw:
            return (f"{data}\nКостя платит\nИгра окончена")
        else:
            return f"{data}\nВладелец платит\nИгра окончена"
        
    elif throw == "нет":
        return "Игра окончена досрочно"

if __name__ == "__main__":
    throw = input("Костя, бросик кубик? Да/Нет?\n").lower()
    print(dice_game(throw))