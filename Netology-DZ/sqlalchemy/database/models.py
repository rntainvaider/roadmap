from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import TIMESTAMP, ForeignKey, String, Integer, Column, func


class Base(DeclarativeBase):
    pass

class Publisher(Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(255))

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String(255))
    id_publisher = Column(Integer, ForeignKey("publisher.id"))

class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id_book = Column(Integer, ForeignKey("book.id"))
    id_shop = Column(Integer, ForeignKey("shop.id"))
    count = Column(Integer)

class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(255))

class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    price = Column(Integer)
    date_sale = Column(TIMESTAMP, default=func.current_timestamp)
    id_stock = Column(Integer, ForeignKey("stock.id"))
    count = Column(Integer)
