class Student:
    def __init__(self, last_name: str, first_name: str, group_number: int,
academic_performance: int) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.group_number = group_number
        self.academic_performance = academic_performance

def append_students_in_list() -> None:
    students = list()
    for _ in range(1):
        last_name = input("Введите имя: ")
        first_name = input("Введите фамилию: ")
        group_number = int(input("Введите номер группы: "))
        academic_performance = list(map(int, input("Введите оценки через пробел: ").split()))
        students.append(Student(last_name, first_name, group_number, academic_performance))
    return students

append_students_in_list()


# class ListStudents:
#     def __init__(self) -> None:
#         self.list_students = []

#     def __str__(self) -> str:
#         return f"[{self.list_students}]"

#     def append_students_in_list(self) -> None:
#         for _ in range(2):
#             last_name = input("Введите имя: ")
#             first_name = input("Введите фамилию: ")
#             group_number = int(input("Введите номер группы: "))
#             academic_performance = list(map(int, input("Введите оценки через пробел: ").split()))
#             self.list_students.append(Student(last_name, first_name, group_number, academic_performance))

# students = ListStudents()
# students.append_students_in_list()
# print(students)
