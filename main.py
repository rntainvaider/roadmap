phone_book = {"Erevan": 89996932314, "Igor": 89993323123, "Petr": 89992334411}
for name in phone_book.keys():
    print(name)

for phone in phone_book.values():
    print(phone)

for key, value in phone_book.items():
    print(key, "-", value)

count_add_friends = int(input("Введите кол-во друзей: "))
for _ in range(count_add_friends):
    name_friends = input("Введите имя друга: ")
    number_phone = int(input("Введите номер телефона: "))
    phone_book[name_friends] = number_phone
print(phone_book)

name = input("Введите имя для кого хотите изменить номер ")
phone = input("Введите номер ")
phone_book[name] = phone
print(phone_book)

name_frie = input("Введите имя для поиска и удаления: ")
if name_frie in phone_book.keys():
    del phone_book[name_frie]
    print("Удалён")
else:
    print("Пользователь не найден")
    pho = input("Введите номер телефона ненайденного пользователя ")
    phone_book[name_frie] = pho
print(phone_book)
