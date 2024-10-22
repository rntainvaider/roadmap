from enum import Enum as E

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase


class TypeCompany(E):
    cool = "cool"
    hot = "hot"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    firstname = Column(String(255))
    lastname = Column(String(255))
    otchevo = Column(String(255))
    phone = Column(String(255), unique=True)
    team_id = Column(Integer, ForeignKey("teams.id"))


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(255))


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(255))
    type_company = Column(Enum(TypeCompany))
    team_id = Column(Integer, ForeignKey("teams.id"))


class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    label = Column(String(255))
    text = Column(Text)
    points_cool = Column(Integer)
    points_hot = Column(Integer)


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    text = Column(Text)
    questions_id = Column(Integer, ForeignKey("questions.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
