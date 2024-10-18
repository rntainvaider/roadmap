from collections import defaultdict
from statistics import mean
from typing import Self

from course import Course
from mentor import Mentor


class Lecturer(Mentor):
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        self.courses_grades = defaultdict[Course, list[int]](list)

    def __str__(self) -> str:  # pyright: ignore[reportImplicitOverride]
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self._get_average_grade()}"
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

    def _get_average_grade(self) -> float:
        if len(self.courses_grades) == 0:
            return -1
        return mean(mean(course_grades) for course_grades in self.courses_grades.values())
