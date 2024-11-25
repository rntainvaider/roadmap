# абстракция - 4й принцип ООП
from abc import ABC, abstractmethod


class MusicPause:
    def play_music(self) -> None:
        print("sd asd fgfd we wdwew w")


class Transport(ABC):
    def __init__(self, color, speed) -> None:
        self._colo = color
        self._speed = speed

    @property  # геттер - позволяет обращаться к атрибуту через точку
    def color(self) -> None:
        return self._color

    @color.setter  # позволяет инициализировать атрибут через точку
    def color(self, value) -> None:
        self._color = value

    @abstractmethod
    def ride_on_the_earth(self) -> None:
        pass

    def signal(self) -> None:
        print("TYTY")


zhiguli = Transport("red", "60")
print(zhiguli.color)
