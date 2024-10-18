from course import Course


class Mentor:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached = list[Course]()

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"
