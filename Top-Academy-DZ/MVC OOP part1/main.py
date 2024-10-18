from Model.model import ShoeModel
from View.view import ShoeView
from Controller.controller import ShoeController

if __name__ == "__main__":
    shoe = ShoeModel(shoe_type="Кроссовки", gender="Мужская", style="Спортивные", color="Черный", price=5000, manufacturer="Nike", size=42)

    view = ShoeView()

    controller = ShoeController(shoe, view)

    controller.show_shoe_info()

    controller.update_price(4500)

    controller.show_shoe_info()