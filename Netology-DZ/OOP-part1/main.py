from statistics import mean

from course import Course
from gender import Gender
from lecturer import Lecturer
from reviewer import Reviewer
from student import Student


def get_average_homework_grade(students: list[Student], course: Course) -> float:
    return mean(
        mean(student.courses_grades[course])
        for student in students
        if course in student.courses_grades
    )


def get_average_lecture_grade(lecturers: list[Lecturer], course: Course) -> float:
    return mean(
        mean(lecturer.courses_grades[course])
        for lecturer in lecturers
        if course in lecturer.courses_grades
    )


students = [Student("John", "Conor", Gender.MALE), Student("Kate", "Black", Gender.FEMALE)]
lecturers = [Lecturer("Larisa", "Alexandrova"), Lecturer("Elena", "Maximova")]
reviewers = [Reviewer("Alex", "Gray"), Reviewer("Olivia", "Red")]

students[0].courses_in_progress.append(Course.PYTHON)
students[0].courses_in_progress.append(Course.MATH)
students[1].courses_in_progress.append(Course.BIOLOGY)
students[1].courses_in_progress.append(Course.PYTHON)
students[1].finished_courses.append(Course.PHYSICS)

lecturers[0].courses_attached.append(Course.PYTHON)
lecturers[0].courses_attached.append(Course.MATH)
lecturers[1].courses_attached.append(Course.BIOLOGY)

reviewers[0].courses_attached.append(Course.PYTHON)
reviewers[0].courses_attached.append(Course.MATH)
reviewers[1].courses_attached.append(Course.BIOLOGY)

students[0].rate_lecturer(lecturers[0], Course.PYTHON, 8)
students[0].rate_lecturer(lecturers[0], Course.MATH, 6)
students[1].rate_lecturer(lecturers[1], Course.BIOLOGY, 8)

reviewers[0].rate_homework(students[0], Course.PYTHON, 9)
reviewers[0].rate_homework(students[0], Course.MATH, 7)
reviewers[0].rate_homework(students[1], Course.PYTHON, 8)
reviewers[1].rate_homework(students[1], Course.BIOLOGY, 7)

TABLE_WIDTH = 60

print("=" * TABLE_WIDTH + "\n")
print(students[0])
print()
print(students[1])
print("\n" + "-" * TABLE_WIDTH + "\n")
if students[0] < students[1]:
    print(f"{students[0].get_full_name()} учится хуже чем {students[1].get_full_name()}.")
elif students[0] > students[1]:
    print(f"{students[0].get_full_name()} учится лучше чем {students[1].get_full_name()}.")
else:
    print(f"{students[0].get_full_name()} и {students[1].get_full_name()} учатся одинаково.")
print("\n" + "=" * TABLE_WIDTH + "\n")

print(lecturers[0])
print()
print(lecturers[1])
print("\n" + "-" * TABLE_WIDTH + "\n")
if lecturers[0] < lecturers[1]:
    print(f"{lecturers[0].get_full_name()} преподает хуже чем {lecturers[1].get_full_name()}.")
elif lecturers[0] > lecturers[1]:
    print(f"{lecturers[0].get_full_name()} преподает лучше чем {lecturers[1].get_full_name()}.")
else:
    print(f"{lecturers[0].get_full_name()} и {lecturers[1].get_full_name()} преподают одинаково.")
print("\n" + "=" * TABLE_WIDTH + "\n")

print(reviewers[0])
print()
print(reviewers[1])

print("\n" + "=" * TABLE_WIDTH + "\n")

course = Course.PYTHON
grade = get_average_homework_grade(students, course)
print(f"Средняя оценка за дз по всем студентам в рамках курса '{course}': {grade}.")

course = Course.PYTHON
grade = get_average_lecture_grade(lecturers, course)
print(f"Средняя оценка за лекции всех лекторов в рамках курса '{course}': {grade}.")

print("\n" + "=" * TABLE_WIDTH)
