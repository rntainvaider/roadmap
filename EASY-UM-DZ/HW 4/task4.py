def admission_to_university(place_in_list: int, count_points: int):
    if 1 <= place_in_list <= 10 and count_points >= 290:
        return "Поздравляем, вы поступили!\nБонусом вам будет начисляться стипендия."
    elif 1 <= place_in_list <= 10 and 108 <= count_points < 290:
        return "Поздравляем, вы поступили!\nНо вам не хватило баллов для стипендии."
    elif place_in_list > 10 or count_points < 108:
        return "К сожалению, вы не поступили."
        
if __name__ == "__main__":
    place_in_list = int(input("Введите место в списке поступающих: "))
    count_points = int(input("Введите количество баллов за экзамены: "))
    print(admission_to_university(place_in_list, count_points))