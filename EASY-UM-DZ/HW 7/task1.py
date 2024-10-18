def cosmic_food():
    kg_food = 100
    for item in range(1, 100):
        if kg_food > 0:
            kg_food -= 4
            print(f"За {item} месяц осталось еды {kg_food} кг")
        else:
            break

cosmic_food()