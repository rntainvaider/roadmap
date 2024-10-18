class TemperatureConverter:
    
    converter_count = 0
       
    @staticmethod
    def converter_in_fahrenheit(celsius: float):
        TemperatureConverter.converter_count += 1
        return ((celsius * 9) / 5) + 32
    
    @staticmethod
    def converter_in_celsius(fahrenheit: float):
        TemperatureConverter.converter_count += 1
        return (5 * (fahrenheit - 32)) / 9
    
    @staticmethod
    def get_count():
        return TemperatureConverter.converter_count
    
print(f"{TemperatureConverter.converter_in_fahrenheit(24)} фаренгейта")
print(f"{TemperatureConverter.converter_in_celsius(95)} цельсия")
print(f"{TemperatureConverter.get_count()} количество подсчетов")