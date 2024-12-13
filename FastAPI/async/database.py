import sqlite3
from typing import Any


def create_database() -> None:
    with sqlite3.connect("sqlite3.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS quote (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                author TEXT NOT NULL)"""
        )
    connection.commit()
    connection.close()


def add_in_database_quote(quote: str, author: str) -> None:
    with sqlite3.connect("sqlite3.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO quote (text, author) VALUES (?, ?)""", (quote, author)
        )
    connection.commit()
    connection.close()


def get_database_quote() -> list[Any]:
    with sqlite3.connect("sqlite3.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT text, author FROM quote""")
        quote = cursor.fetchall()
        return quote
