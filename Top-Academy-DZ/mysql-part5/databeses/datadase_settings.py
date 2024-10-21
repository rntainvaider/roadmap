import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


def get_mysql_connect() -> bool:
    return pymysql.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        port=int(os.getenv('port')),
        database=os.getenv('database')
        )
