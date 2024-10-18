def frequency_histogram() -> None:
    text_input = input("Введите текст: ")
    book_histogram = dict()

    for item in text_input:
        if item not in book_histogram.keys():
            book_histogram[item] = text_input.count(item)

    for key, value in sorted(book_histogram.items()):
        print(f"{key} : {value}")

    max_values = max(book_histogram.values())

    print(f"Максимальная частота: {max_values}")

frequency_histogram()
