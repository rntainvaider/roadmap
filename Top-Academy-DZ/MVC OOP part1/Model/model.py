class ShoeModel:
    def __init__(self, shoe_type, gender, style, color, price, manufacturer, size):
        self.shoe_type = shoe_type     
        self.gender = gender             
        self.style = style                
        self.color = color                
        self.price = price                
        self.manufacturer = manufacturer  
        self.size = size  
    
    def get_info(self):
        return f"Тип: {self.shoe_type}, Пол: {self.gender}, Вид: {self.style}, " \
               f"Цвет: {self.color}, Цена: {self.price}, Производитель: {self.manufacturer}, Размер: {self.size}"

    def set_price(self, new_price):
        self.price = new_price