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

    cur.execute("DELETE FROM messages WHERE from_user_id = %s", (id_user,))
    cur.execute("DELETE FROM messages WHERE to_user_id = %s", (id_user,))
    cur.execute("DELETE FROM likes WHERE user_id = %s", (id_user,))
    cur.execute("DELETE FROM media WHERE user_id = %s", (id_user,))
    cur.execute("DELETE FROM profiles WHERE user_id = %s", (id_user,))
    cur.execute("DELETE FROM users WHERE id = %s", (id_user,))

    connect.commit()
    # result = cur.fetchall()
    # for item in result:
    #     print(item)


del_user_by_id(1)

"""
DELETE FROM likes
WHERE likes.user_id = delete_user_id;

DELETE FROM users_communities
WHERE users_communities.user_id = delete_user_id;

DELETE FROM messages
WHERE messages.to_user_id = delete_user_id OR messages.from_user_id = delete_user_id;

DELETE FROM friend_requests
WHERE friend_requests.initiator_user_id = delete_user_id OR friend_requests.target_user_id = delete_user_id;

DELETE likes
FROM media
JOIN likes ON likes.media_id = media.id
WHERE media.user_id = delete_user_id;

UPDATE profiles
JOIN media ON profiles.photo_id = media.id
SET profiles.photo_id = NULL
WHERE media.user_id = delete_user_id;

DELETE FROM media
WHERE media.user_id = delete_user_id;

DELETE FROM profiles
WHERE profiles.user_id = delete_user_id;

DELETE FROM users
WHERE users.id = delete_user_id;"""

# import pymysql

# def delete_user_data(user_id):
#     try:
#         # Подключение к базе данных
#         connection = pymysql.connect(
#             host='localhost',
#             user='root',
#             password='password',
#             database='vk',
#             cursorclass=pymysql.cursors.DictCursor
#         )

#         with connection.cursor() as cursor:
#             # Удаление сообщений пользователя
#             cursor.execute("DELETE FROM messages WHERE user_id = %s", (user_id,))
#             # Удаление лайков пользователя
#             cursor.execute("DELETE FROM likes WHERE user_id = %s", (user_id,))
#             # Удаление медиа-записей пользователя
#             cursor.execute("DELETE FROM media WHERE user_id = %s", (user_id,))
#             # Удаление профиля пользователя
#             cursor.execute("DELETE FROM profiles WHERE user_id = %s", (user_id,))
#             # Удаление пользователя из таблицы users
#             cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))

#             # Подтверждаем изменения
#             connection.commit()

#         return user_id

#     except Exception as e:
#         print(f"Ошибка: {e}")
#         return None

#     finally:
#         # Закрытие соединения с базой данных
#         connection.close()

# # Пример вызова функции
# user_id = 123  # ID пользователя, которого нужно удалить
# deleted_user = delete_user_data(user_id)

# if deleted_user:
#     print(f"Пользователь с id {deleted_user} успешно удален.")
# else:
#     print("Ошибка при удалении пользователя.")


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
