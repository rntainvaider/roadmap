class Stadium:
    def __init__(self, name_stadium: str, opening_date: int, country: str, city: str, capacity: int):
        self.__name_stadiun = name_stadium
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity
    
    def __str__(self):
        return f"Название стадиона: {self.__name_stadiun}, дата открытия: {self.__opening_date}, страна: {self.__country}, город: {self.__city}, вместимость: {self.__capacity}"
    
    def name_stadium(self):
        return f"Название стадиона: {self.__name_stadiun}"
    
    def oppening_date(self):
        return f"дата открытия: {self.__opening_date}"
    
    def country(self):
        return f"страна: {self.__country}"
    
    def city(self):
        return f"город: {self.__city}"
    
    def capacity(self):
        return f"вместимость: {self.__capacity}"
    
    def new_name_stadium(self, new_name_stadium: str):
        if not isinstance(new_name_stadium, str):
            raise TypeError("Должна быть строка")
        self.__name_stadiun = new_name_stadium
        
    def new_oppening_date(self, new_oppening_date: int):
        if not isinstance(new_oppening_date, int):
            raise TypeError("Должно быть число")
        self.__opening_date = new_oppening_date
    
    def new_country(self, new_country: str):
        if not isinstance(new_country, str):
            raise TypeError("Должна быть строка")
        self.__country = new_country
        
    def new_city(self, new_city: str):
        if not isinstance(new_city, str):
            raise TypeError("Должна быть строка")
        self.__city = new_city
        
    def new_capacity(self, new_capacity: int):
        if not isinstance(new_capacity, int):
            raise TypeError("Должно быть число")
        self.__capacity = new_capacity

stadium = Stadium(
    "Южный",
    1978, 
    "Россия",
    "Ижевск",
    1000
)

print(stadium)
print()
print(stadium.name_stadium())
print(stadium.oppening_date())
print(stadium.country())
print(stadium.city())
print(stadium.capacity())
print()
stadium.new_name_stadium("Восточный")
stadium.new_oppening_date(1489)
stadium.new_country("Россия")
stadium.new_city("Батайск")
stadium.new_capacity(15000)
print(stadium)