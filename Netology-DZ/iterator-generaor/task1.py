"""Доработать класс FlatIterator в коде ниже. Должен получиться итератор,
который принимает список списков и возвращает их плоское представление,
т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже
также должна отработать без ошибок."""


class FlatIterator:

    def __init__(self, list_of_list: list[list[str | int | bool | None]]) -> None:
        self.list_of_list = list_of_list
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str | int | bool | None:
        while self.outer_index < len(self.list_of_list):
            inner_list = self.list_of_list[self.outer_index]
            if self.inner_index < len(inner_list):
                item = inner_list[self.inner_index]
                self.inner_index += 1
                return item
            self.outer_index += 1
            self.inner_index = 0
        raise StopIteration


def test_1() -> None:

    list_of_lists_1: list[list[str | int | bool | None]] = [
        ["a", "b", "c"],
        ["d", "e", "f", "h", False],
        [1, 2, None],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
    ]


if __name__ == "__main__":
    test_1()
