def secrets_of_archeology(table_numbers: list) -> str:
    for numb in table_numbers:
        if numb % 2 == 0 and not numb % 3 == 0:
            print(f"Число {numb} подходит")
        else:
            print(f"Число {numb} не подходит")

table_numbers = [114, 12, 14, 10605, 4907, 450]
secrets_of_archeology(table_numbers)