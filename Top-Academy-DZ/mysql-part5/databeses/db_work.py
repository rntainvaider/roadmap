from dataclasses import dataclass
from datadase_settings import get_mysql_connect

def get_all_users() -> None:
    connect = get_mysql_connect()
    cur = connect.cursor()
    cur.execute(f"select * from users")

    result = cur.fetchall()
    for item in result:
        print(item)


get_all_users()

def del_user_by_id(id_user: int) -> None:
    connect = get_mysql_connect()
    cur = connect.cursor()
    cur.execute(f"DELETE FROM friend_requests WHERE idinitiator_user_id = {id_user}")

    result = cur.fetchall()
    for item in result:
        print(item)


del_user_by_id(1)


# from dataclasses import dataclass

# from databeses.datadase_settings import get_mysql_connect


# @dataclass
# class Book:
#     id: int
#     title: str
#     price: int
#     amount: int
#     author_id: int
#     genre_id: int


# def get_all_book(ID_USER: int):
#     con = get_mysql_connect()
#     cur = con.cursor()
#     cur.execute("select * from book")

#     res = cur.fetchall()
#     lst = []
#     for item in res:
#         lst.append(
#             Book(
#                 id=item[0],
#                 title=item[1],
#                 price=item[2],
#                 amount=item[3],
#                 author_id=item[4],
#                 genre_id=item[5],
#             )
#         )
#     for book in lst:
#         print(book.__dict__)


# print(0.1 * 3)
# get_all_book()

# -- 1. Написать функцию, которая удаляет всю информацию об указанном пользователе из БД vk.
#       Пользователь задается по id.
#       Удалить нужно все сообщения, лайки, медиа записи, профиль и запись из таблицы users.
# --    Функция должна возвращать номер пользователя.
