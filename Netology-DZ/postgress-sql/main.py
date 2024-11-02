import psycopg2

def create_db(conn) -> None:
    cur.execute("CREATE TABLE IF NOT EXISTS client(id SERIAL PRIMARY KEY, first_name VARCHAR(55), last_name VARCHAR(55), email VARCHAR(55));")
    cur.execute("CREATE TABLE IF NOT EXISTS phone_clients(id SERIAL PRIMARY KEY, phone VARCHAR(18), client_id INT, FOREIGN KEY (client_id) REFERENCES client (id));")

def create_new_clients(conn, first_name: str, last_name: str, email: str) -> None:
    cur.execute("INSERT INTO client(first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email))

def create_phone_clients(conn, phone: str, client_id: int) -> None:
    cur.execute("INSERT INTO phone_clients(phone, client_id) VALUES (%s, %s)", (phone, client_id))

def change_date_clients(conn, id_client: int, first_name: str|None=None, last_name: str|None=None, email: str|None=None) -> None:
    cur.execute("UPDATE client SET first_name=%s, last_name=%s, email=%s WHERE id = %s", (first_name, last_name, email, id_client))

def delete_phone_client(conn, client_id: int, phone: str) -> None:
    cur.execute("DELETE FROM phone_clients WHERE client_id = %s", (str(client_id)))

def delete_client(conn, client_id: int) -> None:
    cur.execute(f"DELETE FROM client WHERE id = {client_id}")

def get_client(conn, first_name: str|None=None, last_name: str|None=None, email: str|None=None) -> None:
    cur.execute(f"SELECT * FROM client WHERE first_name={first_name} or last_name={last_name} or email={email}")


with psycopg2.connect(database="work_clients", user="postgres", password="123") as conn:
    cur = conn.cursor()

    create_db(conn)
    create_new_clients(conn, "Евгений", "Вовк", "asd@mail.ru")
    create_phone_clients(conn, "+79998526321", 1)
    change_date_clients(conn, 3, first_name="Павел", last_name="Павлов", email="1132qewqweqwe@gmail.com")
    delete_client(conn, 2)
    delete_phone_client(conn, 1, "79998526321")
    get_client(conn, "Евгений")

    conn.commit()
    cur.close()

conn.close()
