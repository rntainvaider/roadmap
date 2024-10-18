import json


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм
    with open(file_path, encoding="UTF-8") as file:
        data = json.load(file)
    news = data["rss"]["channel"]["items"]

    word_frequency = dict[str, int]()
    for description in (article["description"] for article in news):
        for word in description.split():
            if len(word) <= word_max_len:
                continue
            word_frequency[word] = word_frequency.get(word, 0) + 1
    return sorted(word_frequency, key=word_frequency.get, reverse=True)[:top_words_amt]


if __name__ == "__main__":
    print(read_json("newsafr.json"))
