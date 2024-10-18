def get_list_assessments(count_assessments: int):
    list_assessments = list()
    for _ in range(1, count_assessments + 1):
        numb = int(input("Введите оценку: "))
        if 3 <= numb <= 5:
            list_assessments.append(numb)
        else:
            print("Оценка должна быть 3, 4 или 5!!!")

    count_fhree = 0
    count_four = 0
    count_five = 0
    
    for fhree in list_assessments:
        if fhree == 3:
            count_fhree += 1

    for four in list_assessments:
        if four == 4:
            count_four += 1

    for five in list_assessments:
        if five == 5:
            count_five += 1

    if count_fhree > count_four and count_fhree > count_five:
        return "Троек больше всего"
    elif count_four > count_fhree and count_four > count_five:
        return "Четверок больше всего" 
    elif count_five > count_fhree and count_five > count_four:
        return "Пятерок больше всего"
    elif count_fhree == count_four and count_fhree == count_five:
        return "Троек больше всего"
    elif count_four == count_fhree and count_four == count_five:
        return "Четверок больше всего" 
    elif count_five == count_fhree and count_five == count_four:
        return "Пятерок больше всего"


while True:
    count_assessments = int(input("Введите количество оценок: "))
    if count_assessments < 0:
        print("Отрицательным не может быть!!!")
    else:
        print(get_list_assessments(count_assessments))
        break