import psycopg2

conn = psycopg2.connect(database="work_clients", user="postgres", password="123")

def create_db(conn) -> None:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phone_clients(id SERIAL PRIMARY KEY, phone VARCHAR(18))")
    cur.execute("CREATE TABLE IF NOT EXISTS client(id SERIAL PRIMARY KEY, first_name VARCHAR(55), last_name VARCHAR(55), email VARCHAR(55), phone_id INT, FOREIGN KEY (phone_id) REFERENCES phone_clients (id));")
    conn.commit()
    cur.close()

def create_new_clients(conn, first_name: str, last_name: str, email: str, phone=None) -> None:
    cur = conn.cursor()
    cur.execute("INSERT INTO client(first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email))
    conn.commit()
    cur.close()

def create_phone_clients(conn, id_client: int, phone: str) -> None:
    cur = conn.cursor()
    cur.execute("INSERT INTO phone_clients VALUES ()")
    cur.close()

def change_date_clients(conn, id_client: int, first_name=None, last_name=None, email=None, phone=None) -> None:
    pass

def delete_phone_client(conn, client_id: int, phone: str) -> None:
    pass

def delete_client(conn, client_id: int) -> None:
    cur = conn.cursor()
    cur.execute("DELETE FROM client WHERE id = %s", (str(client_id)))
    cur.close()

def get_client(conn, first_name=None, last_name=None, email=None, phone=None) -> None:
    


with psycopg2.connect(database="work_clients", user="postgres", password="123") as conn:
    create_db(conn)
    create_new_clients(conn, "Евгений", "Вовк", "asd@mail.ru")
    delete_client(conn, 1)


conn.close()
