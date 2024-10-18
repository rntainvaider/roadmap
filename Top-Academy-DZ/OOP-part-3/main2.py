from abc import ABC, abstractmethod

class Ship: 
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
        
class Frigate(Ship):
    
    def __init__(self, name: str, year_manufacture: int, color: str, engine_power: int):
        self.valid_int(engine_power)
        
        super().__init__(name, year_manufacture, color)
        self.engine_power = engine_power

    def turn_on(self) -> str:
        return f'Engine start, Frigate {self.name}: on'

    def turn_of(self) -> str:
        return f'Engine shutdown, Frigate {self.name}: off \n'

    def info(self) -> str:
        return f"Frigate, {super().__str__()}, engine_power: {self.engine_power}"
        
class Destroyer(Ship):   
    def __init__(self, name: str, year_manufacture: int, color: str, engine_power: int):
        self.valid_int(engine_power)
        
        super().__init__(name, year_manufacture, color)
        self.engine_power = engine_power
    
    def turn_on(self) -> str:
        return f'Engine start, Destroyer {self.name}: on'

    def turn_of(self) -> str:
        return f'Engine shutdown, Destroyer {self.name}: off \n'

    def info(self) -> str:
        return f"Destroyer, {super().__str__()}, engine_power: {self.engine_power}"
    
class Cruiser(Ship):   
    def __init__(self, name: str, year_manufacture: int, color: str, engine_power: int):
        self.valid_int(engine_power)
        
        super().__init__(name, year_manufacture, color)
        self.engine_power = engine_power
    
    def turn_on(self) -> str:
        return f'Engine start, Cruiser {self.name}: on'

    def turn_of(self) -> str:
        return f'Engine shutdown, Cruiser {self.name}: off \n'

    def info(self) -> str:
        return f"Cruiser, {super().__str__()}, engine_power: {self.engine_power}"

ship_frigate = Frigate("Frigate", 1983, "blue", 25000)
print(ship_frigate.turn_on())
print(ship_frigate.info())
print(ship_frigate.turn_of())

ship_destroyer = Destroyer("Destroyer", 1991, "black", 12000)
print(ship_destroyer.turn_on())
print(ship_destroyer.info())
print(ship_destroyer.turn_of())

ship_cruiser = Cruiser("Cruiser", 1987, "green", 25000)
print(ship_cruiser.turn_on())
print(ship_cruiser.info())
print(ship_cruiser.turn_of())