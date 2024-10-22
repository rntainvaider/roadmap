from enum import Enum as E

from sqlalchemy import TIMESTAMP, VARCHAR, Column, Enum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import DeclarativeBase


class TypeGender(E):
    man = "man"
    woman = "woman"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    age = Column(Integer)
    gender = Column(Enum(TypeGender))
    email = Column(String(255), unique=True)

    def __repr__(self) -> str:
        return f"<{self.id=}, {self.first_name=}, {self.last_name=}, {self.age=}, {self.gender=}, {self.email=}>"


class UserFriends(Base):
    __tablename__ = "users_friends"

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    friend_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"<{User.first_name} {User.last_name} {self.friend_id}>"


class UserPost(Base):
    __tablename__ = "users_post"

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text(255))
    created_at = Column(TIMESTAMP, default=func.current_timestamp())
