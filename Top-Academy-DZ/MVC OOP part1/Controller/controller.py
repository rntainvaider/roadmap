from Model.model import ShoeModel
from View.view import ShoeView

class ShoeController:
    def __init__(self, shoe: ShoeModel, view: ShoeView):
        self.shoe = shoe  # Модель
        self.view = view  # Представление

    def update_price(self, new_price):
        # Обновляем цену и уведомляем пользователя
        self.shoe.set_price(new_price)
        self.view.display_update_success()

    def show_shoe_info(self):
        # Отображаем информацию об обуви
        self.view.display_shoe_info(self.shoe)
