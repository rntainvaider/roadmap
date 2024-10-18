from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from databases.databases_settings import get_mysql_url
from databases.models import Answer, Base, Company, Questions, Team, User

engine = create_engine(url=get_mysql_url())

Base.metadata.create_all(bind=engine)


class DbWorker:
    def __init__(self, engine) -> None:
        self.engine = engine

    def create_new_user(
        self, firstname: str, lastname: str, otchevo: str, phone: str, team_id: int
    ) -> None:
        with Session(autoflush=False, bind=self.engine) as bd:
            new_user = User(
                firstname=firstname,
                lastname=lastname,
                otchevo=otchevo,
                phone=phone,
                team_id=team_id,
            )
        bd.add(new_user)
        bd.commit()

    def create_new_team(self, name: str) -> None:
        with Session(autoflush=False, bind=self.engine) as bd:
            new_user = User(name=name)
        bd.add(new_user)
        bd.commit()


DB = DbWorker(engine=engine)
