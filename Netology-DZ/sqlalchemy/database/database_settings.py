# import os
# from dotenv import load_dotenv

# load_dotenv()

from database.settings import user, password, localhost, database, port

def get_mysql_url() -> str:
    return f"postgresql://{user}:{password}@{localhost}:{port}/{database}"
    # return f"mysql+pymysql://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('localhost')}:{os.getenv('port')}/{os.getenv('database')}"
