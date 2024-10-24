from database.database_settings import get_mysql_url
from database.models import Base, Publisher, Book, Stock, Shop, Sale
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

engine = create_engine(url=get_mysql_url())

Base.metadata.create_all(engine)

class DbWorker:
    def __init__(self, engine) -> None:
        self.engine = engine

    def get_book_sale(self, publisher_name: str) -> None:
        with Session(autoflush=False, bind=engine) as bd:
            book = (
                select(Book.title, Shop.name, Sale.price, Sale.date_sale)
                .select_from(Publisher)
                .join(Book, Book.id_publisher == Publisher.id)
                .join(Stock, Book.id == Stock.id_book)
                .join(Shop, Shop.id == Stock.id_shop)
                .join(Sale, Sale.id_stock == Stock.id)
                .filter(Publisher.name == publisher_name)
                )
            print(book)
            result = bd.execute(book).all()
            print(result)


            # SELECT book.title, shop.name, sale.price, sale.date_sale
            # FROM publisher
            # JOIN book ON publisher.id = book.id_publisher
            # JOIN stock ON book.id = stock.id_book
            # JOIN shop ON shop.id = stock.id_shop
            # JOIN sale ON sale.id_stock = stock.id
            # WHERE publisher.id = 1;


DB = DbWorker(engine=engine)
