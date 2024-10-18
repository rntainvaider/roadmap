def storage() -> None:
    small_storage = {
        'гвозди': 5000,
        'шурупы': 3040,
        'саморезы': 2000
    }

    big_storage = {
        'доски': 1000,
        'балки': 150,
        'рейки': 600
    }

    for key, value in small_storage.items():
        big_storage[key] = value


    list_product = list()

    for key in big_storage.keys():
        list_product.append(key)

    print(f"Список товаров: {', '.join(list_product)}")

    product_name = input("Введите название товара: ").lower()

    if product_name not in big_storage.keys():
        print("Нет такого товара!!!")
    else:
        count_product = big_storage.get(product_name)

        print(count_product)

storage()
