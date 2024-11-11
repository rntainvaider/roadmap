import psycopg2
from typing import ContextManager

def create_db(conn) -> None:
    cur.execute("CREATE TABLE IF NOT EXISTS phone_clients(id SERIAL PRIMARY KEY, phone VARCHAR(18));")
    cur.execute("CREATE TABLE IF NOT EXISTS client(id SERIAL PRIMARY KEY, first_name VARCHAR(55), last_name VARCHAR(55), email VARCHAR(55), phone_id INT, FOREIGN KEY (phone_id) REFERENCES phone_clients (id));")

def create_new_clients(conn, first_name: str, last_name: str, email: str, phone_id: int|None=None) -> None:
    cur.execute("INSERT INTO client(first_name, last_name, email, phone_id) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, phone_id))

def create_phone_clients(conn, phone: str) -> None:
    cur.execute("INSERT INTO phone_clients(phone) VALUES (%s)", (phone, ))

def change_date_clients(conn, id_client: int, first_name: str|None=None, last_name: str|None=None, email: str|None=None, phone_id: int|None=None) -> None:
    if first_name is not None:
        cur.execute("UPDATE client SET first_name=%s WHERE id = %s", (first_name, id_client))
    if last_name is not None:
        cur.execute("UPDATE client SET last_name=%s WHERE id = %s", (last_name, id_client))
    if email is not None:
        cur.execute("UPDATE client SET email=%s WHERE id = %s", (email, id_client))
    if phone_id is not None:
        cur.execute("UPDATE client SET phone_id=%s WHERE id = %s", (phone_id, id_client))

def delete_phone_client(conn, id: int) -> None:
    cur.execute("DELETE FROM phone_clients WHERE id = %s", (str(id)))

def delete_client(conn, client_id: int) -> None:
    cur.execute("DELETE FROM client WHERE id = %s", str((client_id)))

def get_client(conn:ContextManager[list[tuple[int | str]]], first_name: str|None=None, last_name: str|None=None, email: str|None=None, phone_clients: int|None=None) -> None:
    if first_name is not None:
        cur.execute("SELECT * FROM client WHERE first_name=%s", (first_name, ))
    if last_name is not None:
        cur.execute("SELECT * FROM client WHERE last_name=%s", (last_name, ))
    if email is not None:
        cur.execute("SELECT * FROM client WHERE email=%s", (email, ))
    if phone_clients is not None:
        cur.execute("SELECT * FROM client WHERE phone_clients=%s", (str(phone_clients)))
    result = cur.fetchall()
    return result

if __name__ == '__main__':
    with psycopg2.connect(database="work_clients", user="postgres", password="123") as conn:
        cur = conn.cursor()

        create_db(conn)
        # create_phone_clients(conn, phone='+79999999999')
        # create_new_clients(conn, "Евгений", "Вовк", "asd@mail.ru", 3)
        # change_date_clients(conn, 1, phone_id=1)
        # delete_client(conn, 4)
        # delete_phone_client(conn, 1)
        print(get_client(conn, first_name="Евгений"))

        conn.commit()
        cur.close()
    conn.close()
