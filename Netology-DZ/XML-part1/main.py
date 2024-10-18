import xml.etree.ElementTree as ET


def read_xml(file_path: str, word_max_len: int = 6, top_words_amt: int = 10) -> None:
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    news_list = root.findall("channel/item/description")

    word_frequency = dict[str, int]()
    for news in news_list:
        result = news.text
        for n in result.split():
            if len(n) <= word_max_len:
                continue
            word_frequency[n] = word_frequency.get(n, 0) + 1
    return sorted(word_frequency, key=word_frequency.get, reverse=True)[:top_words_amt]


if __name__ == "__main__":
    print(read_xml("newsafr.xml"))
