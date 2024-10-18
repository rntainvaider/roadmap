from abc import ABC, abstractmethod

class Device: 
    def __init__(self, name: str, year_manufacture: int, color: str):
        self.valid_str(name)
        self.valid_str(color)
        self.valid_int(year_manufacture)
        
        self.name = name
        self.year_manufacture = year_manufacture
        self.color = color
        
    def __str__(self):
        return f"name: {self.name}, year_manufacture: {self.year_manufacture}, color: {self.color}"
    
    @classmethod
    def valid_str(cls, data: str):
        if not isinstance(data, str):
            raise TypeError("Должна быть строка")
    
    @classmethod
    def valid_int(cls, data: int):
        if not isinstance(data, int):
            raise TypeError("Должно быть число")
        
    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_of(self) -> str:
        pass

    @abstractmethod
    def info(self) -> str:
        pass
        
class CoffeeMachine(Device):
    
    def __init__(self, name: str, year_manufacture: int, color: str, volume: int):
        self.valid_int(volume)
        
        super().__init__(name, year_manufacture, color)
        self.volume = volume

    def turn_on(self) -> str:
        return f'Coffee machine {self.name}: on'

    def turn_of(self) -> str:
        return f'Coffee machine {self.name}: off \n'

    def info(self) -> str:
        return f"Coffee machine, {super().__str__()}, volume: {self.volume}"
        
class Blender(Device):   
    def __init__(self, name: str, year_manufacture: int, color: str, volume: int):
        self.valid_int(volume)
        
        super().__init__(name, year_manufacture, color)
        self.volume = volume
    
    def turn_on(self) -> str:
        return f'Blender {self.name}: on'

    def turn_of(self) -> str:
        return f'Blender {self.name}: off \n'

    def info(self) -> str:
        return f"Blender, {super().__str__()}, volume: {self.volume}"
    
class MeatGrider(Device):   
    def __init__(self, name: str, year_manufacture: int, color: str, volume: int):
        self.valid_int(volume)
        
        super().__init__(name, year_manufacture, color)
        self.volume = volume
    
    def turn_on(self) -> str:
        return f'Meat greader {self.name}: on'

    def turn_of(self) -> str:
        return f'Meat greader {self.name}: off \n'

    def info(self) -> str:
        return f"Meat greader, {super().__str__()}, volume: {self.volume}"

device_coffe_machine = CoffeeMachine("Samsung", 2010, "blue", 2500)
print(device_coffe_machine.turn_on())
print(device_coffe_machine.info())
print(device_coffe_machine.turn_of())

device_blender = Blender("Bosh", 2012, "black", 2000)
print(device_blender.turn_on())
print(device_blender.info())
print(device_blender.turn_of())

device_meat_greader = MeatGrider("Huiway", 2015, "green", 2250)
print(device_meat_greader.turn_on())
print(device_meat_greader.info())
print(device_meat_greader.turn_of())