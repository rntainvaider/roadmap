def get_phone_book(phonebook: dict[str, int]) -> None:
    while True:
        name = input("Введите имя (или введите stop для заверешния): ")
        if name.lower() == "stop":
            break

        phone_number = int(input("Введите номер телефона: "))

        if name in phonebook:
            print(f"Контакт с именем {name} уже существует!")
        else:
            phonebook[name] = phone_number
            print(f"Контакт {name} добавлен!")

        print("\nТекущая телефонная книга:")
        for contact_name, contact_number in phonebook.items():
            print(f"{contact_name}: {contact_number}")
        print()

phonebook = dict()
get_phone_book(phonebook)
