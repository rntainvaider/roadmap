"""Необязательное задание. Написать итератор, аналогичный итератору из задания 1,
но обрабатывающий списки с любым уровнем вложенности. """


class FlatIterator:

    def __init__(self, list_of_list) -> None:
        self.stack = [list_of_list]

    def __iter__(self):
        return self

    def __next__(self) -> None:
        while self.stack:
            current = self.stack.pop(0)  # Извлекаем первый элемент из стека
            if isinstance(
                current, list
            ):  # Если текущий элемент — список, добавляем его элементы в начало стека
                self.stack = current + self.stack
            else:
                return current
        raise StopIteration  # Остановка итерации при полном обходе


def test_3() -> None:

    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
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
        "!",
    ]


if __name__ == "__main__":
    test_3()
