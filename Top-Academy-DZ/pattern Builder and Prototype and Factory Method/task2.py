from abc import ABC, abstractmethod

class Pasta(ABC):
    def __init__(self) -> None:
        self.type = None
        self.sauce = None
        self.topping = None
        self.additives = list()

    @abstractmethod
    def prepare(self):
        pass

    def __str__(self) -> str:
        return f"Pasta type: {self.type}, sauce: {self.sauce}, topping: {self.topping}, addivites: {', '.join(self.additives)}"
    
class Spaghetti(Pasta):
    def prepare(self):
        self.type = "Spaghetti"
        self.sauce = "Tomato Sauce"
        self.topping = "Meatballs"
        self.additives = ["Parmesan", "Basil"]

class FettuccineAlfredo(Pasta):
    def prepare(self):
        self.type = "Fettuccine"
        self.sauce = "Alfredo Sauce"
        self.topping = "Chicken"
        self.additives = ["Parsley", "Black Pepper"]

class PenneArrabbiata(Pasta):
    def prepare(self):
        self.type = "Penne"
        self.sauce = "Arrabbiata sauce"
        self.topping = "Chili Peppers"
        self.additives = ["Garlic", "Olive Oil"]

class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "spaghetti":
            pasta = Spaghetti()
        elif pasta_type == "fettuccine":
            pasta = FettuccineAlfredo()
        elif pasta_type == "penne":
            pasta = PenneArrabbiata()
        else:
            raise ValueError(f"Unknown pasta type: {pasta_type}")
        
        pasta.prepare()
        return pasta
    
if __name__ == "__main__":
    pasta_factory = PastaFactory()

    spaghetti = pasta_factory.create_pasta("spaghetti")
    print(spaghetti)

    fettuccine = pasta_factory.create_pasta("fettuccine")
    print(fettuccine)

    penne = pasta_factory.create_pasta("penne")
    print(penne)

    fettuchini = pasta_factory.create_pasta("fettuchini")
    print(fettuchini)