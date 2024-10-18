def load_cook_book() -> dict[str, list[dict[str, int | str]]]:
    with open("recipes.txt") as file:
        dishes = file.read().split("\n\n")

    cook_book = dict[str, list[dict[str, int | str]]]()
    for dish in dishes:
        dish_name, _, *raw_ingredients = dish.splitlines()
        ingredients = list[dict[str, int | str]]()
        for raw_ingredient in raw_ingredients:
            ingredient_name, quantity, measure = raw_ingredient.split(" | ")
            ingredients.append(
                {
                    "ingredient_name": ingredient_name,
                    "quantity": int(quantity),
                    "measure": measure,
                }
            )
        cook_book[dish_name] = ingredients
    return cook_book


def get_shop_list_by_dishes(
    dish_names: list[str], person_count: int
) -> dict[str, dict[str, int | str]]:
    cook_book = load_cook_book()
    shop_list = dict[str, dict[str, int | str]]()
    for dish_name in dish_names:
        ingredients = cook_book[dish_name]
        for ingredient in ingredients:
            ingredient_name = ingredient["ingredient_name"]
            ingredient_measure = ingredient["measure"]
            ingredient_quantity = ingredient["quantity"] * person_count
            if ingredient_name in shop_list:
                shop_list[ingredient_name]["quantity"] += ingredient_quantity
            else:
                shop_list[ingredient_name] = {
                    "measure": ingredient_measure,
                    "quantity": ingredient_quantity,
                }
    return shop_list


print(get_shop_list_by_dishes(["Омлет", "Омлет"], 2))
