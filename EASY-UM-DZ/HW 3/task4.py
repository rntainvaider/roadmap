def get_check_amount(count_products: int):
    price_products = []
    while count_products > 0:
        product = int(input("Введите сумму товара: "))
        price_products.append(product)
        count_products -= 1

    sum_products = 0
    for sum_product in price_products:
        sum_products += sum_product
    
    if sum_products > 10_000:
        discount_products = sum_products * 10 / 100
        return f"Сумма чека со скидкой составила {discount_products}"
    else:
        return f"Сумма чека без скидки составила {sum_products}"

if __name__ == "__main__":
    count_products = int(input("Введите количество товаров: "))
    print(get_check_amount(count_products))