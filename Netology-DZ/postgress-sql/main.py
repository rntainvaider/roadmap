import psycopg2

conn = psycopg2.connect(database="work_clients", user="postgres", password="123")

def create_db(conn) -> None:
    cur.execute("CREATE TABLE IF NOT EXISTS client(id SERIAL PRIMARY KEY, first_name VARCHAR(55), last_name VARCHAR(55), email VARCHAR(55));")
    cur.execute("CREATE TABLE IF NOT EXISTS phone_clients(id SERIAL PRIMARY KEY, phone VARCHAR(18), client_id INT, FOREIGN KEY (client_id) REFERENCES client (id));")

def create_new_clients(conn, first_name: str, last_name: str, email: str) -> None:
    cur.execute(f"INSERT INTO client(first_name, last_name, email) VALUES ({first_name}, {last_name}, {email})")

def create_phone_clients(conn, phone: str, client_id: int) -> None:
    cur.execute(f"INSERT INTO phone_clients(phone, client_id) VALUES ({phone}, {client_id})")

def change_date_clients(conn, id_client: int, first_name=None, last_name=None, email=None, phone=None) -> None:
    pass

def delete_phone_client(conn, client_id: int, phone: str) -> None:
    pass

def delete_client(conn, client_id: int) -> None:
    cur.execute(f"DELETE FROM client WHERE id = {client_id}")

def get_client(conn, first_name=None, last_name=None, email=None) -> None:
    cur.execute(f"SELECT * FROM client WHERE first_name={first_name} or last_name={last_name} or email={email}")


with psycopg2.connect(database="work_clients", user="postgres", password="123") as conn:
    cur = conn.cursor()
    create_db(conn)
    create_new_clients(conn, "Евгений", "Вовк", "asd@mail.ru")
    create_phone_clients(conn, "+79998526321", 1)
    delete_client(conn, 3)
    get_client(conn, "Евгений")
    conn.commit()
    cur.close()

conn.close()
