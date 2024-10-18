class Converter:
    
    @staticmethod
    def converter_in_pound(kilogram: float):
        return kilogram * 2.2046
    
    @staticmethod
    def converter_in_kilogram(pound: float):
        return pound / 2.2046
    
    @staticmethod
    def converter_in_metre(mile: float):
        return mile / 0.00062137
    
    @staticmethod
    def converter_in_mile(metre: float):
        return metre * 0.00062137
    
print(f"{Converter.converter_in_pound(75)} фунтов")
print(f"{Converter.converter_in_kilogram(50)} килограмм")
print(f"{Converter.converter_in_metre(100)} метров")
print(f"{Converter.converter_in_mile(10)} миль")