from collections import defaultdict
from statistics import mean
from typing import Self

from course import Course
from gender import Gender
from lecturer import Lecturer


class Student:
    def __init__(self, name: str, surname: str, gender: Gender) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = list[Course]()
        self.courses_in_progress = list[Course]()
        self.courses_grades = defaultdict[Course, list[int]](list)

    def __str__(self) -> str:  # pyright: ignore[reportImplicitOverride]
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self._get_average_grade()}\n"
            f"Курсы в процессе изучения: {self._get_courses_in_progress()}\n"
            f"Завершенные курсы: {self._get_finished_courses()}"
        )

    def __eq__(self, other: object) -> bool:  # pyright: ignore[reportImplicitOverride]
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._get_average_grade() == other._get_average_grade()

    def __lt__(self, other: Self) -> bool:
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other: Self) -> bool:
        return self._get_average_grade() <= other._get_average_grade()

    def __gt__(self, other: Self) -> bool:
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other: Self) -> bool:
        return self._get_average_grade() >= other._get_average_grade()

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def rate_lecturer(self, lecturer: Lecturer, course: Course, grade: int) -> None:
        if grade < 0 or grade > 10:
            raise ValueError("grade should be in range [0, 10]")  # noqa: TRY003
        if course not in lecturer.courses_attached:
            raise ValueError("lecturer should be attached to the course")  # noqa: TRY003
        if course not in self.courses_in_progress:
            raise ValueError("student should be enrolled for the course")  # noqa: TRY003
        lecturer.courses_grades[course].append(grade)

    def _get_average_grade(self) -> float:
        if len(self.courses_grades) == 0:
            return -1
        return mean(mean(course_grades) for course_grades in self.courses_grades.values())

    def _get_courses_in_progress(self) -> str:
        if len(self.courses_in_progress) == 0:
            return "Отсутствуют"
        return ", ".join(self.courses_in_progress)

    def _get_finished_courses(self) -> str:
        if len(self.finished_courses) == 0:
            return "Отсутствуют"
        return ", ".join(self.finished_courses)
