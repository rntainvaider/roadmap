from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from databeses1.database_settings1 import get_mysql_url
from databeses1.models1 import Base, User

engine = create_engine(url=get_mysql_url(), echo=True)

Base.metadata.create_all(bind=engine)


def create_new_user(name: str, age: int) -> None:
    with Session(autoflush=False, bind=engine) as db:
        new_user = User(name=name, age=age)
        db.add(new_user)
        db.commit()


def get_all_users():
    with Session(autoflush=False, bind=engine) as db:
        all_user = db.query(User).all()
        return all_user


def get_user_to_id(user_id: int):
    with Session(autoflush=False, bind=engine) as db:
        return db.query(User).filter(User.id == user_id).first()


def rename_user(user_id: int, new_name: str):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.name = new_name
            db.commit()
