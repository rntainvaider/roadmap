from Model.model import ShoeModel

class ShoeView:
    @staticmethod
    def display_shoe_info(shoe: ShoeModel):
        print(shoe.get_info())

    @staticmethod
    def display_update_success():
        print("Цена успешно обновлена.")