list_of_lists_1: list[list[str | int | bool | None]] = [
    ["a", "b", "c"],
    ["d", "e", "f", "h", False],
    [1, 2, None],
]


def flat_generator(list_of_lists: list[list[str | bool | int | None]]):
    for i in list_of_lists:
        for item in i:
            yield item


print(flat_generator(list_of_lists_1))
