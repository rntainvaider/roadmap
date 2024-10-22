from typing import Union

from databases_settings import get_mysql_url
from models import Communities, Likes, Message, Profiles, User, UsersCommunities
from sqlalchemy import create_engine, delete, func, insert, select, update
from sqlalchemy.orm import Session

engine = create_engine(
    url=get_mysql_url(),
    # echo=True
)


def create_new_user(firstname, lastname, email, phone) -> None:
    with Session(autoflush=False, bind=engine) as db:
        new_user = User(firstname=firstname, lastname=lastname, email=email, phone=phone)
        db.add(new_user)
        db.commit()


# new_users = create_new_user("хххх", "хххх", "лавариорва", "9954678389")


def search_user(firstname: str, lastname: str):
    with Session(autoflush=False, bind=engine) as db:
        return (
            db.query(User).filter(User.firstname == firstname, User.lastname == lastname).first()
        )


# user1 = search_user("Ozella", "Hauck")
# print(user1.firstname, user1.lastname, user1.phone, user1.email)
def get_user_to_id(id: int):
    with Session(autoflush=False, bind=engine) as db:
        return db.query(User).filter(User.id == id).first()


def update_user(
    user_id: int, new_firstname: Union[str, None] = None, new_lastname: str = None
) -> None:
    with Session(autoflush=False, bind=engine) as db:
        user: User = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return
        if new_firstname:
            user.firstname = new_firstname
        if new_lastname:
            user.lastname = new_lastname
        db.commit()


def task1() -> None:
    with Session(autoflush=False, bind=engine) as db:
        """SELECT profiles.gender, count(likes.id) as "Наибольшее количество лайков"
        FROM profiles
        join likes ON likes.user_id = profiles.user_id
        GROUP BY profiles.gender
        order by "Наибольшее количество лайков" desc
        LIMIT 1;"""
        query = (
            select(Profiles.gender, func.count(Likes.id))
            .select_from(Profiles)
            .join(Likes, Likes.user_id == Profiles.user_id)
            .group_by(Profiles.gender)
            .order_by(Likes.id.desc)
        )

        """SELECT users_communities.community_id, communities.name, count(user_id) as "Количество пользователей"
        FROM users_communities
        inner join communities
        on users_communities.community_id = communities.id
        group by community_id;"""
        # query = (
        #     select(
        #         UsersCommunities.community_id,
        #         Communities.name,
        #         func.count(UsersCommunities.user_id),
        #     )
        #     .select_from(UsersCommunities)
        #     .join(Communities, UsersCommunities.community_id == Communities.id)
        #     .group_by(UsersCommunities.community_id)
        # )

        # query = (
        #     select(
        #         UsersCommunities.user_id,
        #         User.lastname,
        #         User.firstname,
        #         User.email,
        #         func.count(UsersCommunities.community_id).label("количество_групп"),
        #     )
        #     .select_from(UsersCommunities)
        #     .join(User, User.id == UsersCommunities.user_id)
        #     .group_by(User.id)
        # )

        # query = (
        #     select(User, Profiles.birthday, func.count(User.id).label("Кол-во_пользователей"))
        #     .select_from(User)
        #     .join(Profiles, User.id == Profiles.user_id)
        #     .filter(User.id > 1, User.id < 10)
        #     .group_by(User.id)
        #     .order_by(User.firstname)
        # )
        print(query)
        result = db.execute(query).all()
        print(result)


task1()
