from course import Course
from mentor import Mentor
from student import Student


class Reviewer(Mentor):
    def __str__(self) -> str:  # pyright: ignore[reportImplicitOverride]
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_homework(self, student: Student, course: Course, grade: int) -> None:
        if grade < 0 or grade > 10:  # noqa: PLR2004
            raise ValueError("grade should be in range [0, 10]")  # noqa: TRY003
        if course not in self.courses_attached:
            raise ValueError("lecturer should be attached to the course")  # noqa: TRY003
        if course not in student.courses_in_progress:
            raise ValueError("student should be enrolled for the course")  # noqa: TRY003
        student.courses_grades[course].append(grade)
