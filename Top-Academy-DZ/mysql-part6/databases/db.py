from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from databases.database_settings import get_mysql_url
from databases.models import Base, User, UserFriends, UserPost

engine = create_engine(url=get_mysql_url())

Base.metadata.create_all(bind=engine)


class DbWorker:
    def __init__(self, engine) -> None:
        self.engine = engine

    def add_user(self, first_name: str, last_name: str, age: int, gender, email: str):
        with Session(autoflush=False, bind=self.engine) as bd:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                age=age,
                gender=gender,
                email=email,
            )
            bd.add(new_user)
            bd.commit()
            print(f"Пользователь {first_name} {last_name} добавлен успешно.")

    def delete_user(self, user_id: int) -> None:
        with Session(autoflush=False, bind=self.engine) as bd:
            user = bd.query(User).filter(User.id == user_id).first()
            if user:
                bd.delete(user)
                bd.commit()
                print(f"Пользователь {user.first_name} {user.last_name} удалён успешно.")
            else:
                print("Пользователя не существует!")

    def update_user(
        self,
        user_id: int,
        first_name: str | None,
        last_name: str | None,
        age: int | None,
        gender=None,
        email: str | None,
    ) -> None:
        with Session(autoflush=False, bind=self.engine) as bd:
            user = bd.query(User).filter(User.id == user_id).first()
            if user:
                if first_name:
                    user.first_name = first_name
                if last_name:
                    user.last_name = last_name
                if age:
                    user.age = age
                if gender:
                    user.gender = gender
                if email:
                    user.email = email
                bd.commit()
                print(f"Пользователь {user_id} успешно изменен.")
            else:
                print("Пользователя не существует!")

    def search_user(self, first_name: str, last_name: str) -> None:
        with Session(autoflush=False, bind=self.engine) as bd:
            users = (
                bd.query(User)
                .filter(User.first_name == first_name, User.last_name == last_name)
                .all()
            )

            if users:
                for user in users:
                    print(
                        f"ID: {user.id}, Name: {user.first_name} {user.last_name}, Age: {user.age}, Gender: {user.gender}, Email: {user.email} "
                    )
            else:
                print("Пользователя не существует!")

    def add_user_friends(self, user_id: int, friend_id: int) -> None:
        with Session(autoflush=False, bind=self.engine) as bd:
            user_friends = UserFriends(user_id=user_id, friend_id=friend_id)
            bd.add(user_friends)
            bd.commit()
            print(f"Дружба между {user_id} и {friend_id} добавлена.")

    def add_user_post(self, user_id: int, content: str):
        with Session(autoflush=False, bind=self.engine) as bd:
            user_post = UserPost(user_id=user_id, content=content)
            bd.add(user_post)
            bd.commit()
            print(f"Пользователь {user_id} добавил пост.")


DB = DbWorker(engine=engine)
