class Books:
    def __init__(self, name_book: str, year_manufacture: int, publisher: str, genre: str, author: str, price: int):
        self.__name_book = name_book
        self.__year_manufacture = year_manufacture
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price
        
    def __str__(self):
        return f"Название книги: {self.__name_book}, год выпуска: {self.__year_manufacture}, издатель: {self.__publisher}, жанр: {self.__genre}, автор: {self.__author}, цена: {self.__price}"

    def name_book(self):
        return f"Название книги: {self.__name_book}"
    
    def year_manufacture(self):
        return f"Год выпуска: {self.__year_manufacture}"
    
    def publisher(self):
        return f"Издатель: {self.__publisher}"
    
    def genre(self):
        return f"Жанр: {self.__genre}"
    
    def author(self):
        return f"Автор: {self.__author}"
    
    def price(self):
        return f"Цена: {self.__price}"
    
    def new_name_book(self, new_name_book: str):
        if not isinstance(new_name_book, str):
            raise TypeError("Должна быть строка")
        self.__name_book = new_name_book
        
    def new_year_manufacture(self, new_year_manufacture: int):
        if not isinstance(new_year_manufacture, int):
            raise TypeError("Должно быть число")
        self.__year_manufacture = new_year_manufacture

    def new_publisher(self, new_publisher: str):
        if not isinstance(new_publisher, str):
            raise TypeError("Должна быть строка")
        self.__publisher = new_publisher
        
    def new_genre(self, new_genre: str):
        if not isinstance(new_genre, str):
            raise TypeError("Должна быть строка")
        self.__genre = new_genre
        
    def new_author(self, new_author: str):
        if not isinstance(new_author, str):
            raise TypeError("Должна быть строка")
        self.__author = new_author
    
    def new_price(self, new_price: int):
        if not isinstance(new_price, int):
            raise TypeError("Должно быть число")
        self.__price = new_price
        
    
my_book = Books(
    "Мастер и Маргарита",
    1976, 
    "Три бабки",
    "Роман",
    "Булгаков",
    1450
)

print(my_book)
print(my_book.name_book())
print(my_book.year_manufacture())
print(my_book.publisher())
print(my_book.genre())
print(my_book.author())
print(my_book.price())
my_book.new_name_book("Война и мир")
my_book.new_year_manufacture(1932)
my_book.new_publisher("Пять бабок")
my_book.new_genre("Роман")
my_book.new_author("Толстой")
my_book.new_price(1499)
print(my_book)