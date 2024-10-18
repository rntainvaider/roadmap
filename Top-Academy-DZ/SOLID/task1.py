class SpeedCalculationCar:
    def calculate_allowed_spped(self, vehicle):
        if vehicle.get_type().lower() == "car":
            return vehicle.get_max_speed() * 0.8
        return 0.0

class SpeedCalculationBus:
    def calculate_allowed_spped(self, vehicle):
        if vehicle.get_type().lower() == "bus":
                return vehicle.get_max_speed() * 0.6
        return 0.0

class Vehicle:
    def __init__(self, max_speed: int, type: str):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type

if __name__ == "__main__":
    vehicle_car = Vehicle(100, "car")
    vehicle_bus = Vehicle(80, "bus")

    speed_calculation_car = SpeedCalculationCar()
    speed_calculation_bus = SpeedCalculationBus()

    print(speed_calculation_car.calculate_allowed_spped(vehicle_car))
    print(speed_calculation_bus.calculate_allowed_spped(vehicle_bus))