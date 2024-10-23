import os
from dotenv import load_dotenv

load_dotenv()

def get_mysql_url() -> str:
    return f"mysql+pymysql://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('localhost')}:{os.getenv('port')}/{os.getenv('database')}"
