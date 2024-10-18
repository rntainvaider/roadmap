def get_money(money: int):
    if money % 100 == 0:
        return f"Вы сняли {money}"
    else:
        return "Такую сумму снять невозможно. Обратитесь в другой банкомат!"

if __name__ == "__main__":
    money = int(input("Введите сумму, которую хотите снять: "))
    print(get_money(money))