class Car:
    def __init__(self) -> None:
        self.auto = None
        self.model = None
        self.year = None
        self.color = None
        self.engine = None

    def __str__(self) -> str:
        return f"Auto: {self.auto}, model: {self.model}, year: {self.year}, color: {self.color}, engine: {self.engine}"


class CarBuilder:
    def __init__(self) -> None:
        self.car = Car()

    def get_auto(self, auto: str):
        self.car.auto = auto
        return self

    def get_model(self, model: str):
        self.car.model = model
        return self

    def get_year(self, year: int):
        self.car.year = year
        return self

    def get_color(self, color: str):
        self.car.color = color
        return self

    def get_engine(self, engine: str):
        self.car.engine = engine
        return self

    def builder(self):
        return self.car


if __name__ == "__main__":
    car_builder = CarBuilder()

    car1 = (
        car_builder.get_auto("Toyta")
        .get_model("Camry")
        .get_year(2017)
        .get_color("white")
        .get_engine("V8")
        .builder()
    )

    print(car1)

    car2 = (
        car_builder.get_auto("BMW")
        .get_model("240i")
        .get_year(2002)
        .get_color("black")
        .get_engine("V6")
        .builder()
    )

    print(car2)
