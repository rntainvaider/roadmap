 1. Написать функцию, которая удаляет всю информацию об указанном пользователе из БД vk.
- Пользователь задается по id.
- Удалить нужно все сообщения, лайки, медиа записи, профиль и запись из таблицы users.
- Функция должна возвращать номер пользователя.


import pymysql

def delete_user_data(user_id):
    try:
        # Подключение к базе данных
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='password',
            database='vk',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            # Удаление сообщений пользователя
            cursor.execute("DELETE FROM messages WHERE user_id = %s", (user_id,))
            # Удаление лайков пользователя
            cursor.execute("DELETE FROM likes WHERE user_id = %s", (user_id,))
            # Удаление медиа-записей пользователя
            cursor.execute("DELETE FROM media WHERE user_id = %s", (user_id,))
            # Удаление профиля пользователя
            cursor.execute("DELETE FROM profiles WHERE user_id = %s", (user_id,))
            # Удаление пользователя из таблицы users
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))

            # Подтверждаем изменения
            connection.commit()

        return user_id

    except Exception as e:
        print(f"Ошибка: {e}")
        return None

    finally:
        # Закрытие соединения с базой данных
        connection.close()

# Пример вызова функции
user_id = 123  # ID пользователя, которого нужно удалить
deleted_user = delete_user_data(user_id)

if deleted_user:
    print(f"Пользователь с id {deleted_user} успешно удален.")
else:
    print("Ошибка при удалении пользователя.")
