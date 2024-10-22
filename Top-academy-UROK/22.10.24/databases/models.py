from sqlalchemy import (
    BigInteger,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.mssql import JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(120))
    phone = Column(Integer)

    def __repr__(self) -> str:
        return f"<{self.id=}, {self.firstname=}, {self.lastname=}>"


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey("users.id"))
    to_user_id = Column(Integer, ForeignKey("users.id"))
    body = Column(Text)
    created_at = Column(DateTime)


class FriendRequest(Base):
    __tablename__ = "friend_requests"

    initiator_user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    target_user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    status = Column(String(255))
    requested_at = Column(DateTime)
    confirmed_at = Column(DateTime)


class Communities(Base):
    __tablename__ = "communities"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class UsersCommunities(Base):
    __tablename__ = "users_communities"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    community_id = Column(Integer, ForeignKey("communities.id"), primary_key=True)


class Profiles(Base):
    __tablename__ = "profiles"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    gender = Column(String(1))
    birthday = Column(Date)
    photo_id = Column(Integer)
    create_at = Column(DateTime)
    hometown = Column(String(50))


class Likes(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    media_id = Column(Integer, ForeignKey("media.id"), primary_key=True)
    create_at = Column(DateTime)


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    media_type_id = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    body = Column(Text)
    filename = Column(String(255))
    size = Column(BigInteger)
    metadata = Column(JSON)
    created_at = Column(DateTime)
    update_at = Column(DateTime)
