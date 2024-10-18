class Auto:
    def __init__(self, model_name: str, year_publication: int, manufacturer: str, volume: int, car_color: str, price: int):
        self.__model_name = model_name
        self.__year_publication = year_publication
        self.__manufacturer = manufacturer
        self.__volume = volume
        self.__car_color = car_color
        self.__price = price

    def __str__(self):
        return f"Модель: {self.__model_name}, год выпуска: {self.__year_publication}, производитель: {self.__manufacturer}, объем двигателя: {self.__volume}, цвет: {self.__car_color}, цена: {self.__price}"
    
    def model(self):
        return f"Модель автомобиля: {self.__model_name}"
    
    def year(self):
        return f"Год выпуска: {self.__year_publication}"
    
    def manufacturer(self):
        return f"Производитель: {self.__manufacturer}"
    
    def volume(self):
        return f"Объем двигателя: {self.__volume}"
    
    def car_color(self):
        return f"Цвет машины: {self.__car_color}"
    
    def price(self):
        return f"Цена: {self.__price}"
    
    def new_model(self, new_model: str):
        if not isinstance(new_model, str):
            raise TypeError("Должна быть строка")
        self.__model_name = new_model
    
    def new_year(self, new_year: int):
        if not isinstance(new_year, int):
            raise TypeError("Должно быть число")
        self.__year_publication = new_year    
        
    def new_manufacturer(self, new_manufacturer: str):
        if not isinstance(new_manufacturer, str):
            raise TypeError("Должна быть строка")
        self.__manufacturer = new_manufacturer 
        
    def new_volume(self, new_volume: int):
        if not isinstance(new_volume, int):
            raise TypeError("Должно быть число")
        self.__volume = new_volume 
        
    def new_car_color(self, new_car_color: str):
        if not isinstance(new_car_color, str):
            raise TypeError("Должна быть строка")
        self.__car_color = new_car_color 
        
    def new_price(self, new_price: int):
        if not isinstance(new_price, int):
            raise TypeError("Должно быть число")
        self.__price = new_price 
    
my_auto = Auto(
    "Mersedes", 
    "2010", 
    "Завод", 
    "200", 
    "Серый", 
    "4_000_000"
    )

print(my_auto)
print(my_auto.model())
print(my_auto.year())
print(my_auto.manufacturer())
print(my_auto.volume())
print(my_auto.car_color())
print(my_auto.price())
my_auto.new_model("bmw")
my_auto.new_year(1998)
my_auto.new_manufacturer("Германия")
my_auto.new_volume(400)
my_auto.new_car_color("Белый")
my_auto.new_price(12392392)
print(my_auto)