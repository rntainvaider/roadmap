from database.db import DB

publisher_name = input("Введите ФИО издателя\n")

DB.get_book_sale(publisher_name)
