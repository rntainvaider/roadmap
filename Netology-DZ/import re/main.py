from ast import pattern
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

def split_name(contact):
    full_name = " ".join(contact[:3]).split()
    if len(full_name) == 3:
        contact[0], contact[1], contact[2] = full_name
    elif len(full_name) == 2:
        contact[0], contact[1] = full_name
        contact[2] = ""
    if len(full_name) == 1:
        contact[0] = full_name[0]
        contact[1], contact[2] = "", ""
    return contact

def format_phone(phone) -> str:
    pattern = r"^(\+7|8)?\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s*\(?доб\.\s(\d{4})\)?)?$"
    return re.sub(pattern, r"+7(\2)\3-\4-\5 доб.\7" if "доб." in phone else r"+7(\2)\3-\4-\5", phone)

contacts_dict = {}
for contact in contacts_list[1:]:
    contact[:3] = split_name(contact[:3])
    contact[5] = format_phone(contact[5])

     # Создание ключа по ФИ
    key = (contact[0], contact[1])
    if key not in contacts_dict:
        contacts_dict[key] = contact
    else:
        # Объединение дубликатов, заполняя пустые значения
        for i in range(len(contact)):
            if contacts_dict[key][i] == "" and contact[i] != "":
                contacts_dict[key][i] = contact[i]

contacts_list = [contacts_list[0]] + list(contacts_dict.values())

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
