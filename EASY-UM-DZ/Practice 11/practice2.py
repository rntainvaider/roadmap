def students(student: str) -> None:
    data = student.split()

    information_student = {
        "Имя": data[0],
        "Фамилия": data[1],
        "Город": data[2],
        "Место учёбы": data[3],
        "Оценки": list(map(int, data[4:]))
    }

    print("Результат:")
    for key, value in information_student.items():
        print(f"{key} - {value}")


student = input("Введите данные студента через пробел имя, фамилия, город, место учёбы, оценки\n")
students(student)
